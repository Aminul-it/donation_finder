from django.urls import path
from Event_app import views
app_name = 'event_app'

urlpatterns = [
   path('', views.EventList.as_view(),name='EventList'),
   path('write/',views.create_event.as_view(),name='create_event'),
   path('detailes/<slug>/', views.event_details,name='event_details'),
   path('like/<pk>/',views.like,name='like'),
   path('unlike/<pk>/',views.unlike,name='unlike'),

   path('', views.home_donate, name='home_donate'),
   path('success',views.success , name='success'),
   path('my_event/', views.my_event.as_view(), name='my_event'),
   path('edit/<pk>', views.UpdateEvent.as_view(), name='UpdateEvent'),



]
