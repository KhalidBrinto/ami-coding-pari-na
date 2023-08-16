from django.shortcuts import render, redirect
from .algorithms import binarySearch
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from .models import InputHistory
from rest_framework.permissions import IsAuthenticated

def Registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confpass = request.POST.get('confpass')

        if password == confpass:
            user = User.objects.create_user(username=username,
                                    email=email,
                                    first_name = fname,
                                    last_name= lname,
                                    )
            user.set_password(password)
            user.save()
            token = Token.objects.create(user=user)
            print(token.key)

            return redirect('login')
        
        else:
            return render(request, 'registration.html', {"message":"passwords do not match"})



        print(fname, lname, email, username, password, confpass)

    return render(request, 'registration.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            print(token, created)
            login(request, user)
            return redirect('khoj')  # Redirect to your search page
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        error_message = ''

    return render(request, 'login.html')

@permission_classes([IsAuthenticated])
def Khoj(request):
    if request.method == 'POST':
        input_values_str = request.POST.get('input_values')
        search_value = int(request.POST.get('search_value'))
        input_values = [int(val.strip()) for val in input_values_str.split(',')]

        sorted_input_values = sorted(input_values, reverse=True)
        input_history = ', '.join(str(val) for val in sorted_input_values)

        InputHistory.objects.create(user=request.user, input_values=input_history)
        
        #Implementing binary search for optimized searching
        result = binarySearch(sorted_input_values, search_value, 0, len(input_values)-1)

        return render(request, 'khoj.html', {'result': result})
    
    if not request.user.is_authenticated:
        print('user not authenticated')
        return redirect('login')
    
    return render(request, 'khoj.html')



