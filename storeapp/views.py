from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.views.generic import TemplateView
from paginator import Paginator

from .models import Department

def home(request):
    departments = Department.objects.all()
    return render(request, 'base.html', {'departments': departments})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request, 'Please fill out all the fields.')
            return render(request, 'login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('new_page')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')

        else:
                messages.info(request,"password not match")
                return redirect('register')
        return redirect('/')

    return render(request,"register.html")


class DepartmentListView(TemplateView):
    template_name = 'departments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

#

def new_page(request):
    return render(request, 'new_page.html')



from .forms import OrderForm

def form_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # form = OrderForm()
            # print(form.cleaned_data)
            messages.success(request, 'Success!!')
            return redirect('base')
    else:
        form = OrderForm()
    return render(request, 'form_page.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')





