from django.shortcuts import render,HttpResponse
from .models import Diary

# Create your views here.
def index(request):
	diary = Diary.objects.all()
	return render(request,'index.html',{'diary':diary})

def new(request):
  return render(request,'new-entry.html')

def about(request):
  return render(request,'about.html')

def view(request,d_id):
	diary = Diary.objects.get(id = d_id)
	return render(request,'show.html',{'diary':diary})