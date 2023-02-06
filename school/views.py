from django.shortcuts import render, redirect
from .forms import StudentForm,LoginPage
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def form_view(request):
    form = StudentForm
    context={'form':form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_form')
    return render(request, 'register_form.html',context)


    
def student_login(request):
    form = LoginPage
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            return HttpResponse('Invalid')
        

    return render(request, 'login_form.html',{'form':form})
