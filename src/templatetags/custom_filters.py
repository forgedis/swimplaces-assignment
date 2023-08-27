from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name='get_fields_and_values')
def get_fields_and_values(instance):
    field_value_pairs = []
    for field in instance._meta.fields:
        field_name = field.verbose_name
        field_value = getattr(instance, field.name, None)

        if field_name == "longitude":
            field_value = format(field_value, '.6f')
        
        if field_name == "latitude":
            field_value = format(field_value, '.6f')

        if field_name == "rating":
            if field_value:
                field_value = format(Decimal(field_value), '.2f')
        
        if field_value and field.is_relation:
            field_value = field_value.name
        
        field_value_pairs.append((field_name, field_value))
    return field_value_pairs