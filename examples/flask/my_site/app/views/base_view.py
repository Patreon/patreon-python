from flask import render_template
from jinja2 import Markup


class View:
    def __init__(self, *args, **kwargs):
        self._template_data = None

    def get_data(self):
        if self._template_data is None:
            self._template_data = self.data()
        return self._template_data

    def data(self):
        return {}

    def context(self):
        context = {}
        context.update(self.get_data())
        return context

    def render(self):
        template = self.template()
        if template is not None:
            context = self.context()
            html = render_template(template, **context)
            return Markup(html)
        else:
            raise Exception("Unable to render view: {0}".format("TODO"))

    def template(self):
        # Override in subclass.
        return None
