from django import template

register = template.Library()


@register.filter()
def media_filter_blog(path):
    if path:
        return f"/media/{path}"
    else:
        return "#"
