from django import template

register = template.Library()

@register.filter
def currency(value):
    return f"₹{value}"

@register.filter
def discounted_value(value, percentage):
    return f"Discounted Price: ₹{int(int(value) - (int(value)*(int(percentage)/100)))}"
