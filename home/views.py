from django.shortcuts import render, HttpResponse, redirect
from .models import RoomDetails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import BookingForm
import datetime

@login_required(login_url='login')
def home(request):
    return render(request,'home/index.html')

@login_required(login_url='login')
def services(request):
    context = {
        'service': RoomDetails.objects.all(),
        'services': RoomDetails.objects.filter(availability=True)
        }
    return render(request,'home/service.html',context)
    
    return render(request,'home/service.html')

# def search(request):
#     query = request.GET['query']
#     allRoom=RoomDetails.objects.filter(types__icontains=query)
#     params = {'allRoom':allRoom}
#     return render(request,'home/search.html',params)
#     return HttpResponse('This is search')

@login_required(login_url='login')
def index(request):
    return render(request,'home/index.html')

@login_required(login_url='login')
def about(request):
    return render(request,'home/about.html')

@login_required(login_url='login')
def blog(request):
    return render(request,'home/blog.html')

def user_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        confirm_password = request.POST.get('confirm_password')  
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print ('User exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('User register successfully. Please login with the same username and password')
                return redirect('login')
        else:
            print('Password did not match')

    return render(request, 'home/register.html')


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('Login Successfull')
            return redirect('index')
        else:
            messages.error(request,'Invalid Username and Password')
    return render(request, 'home/login.html')


@login_required(login_url='login')
def User_logout(request):
    logout(request)    
    return redirect('login')



@login_required(login_url='login')
def book_room(request, pk):
    form = BookingForm()
    room = RoomDetails.objects.get(id=pk)
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            curent_date = datetime.date.today()
            check_out_date =  form.cleaned_data['check_out_date']
            check_in_date =  form.cleaned_data['check_in_date']
            if check_out_date < curent_date:
                print('Invalid check out date')
            elif check_in_date < curent_date:
                print('Invalid check in date. Check in date must be greate or equal to todays date')
            else:
                room.availability = False
                room.save()
                form.save()
                return redirect('index')
    context = {
        'room': room,
        'form': form,
    }
    return render(request, 'home/booking.html', context)


