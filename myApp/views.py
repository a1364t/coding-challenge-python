from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppSerializer



@api_view(['POST'])
def app(request):
    ser = AppSerializer(data=request.data)

    if ser.is_valid():
        payload = ser.data['payload']
        for i in payload:
            #if i.drm:
            return Response({"response": [i]}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Could not decode request: JSON parsing failed"}, 
        status=status.HTTP_400_BAD_REQUEST)