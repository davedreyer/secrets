from django.shortcuts import render, redirect
from .models import Secret, Like

def index(request):
	if request.method == "GET":
		context = {
				"secrets": Secret.objects.all().order_by('-created_at'),
				"likes": Like.objects.all()
				
			}	
		return render(request, 'first_app/index.html', context)

	elif request.method == "POST":	
		Secret.objects.create(secret=request.POST['secret'])
		return redirect('/')

def like(request, secret_id):
	Like.objects.create(secret=secret_id)
	return redirect('/')

