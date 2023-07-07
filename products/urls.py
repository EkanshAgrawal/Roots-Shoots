from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.items_display, name='itemlist'),
    path('items/<slug:the_slug>', views.itemView, name='itemView'),
    path('items/review/<slug:the_slug>', views.addReview, name='addReview'),
    path('product_upload', views.product_upload, name='product_upload'),
    path('cart', views.cart, name='cart'),
    path('clear_cart', views.clear_cart, name='clear_cart'),
    path('faq', views.faq, name='faq'),
    path('checkout', views.checkout, name='checkout'),
    path('our_team', views.our_team, name='our_team'),
    path('success', views.success, name='success'),
    path('order_success', views.order_success, name='order_sucess'),
]