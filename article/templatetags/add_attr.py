from django import template
register = template.Library()


@register.filter(name='add_attr')
def add_attr(field_name,css_class):
    attrs = {}
    definition = css_class.split(',')
    print(field_name,'shubham')
    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val
    print(field_name)
    return field_name.as_widget(attrs=attrs)

# :"class:form-control"