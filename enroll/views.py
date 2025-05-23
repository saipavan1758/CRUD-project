from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['password']
   reg = User(name=nm, email=em, password=pw)
   reg.save()
   fm = StudentRegistration()
   messages.add_message(request, messages.SUCCESS,"Your Data has been Submitted!!")
   messages.add_message(request, messages.INFO,"NOW YOU CAN LOGIN!!")
   
   
 else:
  fm = StudentRegistration()
 stud = User.objects.all()
 
 
 return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)

  fm = StudentRegistration(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = User.objects.get(pk=id)
  fm = StudentRegistration(instance=pi)
 return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')
 

 def show_feedbacks(request):
    feedbacks = Feedback.objects.all()  # Get all rows from DB
    return render(request, 'feed/show_feedbacks.html', {'feedbacks': feedbacks})