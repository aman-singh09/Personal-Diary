from django.shortcuts import render,HttpResponse,redirect
from .models import Diary
from django.contrib.auth.models import User,auth 
from django.contrib.auth import logout,authenticate,login

# Create your views here.
def index(request):
	diary = Diary.objects.all()
	for d in diary:
		d.content = d.content[0:200]
		d.content+="...";
	return render(request,'index.html',{'diary':diary})

def new(request):
  return render(request,'new-entry.html')

def about(request):
  return render(request,'about.html')

def view(request,d_id):
	diary = Diary.objects.get(id = d_id)
	return render(request,'show.html',{'diary':diary})

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user= authenticate(username=username, password= password)
		if user is not None:
			login(user,request)
			return redirect("/")
		else:
			return render(request,'/login')

	return render(request,'credentials.html')

# def logout(request):
# 	return render()
def registration(request):
	if request.method == 'POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		user= User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
		user.save();
		print("User created !")
		return redirect('/')
		
	else:
		return render(request,'registration.html')