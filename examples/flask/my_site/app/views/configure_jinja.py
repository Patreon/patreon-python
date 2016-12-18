import jinja2

from my_site.app import views


class DependencyBubbler:
    def __init__(self, base_module):
        self.base_module = base_module

    def __getattribute__(self, name):
        base_module = object.__getattribute__(self, 'base_module')
        template = getattr(base_module, name, None)
        if template is None:
            raise AttributeError
        return template


def configure(app):
    my_template_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(['my_site/app/views'])
    ])
    app.jinja_loader = my_template_loader
    app.jinja_env.globals.update(
        views=DependencyBubbler(views),
    )
