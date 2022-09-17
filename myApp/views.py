from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['POST'])
def app(request):
    try:
        image = request.data["image"]
        slug = request.data["slug"]
        title = request.data["title"]
    except:
        return Response({"error": "Could not decode request: JSON parsing failed"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"response": 
            [
            {"image", image, 
            "slug", slug, 
            "title", title}
            ]
        }, status=status.HTTP_200_OK)