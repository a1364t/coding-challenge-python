from typing import Dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AppSerializer



@api_view(['POST'])
def app(request):
    serializer = AppSerializer(data=request.data)
    if serializer.is_valid():
        response = list()
        payloads = serializer.data['payload']
        for payload in payloads:
            drm = payload.get('drm', None)
            episodeCount = payload.get('episodeCount', None)
            if drm and episodeCount > 0:
                response.append({
                    "image": payload["image"]["showImage"],
                    "slug": payload["slug"],
                    "title": payload["title"]
                })
        return Response({"response": response}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Could not decode request: JSON parsing failed"}, 
        status=status.HTTP_400_BAD_REQUEST)