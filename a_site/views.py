from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse

from .models import Wishes

from django.utils import timezone

def index(request,uname):
	uname="Afridy"
		
	return render(request,'a_site/index1.html',{'uname':uname})

def insert(request,uname):
	return render(request,'a_site/insert.html',{'uname':uname})

def wishes(request,uname):
	w = Wishes.objects.all().order_by('idate').reverse()
	return render(request,'a_site/wishes.html',{'wishes':w,'uname':uname})

def validate(request,uname):
	wish = request.POST['wish']
	name = request.POST['wname'] 
	new = Wishes(name=name, w_text = wish,idate=timezone.now())
	new.save()
	return HttpResponseRedirect(reverse('a_site:wishes',args=[uname]))



