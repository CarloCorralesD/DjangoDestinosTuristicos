from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def register(request):
	if request.method =="POST":
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"username ya existe")
				return redirect("register")
			elif User.objects.filter(email=email).exists():
				messages.info(request,"email ya existe")
				return redirect("register")
			else:
				user = User.objects.create_user(username=username, password=password1,first_name=first_name,last_name=last_name,email=email)
				user.save()
				messages.info(request,"usuario creado")
		else:
			messages.info(request,"la contraseña no coincide durante la confirmación")
			return redirect("register")
		return redirect("/")

	else:
		context = {}
		return render(request,"register.html",context)
