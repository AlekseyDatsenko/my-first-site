from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image, Info, About, About_ru

def main_en(request):
	posts = Image.objects.all
	return render(request, 'img/images.html', {'posts': posts})

def tel(request):
	contact = Info.objects.all
	return render(request, 'img/contact.html', {'contact':contact})

def info(request):
	inform = About.objects.all
	return render(request, 'img/info.html', {'inform':inform})

def main_ru(request):
	posts = Image.objects.all
	return render(request, 'img/images_ru.html', {'posts': posts})	

def tel_ru(request):
	contact = Info.objects.all
	return render(request, 'img/contact_ru.html', {'contact':contact})

def info_ru(request):
	inform = About_ru.objects.all
	return render(request, 'img/info_ru.html', {'inform':inform})
