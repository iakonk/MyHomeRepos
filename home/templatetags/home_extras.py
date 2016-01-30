from django.template import Library

register = Library()


@register.filter
def filter_list_by(obj_list, string):
    """
    Function filters given dictionary by given article type
    :param obj_list:  objects list
    :param string: two-characters type of the article
    :return: list of objects where object.article_type == string
    """
    return [obj for obj in obj_list if obj['article_type'] == string]
register.filter('filter_list_by', filter_list_by)


@register.filter
def draw_stars(value):
    """
    Function receives a number as a string and returns list range (no more than 5)
    :param value: end value of the range
    :return: list of iterable items
    """
    pass
register.filter('draw_stars', draw_stars)
