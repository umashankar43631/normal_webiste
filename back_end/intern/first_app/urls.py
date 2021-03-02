from django.conf.urls import url
from django.urls import path
from . import views
# Template URL's
app_name = 'first_app'

urlpatterns = [

    path('',views.home, name = 'home'),
    path('about/',views.about, name = 'about'),
    path('blog/', views.blog, name = 'blog'),
    path('contactUs/',views.contactUs, name ='contactus'),
    path('index/',views.index, name ='index'),
    path('post_1/', views.post_1, name = 'post_1'),
    path('post_2/', views.post_2, name = 'post_2'),
    path('post_3/', views.post_3, name = 'post_3'),
    path('post_4/', views.post_4, name = 'post_4'),
    path('post_5/', views.post_5, name = 'post_5'),
    path('cart/', views.cart, name = 'cart'),
    path('post/', views.post, name = 'post'),
    path('product/', views.product, name = 'product'),
    path('services/', views.services, name = 'services'),
    path('register/',views.user_signup, name = 'user_signup'),
    path('login/',views.user_login, name = 'user_login')
    

]
#need to add after running server
#path('login/', views.login, name = 'login'),