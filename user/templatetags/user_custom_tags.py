from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter()
def strip(value):
    return str(value).strip()

@register.filter()
def original_username(value):
    return value.__class__.objects.get(pk=value.id).get_username()

@register.filter()
def class_name(value):
    return value.__class__.__name__

@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()