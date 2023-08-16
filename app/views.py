from django.shortcuts import render, redirect
from rest_framework.response import Response
from .algorithms import binarySearch
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import TokenSerializer
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
            return redirect('login')
        
        else:
            return render(request, 'registration.html', {"message":"passwords do not match"})

    return render(request, 'registration.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
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
        return redirect('login')
    
    return render(request, 'khoj.html', {'logout':True})

def user_logout(request):
    logout(request)
    return redirect('login')

@api_view(['POST'])
def gettoken(request):
    # Your logic to obtain the token
    token, created = Token.objects.get_or_create(user=request.user)
    serializer = TokenSerializer(token)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_input_values(request):
    start_datetime = request.query_params.get('start_datetime')
    end_datetime = request.query_params.get('end_datetime')
    user_id = request.query_params.get('user_id')
    
    input_history = InputHistory.objects.filter(user_id=user_id, timestamp__range=(start_datetime, end_datetime))
    
    payload = []
    for entry in input_history:
        payload.append({
            'timestamp': entry.timestamp,
            'input_values': entry.input_values,
        })
    
    response_data = {
        'status': 'success',
        'user_id': user_id,
        'payload': payload,
    }
    
    return Response(response_data)





