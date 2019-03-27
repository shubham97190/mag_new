from django import template
register = template.Library()

@register.filter(name='add_attr')
def add_attr(field_name,css_class):
    attrs = {}
    definition = css_class.split(',')
   
    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val
    
    return field_name.as_widget(attrs=attrs)

   

