from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
	dest1 = Destination.objects.get(id=1)
	dest2 = Destination.objects.get(id=2)
	dest3 = Destination()
	# dest1.name = "Arequipa"
	# dest1.desc = "La ciudad blanca"
	# dest1.img = 'arequipa.jpg'
	# dest1.offer = True
	# dest1.price = 90
	# dest2.name = "Cuzco"
	# dest2.desc = "La capital arqueologica de America"
	# dest2.img = "cuzco.jpg"
	# dest2.offer = False
	# dest2.price = 200
	# dest3.name = "Lima"
	# dest3.desc = "La ciudad de los Reyes"
	# dest3.img = "lima.jpg"
	# dest3.offer = False
	# dest3.price = 150

	dests = [dest1,dest2,dest3]


	context = {
		'dests' : dests,
	}
	return render(request,"index.html",context)