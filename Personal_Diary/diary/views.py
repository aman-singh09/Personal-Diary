from django.shortcuts import render,HttpResponse,redirect
from .models import Diary
from django.contrib.auth.models import User,auth 
from django.contrib.auth import logout,authenticate,login

# Create your views here.

def homepage(request):
	return render(request, 'home-page.html')

def index(request):
	diary = Diary.objects.filter(user=request.user)
	for d in diary:
		d.content = d.content[0:200]
		d.content+="...";
	return render(request,'index.html',{'diary':diary})

def new(request):
	if request.method == 'POST':
		user = request.user	
		title=request.POST['title']
		content=request.POST['content']
		mood=request.POST['mood']
		details= Diary(user=user,title=title,content=content,mood=mood)
		details.save()
	return render(request,'new-entry.html')

def about(request):
  return render(request,'about.html')

def view(request,d_id):
	try:
		diary = Diary.objects.get(user=request.user,id = d_id)
	except:
		return redirect('home')
	return render(request,'show.html',{'diary':diary})

def signin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user= authenticate(username=username, password= password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return redirect('login')

	return render(request,'credentials.html')

def signout(request):
	logout(request)
	return redirect("login")

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