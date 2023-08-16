from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import InputHistory
from .serializers import TokenSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_input_values(request):
    start_datetime = request.query_params.get('start_datetime')
    end_datetime = request.query_params.get('end_datetime')
    
    user_id = request.user.id
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

@api_view(['POST'])
def obtain_token(request):
    # Your logic to obtain the token
    token, created = Token.objects.get_or_create(user=request.user)
    serializer = TokenSerializer(token)
    return Response(serializer.data)

