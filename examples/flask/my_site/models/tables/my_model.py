from flask.ext.sqlalchemy import Model
from sqlalchemy import inspect
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Insert


class InsertOnDuplicate(Insert):
    pass


@compiles(InsertOnDuplicate)
def insert_on_duplicate(insert, compiler, **kwargs):
    text = compiler.visit_insert(insert, **kwargs)
    text += ' ON DUPLICATE KEY UPDATE '

    if insert._has_multi_parameters:
        stmt_parameters = insert.parameters[0]
    else:
        stmt_parameters = insert.parameters

    update_columns = []

    # retrieve all relevant columns from table
    for column in insert.table.columns:
        if not column.primary_key and column.key in stmt_parameters:
            update_columns.append(column)

    text += ', '.join(
        '{0} = VALUES({0})'.format(compiler.visit_column(c))
        for c in update_columns
    )

    return text


class MyModel(Model):
    """Custom base class used as mixin for SQLAlchemy Models."""

    def __columns__(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns if
                getattr(self, column.name) is not None}

    def as_dict(self):
        return self.__columns__()

    def __repr__(self):
        attributes = self.__columns__()
        attributes_strings = ['{0}={1}'.format(k, v) for k, v in attributes.items()]
        attributes_combined = ' '.join(attributes_strings)
        return 'Model<{0}>: {1}'.format(self.__class__.__tablename__, attributes_combined)

    def __eq__(self, other):
        return (self.__class__ == other.__class__) and (self.__columns__() == other.__columns__())

    @classmethod
    def __get_primary_keys(cls):
        primary_keys = inspect(cls).primary_key
        return [key.name for key in primary_keys]

    def __get_primary_key_dict(self):
        primary_keys = self.__get_primary_keys()
        return {key: getattr(self, key) for key in primary_keys}

    @classmethod
    def __args_to_valid_kwargs(cls, args, kwargs, primary_keys):
        temp_keys = primary_keys.copy()

        for key in kwargs.keys():
            temp_keys.remove(key)

        if len(args) != len(temp_keys):
            raise Exception("Args and kwargs do not cover all primary keys")

        for key, value in zip(temp_keys, args):
            kwargs[key] = value

        if len(list(kwargs.keys())) != len(primary_keys):
            raise Exception("Args and kwargs do not cover all primary keys")

        for key in kwargs.keys():
            if key not in primary_keys:
                raise Exception(key + " not in primary keys for " + cls.__name__)

        return kwargs

    @classmethod
    def __get(cls, *args, **kwargs):
        primary_keys = cls.__get_primary_keys()

        kwargs = cls.__args_to_valid_kwargs(args, kwargs, primary_keys)

        working_query = cls.query

        for key in kwargs.keys():
            working_query = working_query.filter(getattr(cls, key) == kwargs[key])

        return working_query

    @classmethod
    def get(cls, *args, **kwargs):
        return cls.__get(*args, **kwargs).first()

    @classmethod
    def get_with_lock(cls, *args, **kwargs):
        return cls.__get(*args, **kwargs).with_for_update().first()

    @classmethod
    def primary_key_from_insert_or_update(cls, execution_result):
        inserted_params = execution_result.last_inserted_params()
        primary_keys = cls.__get_primary_keys()
        if len(primary_keys) > 0:
            insertion_results = []
            for primary_key in primary_keys:
                if primary_key in inserted_params:
                    insertion_results.append(inserted_params[primary_key])
                else:
                    break
            if len(insertion_results) == len(primary_keys):
                return insertion_results
        return execution_result.inserted_primary_key

    @classmethod
    def insert(cls, insert_values):
        from my_site.app import db

        result = db.session.execute(cls.__table__.insert().values(insert_values))
        return cls.primary_key_from_insert_or_update(result)

    @classmethod
    def insert_ignore(cls, insert_values):
        from my_site.app import db

        result = db.session.execute(
            cls.__table__.insert(prefixes=['OR ignore']).values(insert_values))
        return cls.primary_key_from_insert_or_update(result)

    @classmethod
    def insert_on_duplicate_key_update(cls, insert_values):
        from my_site.app import db

        insert_operation = cls.__table__.insert().prefix_with("OR REPLACE").values(insert_values)
        result = db.session.execute(insert_operation)
        return cls.primary_key_from_insert_or_update(result)

    def delete(self):
        self.query.filter_by(**self.__get_primary_key_dict()).delete()

    def update(self, update_values):
        self.query.filter_by(**self.__get_primary_key_dict()).update(update_values)