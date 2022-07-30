from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='index'),
    path('service/',views.services,name='service'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('register/',views.user_register_view,name='register'),
    path('login/',views.user_login_view,name='login'),
    path('logout/',views.User_logout,name='logout'),


    path('booking/<int:pk>/',views.book_room,name='booking'),
    # path('search/',views.service,name='search'),
]
