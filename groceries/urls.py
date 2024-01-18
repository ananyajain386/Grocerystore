from django.urls import path

from . import views

urlpatterns = [
     path('register', views.register, name='register'),
     path('login1', views.login1, name='login1'),
     # path('logout', views.logout, name='logout'),
     path('section', views.section, name='section'),
     # path('send_file', views.send_file, name='send_file'),
     path('product', views.product, name='product'),
     path('deletesection', views.deletesection, name='deletesection'),
     path('deleteproduct', views.deleteproduct, name='deleteproduct'),
     path('editsection', views.editsection, name='editsection'),
     path('editproduct', views.editproduct, name='editproduct'),
     path('addtocart', views.addtocart, name='addtocart'),
     path('cartview', views.cartview, name='cartview'),
     path('removefromcart', views.removefromcart, name='removefromcart'),
     path('qtyinc', views.qtyinc, name='qtyinc'),
     path('buynow', views.buynow, name='buynow'),
     path('buycart', views.buycart, name='buycart'),
     # path('searchpro', views.searchpro, name='searchpro')    
]