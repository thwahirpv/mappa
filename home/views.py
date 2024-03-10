from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import re


# Create your views here.


def raise_complant(request):
    phone_number_patter = '^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$'
    url = 'home:complant'
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        state = request.POST.get('state')
        address = request.POST.get('address')
        country_code = +91
        phone_number = int(str(country_code) + str(phone_number))

        if name == '' or len(name) < 3:
            messages.error(request, 'Enter valid name')
            return redirect(url)
        elif re.match(phone_number_patter, phone_number):
            messages.error(request, 'Enter valid phone number')
            return redirect(url)
        elif not any(letter.isalpha() for letter in state) or state == '':
            messages.errro(request, 'Enter state!') 
            return redirect(url)
        elif address == '':
            messages.error(request, 'Enter address!')
            redirect(url)
    return render('html')



