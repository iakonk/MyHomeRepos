from django.template.defaultfilters import register


@register.filter(name='dict_key')
def dict_key(d, k):
    return d[k]


@register.filter(name='in')
def inside(key, dict_):
    return key in dict_


@register.filter(name='range')
def filter_range(start, end):
    return range(start, end + 1)
