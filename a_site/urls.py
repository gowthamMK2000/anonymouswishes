from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='a_site'

urlpatterns=[
	path('',views.index,name='index'),
	path('validate/',views.validate,name='validate'),
	path('insert/',views.insert,name='insert'),
	path('wishes/',views.wishes,name='wishes'),
	
] + static(settings.STATIC_URL,decument_root=settings.STATIC_ROOT)
