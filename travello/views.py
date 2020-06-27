from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
	dest1 = Destination()
	dest1.name = "Arequipa"
	dest1.desc = "La ciudad blanca"
	dest1.img = 'arequipa.jpg'
	dest1.price = 90.05

	context = {
		'dest1' : dest1,
	}
	return render(request,"index.html",context)