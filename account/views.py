from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import CustomUser
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import re
from django.core.validators import validate_email

# Create your views here.


def registration(request):
    phone_number_patter = '^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
    if request.user.is_authenticated and request.user.is_active:
        return redirect()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        country_code = +91
        phone_number = int(str(phone_number) + str(country_code))


        if not any(letter.isalpha() for letter in username) or len(username) < 3:
            messages.error(request, 'Enter valid username')
            return redirect('')
    
        elif not re.match(phone_number_patter, phone_number):
            messages.error(request, 'Enter valid mobile number')
            return redirect()
        
        elif len(password) < 8 or password == '':
            messages.error('password should be 8 cherancter')
            return redirect()
        
        try:
            validate_email(email)
        except:
            messages.error(request, 'invalid Email!')
            return redirect('account:')
        

        if CustomUser.objects.filter(Q(username=username) or Q(phone_number=phone_number)).exists():
            messages.error(request, 'username or phone number is already exits!')
        else:
            CustomUser.objects.create_user(username=username, email=email, phone_number=phone_number, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect()
            else:
                return redirect()
    return render()



def login(request): 
    if request.user.is_authenticated and request.user.is_active:
        return redirect('account:')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, usernaem=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:user_home') 
        else:
            messages.error(request, 'email or password is incorrect!')        
    return render(request, 'html')


def logout(request):
    if request.user.is_authenticated:
        logout(request)
        request.session.flush()         
        return redirect('user_app:user_home')
    


def home(request):
    user = request.user
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'html', {'user':user})
    else:
        return render(request, 'html', {'user':user})
    

        

