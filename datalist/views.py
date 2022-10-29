from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usertask

@api_view(['get'])
def get_data(request):
    obj = Usertask.objects.all()
    lst = []
    for i in obj:
        dct ={}
        dct['name'] = i.name
        dct['isDone'] = i.isDone
        lst.append(dct)
    
    return Response(lst)

@api_view(['post'])
def add_data(request):
    name = request.data.get('name')
    if name and not Usertask.objects.filter(name=name).exists():
        Usertask.objects.create(name=name)
        return Response({'status':'created'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'status':'data is empty or user exists'}, status=status.HTTP_417_EXPECTATION_FAILED)

@api_view(['POST'])
def delete_data(request):
    name = request.data.get('name')
    if name:
        user = Usertask.objects.get(name=name)
        user.delete()
        return Response({'status':"user deleted"})
    return Response({'status': f'{name} doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_data(request):
    name = request.data.get('name')
    isDone = request.data.get('isDone')
    if name:
        user = Usertask.objects.get(name=name)
        user.isDone = isDone
        user.save()
        return Response({'status':'updated'}, status=status.HTTP_202_ACCEPTED)
    return Response({'status':'data is empty'}, status=status.HTTP_417_EXPECTATION_FAILED)
