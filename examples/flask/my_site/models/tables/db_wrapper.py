def build_if_needed(db):
    """Little helper method for making tables in SQL-Alchemy with SQLite"""
    if len(db.engine.table_names()) == 0:
        # import all classes here
        from my_site.models.tables.user import User

        db.create_all()
