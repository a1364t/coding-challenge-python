from typing import Dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppSerializer



@api_view(['POST'])
def app(request):
    ser = AppSerializer(data=request.data)
    results = {}
    if ser.is_valid():
        payload = list(ser.data['payload'])
        for i in payload:
            results.setdefault(i)
            return Response({"response": results}, status=status.HTTP_200_OK)
    else:
        return Response(ser.errors, #{"error": "Could not decode request: JSON parsing failed"}, 
        status=status.HTTP_400_BAD_REQUEST)