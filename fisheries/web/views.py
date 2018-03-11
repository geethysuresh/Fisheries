from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Profile


class HomeView(TemplateView):

	template_name = 'home.html'


class ContactView(TemplateView):

	template_name = 'contact.html'

class LoginSignupView(TemplateView):
	template_name='index.html'

class CategoriesView(TemplateView):
	template_name='categories.html'

class UserSignup(View):

	def post(self, request, *args, **kwargs):
		
		try:
			User.objects.get(email=request.POST['email'].lower())
		except:
			user = User.objects.create(username=request.POST['email'].lower(),
				first_name=request.POST['fname'], last_name=request.POST['lname'],
				email=request.POST['email'].lower())
			user.set_password(request.POST['password'])
			user.save()
			profile = Profile.objects.create(user=user, mobile=request.POST['mobile'])
		return HttpResponseRedirect("/")

class LoginView(View):

	def post(self, request, *args, **kwargs):

		user = authenticate(username=request.POST['email'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			messages.success(request, "You are successfully logged in")
		else:
			messages.error(request, "Please check the username and password")
		return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    messages.success(request, "You are successfully logged out")
    return HttpResponseRedirect("/")

