from django.template.defaulttags import register

@register.filter
def get_plant_Cat(dictionary, key):
    return dictionary.get(str(key))
