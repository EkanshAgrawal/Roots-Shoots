from django.template.defaulttags import register
from products.models import UserCart
@register.simple_tag
def item_count(user):
    count = UserCart.objects.filter(user = user)
    return len(count)
