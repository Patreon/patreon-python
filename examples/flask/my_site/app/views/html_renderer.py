from flask import render_template, request, session


def render_page(
        base_template_path='BasePage/base_page.html',
        inner=None,
        title='Patreon OAuth Example: Flask Server',
        **kwargs
):
    inner_template = inner(**kwargs)
    return render_template(
        base_template_path,
        request=request,
        session=session,
        inner=inner_template.render(),
        title=title
    )
