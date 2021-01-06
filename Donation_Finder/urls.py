
from django.contrib import admin
from django.urls import path ,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static , staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Event_app/',include('Event_app.urls')),
    path('app_login/',include('app_login.urls')),
    path('',views.index,name='index'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
