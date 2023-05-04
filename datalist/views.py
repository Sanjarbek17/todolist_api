from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import Usertask

@api_view(['post'])
def get_user(request):
    # getting date from request username and password
    username = request.data.get('username', 'guest')
    password = request.data.get('password', '17')
    user     = User.objects.create_user(username=username, password=password)
    # if user created returns created response
    if user:
        return Response({'status':f"user {user} created"}, status=status.HTTP_200_OK)
    return Response({'status': 'User doesn\'t exists'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['get', 'post'])
def get_data(request):
    # if user created returen created response

    obj = Usertask.objects.all()
    lst = []
    # turning complex date to simple data
    for i in obj:
        dct ={}
        dct['name'] = i.name
        dct['isDone'] = i.isDone
        lst.append(dct)
    return Response(lst, status=status.HTTP_200_OK)

@api_view(['post'])
def add_data(request):
    # getting date from request username and password
    name = request.data.get('name')

    if name:
        Usertask.objects.create(name=name)
        return Response({'status':'created'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status':'date is emptpy'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def delete_data(request):
    # getting date from request username and password
    name = request.data.get('name')

    if name:
        data = Usertask.objects.filter(name=name)
        if data.exists():
            data = data.first()
            data.delete()
            return Response({'status':"user deleted"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'status':f'{name} doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'status':'date is emptpy'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def update_data(request):
    name = request.data.get('name')
    isDone = request.data.get('isDone')

    if name:
        data = Usertask.objects.filter(name=name)
        if data.exists():
            data = data.first()
            data.isDone = isDone
            data.save()
            return Response({'status':'updated'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'status':f'{name} doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'status':'date is emptpy'}, status=status.HTTP_204_NO_CONTENT)
