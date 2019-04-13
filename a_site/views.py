from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse

from .models import Wishes

from django.utils import timezone

def index(request):
	return render(request,'a_site/index1.html')

def insert(request):
	return render(request,'a_site/insert.html')

def wishes(request):
	w = Wishes.objects.all()
	return render(request,'a_site/wishes.html',{'wishes':w})

def validate(request):
	w = request.POST['wish']
	n = request.POST['wname'] 
	new = Wishes(name=n, w_text = w,idate=timezone.now())
	new.save()
	return HttpResponseRedirect(reverse('a_site:index'))



