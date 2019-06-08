from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'ShopHome'),
    path('about', views.about, name = 'AboutUs'),
    path('contact', views.contact, name = 'ContactUs'),
    path('mycart', views.myCart, name = 'MyCart'),
    path('tracker', views.tracker, name = 'TrackingStatus'),
    path('search', views.search, name = 'Search'),
    path('checkout', views.checkout, name = 'Checkout'),
    path('products/<int:myId>', views.productView, name = 'ProductView')
]