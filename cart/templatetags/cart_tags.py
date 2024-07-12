from django import template

register = template.Library()

@register.simple_tag
def get_price(sushi, amount):
    return sushi.price * amount