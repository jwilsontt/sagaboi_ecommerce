from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

def home_page(request):
	context = {
		"title":"Sagaboi Styles",
		"content":"Welcome to the home of fashion diversity",
	}
	if request.user.is_authenticated():
		context["premium_content"] = "This is your exclusive content."
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title":"About Us",
		"content":"About page holder"
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm()
	context = {
		"title":"Contact",
		"content":"Contact page holder",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request, "contact/view.html", context)
