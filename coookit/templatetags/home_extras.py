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
