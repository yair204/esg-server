# manager_accounts/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Manager
from .serializers import ManagerSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.contrib.auth.hashers import make_password


@api_view(['POST'])
def manager_signup(request):
    if request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            manager = serializer.save(password=make_password(serializer.validated_data['password']))
            return Response({'id': manager.id}, status=status.HTTP_201_CREATED)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerDetail(APIView):
    def get(self, request, pk):
        try:
            user = Manager.objects.get(pk=pk)
            serializer = ManagerSerializer(user)
            return Response(serializer.data)
        except Manager.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                manager = Manager.objects.get(email=serializer.data['email'])
                if check_password(serializer.data['password'], manager.password):
                    return Response({'id': manager.id}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
            except Manager.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def login_page(request):
    return render(request, 'login.html')
