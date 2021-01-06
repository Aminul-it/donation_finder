from django.urls import path
from app_login import views
app_name = 'login_app'

urlpatterns = [
   path('signup/', views.signup,name='signup'),
   path('login/', views.loginpage,name='loginpage'),
   path('logoutpage', views.logoutpage,name='logoutpage'),
   path('user_profile/', views.user_profile, name='user_profile'),
   path('user_change/',views.user_change, name='user_change'),
   path('password/',views.change_password,name='change_password'),
   path('pro_pic_add/',views.pro_pic_add,name='pro_pic_add'),
   path('change_user_pic',views.change_user_pic,name='change_user_pic'),
]
