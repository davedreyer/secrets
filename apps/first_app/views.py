from django.shortcuts import render, redirect

def index(request):
	return render(request, 'first_app/index.html')

def ninjas(request, color = None):

	if color == None:
		ninjas = ['first_app/images/leonardo.jpg','first_app/images/michelangelo.jpg','first_app/images/raphael.jpg','first_app/images/donatello.jpg']
		context = {'ninjas': ninjas}	

	elif color == 'blue':
		context = {'ninjas': ['first_app/images/leonardo.jpg']}

	elif color == 'orange':
		context = {'ninjas': ['first_app/images/michelangelo.jpg']}	
	
	elif color == 'red':
		context = {'ninjas': ['first_app/images/raphael.jpg']}	

	elif color == 'purple':
		context = {'ninjas': ['first_app/images/donatello.jpg']}		

	else: 
		context = {'ninjas': ['first_app/images/notapril.jpg']}	

	return render(request, 'first_app/ninjas.html', context)	
