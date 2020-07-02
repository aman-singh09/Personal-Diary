from django.shortcuts import render,HttpResponse
from .models import Diary

# Create your views here.
def index(request):
	diary = Diary.objects.all()
	return render(request,'home.html',{'diary':diary})

def new(request):
  return render(request,'new-entry.html')

def about(request):
  return render(request,'about.html')