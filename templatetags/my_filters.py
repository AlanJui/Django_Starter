from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    Removes all values of arg from the given string
    :param value:
    :param arg:
    :return:
    """

    return value.replace(arg, '')

@register.filter
def lower(value): # Only one argument.
    """
    Converts a string into all lowercase
    :param value:
    :return:
    """
    return value.lower()

# register.filter('cut', cut)
# register.filter('lower', lower)