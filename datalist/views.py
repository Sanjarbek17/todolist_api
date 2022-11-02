from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usertask, Username

@api_view(['get', 'post'])
def get_data(request):
    # getting date from request username and password
    username = request.data.get('username', 'guest')
    password = request.data.get('password', '17')
    user, created = Username.objects.get_or_create(name=username, password=password)
    # if user created returen created response
    if created:
        return Response({'status': 'created'})

    obj = user.task.all()
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
    username = request.data.get('username', 'guest')
    password = request.data.get('password', '17')
    # getting user
    user = Username.objects.filter(name=username, password=password)
    if user.exists():
        if name:
            user.first().task.create(name=name)
            return Response({'status':'created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'date is emptpy'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'status':'invalid user'}, status=status.HTTP_417_EXPECTATION_FAILED)

@api_view(['POST'])
def delete_data(request):
    # getting date from request username and password
    name = request.data.get('name')
    username = request.data.get('username', 'guest')
    password = request.data.get('password', '17')

    user = Username.objects.filter(name=username, password=password)
    if user.exists():
        if name:
            data = user.first().task.objects.filter(name=name)
            if data.exists():
                data.delete()
                return Response({'status':"user deleted"}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'status':f'{name} doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'status':'date is emptpy'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'status': 'invalid user'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_data(request):
    name = request.data.get('name')
    username = request.data.get('username', 'guest')
    password = request.data.get('password', '17')
    isDone = request.data.get('isDone')

    user = Username.objects.filter(name=username, password=password)
    if user.exists():
        if name:
            data = user.first().task.objects.filter(name=name)
            if data.exists():
                data.isDone = isDone
                data.save()
                return Response({'status':'updated'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'status':f'{name} doesn\'t exist'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'status':'date is emptpy'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'status':'invalid user'}, status=status.HTTP_417_EXPECTATION_FAILED)
