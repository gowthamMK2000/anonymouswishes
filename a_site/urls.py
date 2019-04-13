from django.urls import path

from . import views

app_name='a_site'

urlpatterns=[
	path('',views.index,name='index'),
	path('validate/',views.validate,name='validate'),
	path('insert/',views.insert,name='insert'),
	path('wishes/',views.wishes,name='wishes'),
]
