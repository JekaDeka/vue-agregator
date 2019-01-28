from django import template

register = template.Library()


@register.inclusion_tag('core/include/left_menu.html')
def left_menu():
  pass


@register.inclusion_tag('core/include/rigth_menu.html')
def rigth_menu():
  pass


@register.inclusion_tag('core/include/selection_one.html')
def selection_one():
  pass


@register.inclusion_tag('core/include/main_link.html')
def main_link():
  pass
