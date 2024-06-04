from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Manager
from .serializers import ManagerSerializer

@api_view(['POST'])
def manager_signup(request):
    if request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            manager = serializer.save()
            return Response({'id': manager.id}, status=status.HTTP_201_CREATED)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
