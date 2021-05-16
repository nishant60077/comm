from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import commissionSerializer
from .models import commission

# Create your views here.
@api_view(['GET'])
def api(request):
     api_urls={
         'List':'/comm-list/',
         'Detail view': '/comm-detail/<int:id>',
         'add': '/comm-add/',
         'Delete view': '/comm-detail/<int:id>',
     }
     
     return Response(api_urls);

@api_view(['GET'])
def showall(request):
    products = commission.objects.all()
    serializer = commissionSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewcomm(request, pk):
    products = commission.objects.get(commission_id=pk)
    serializer = commissionSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def addcomm(request):
    serializer = commissionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

    

@api_view(['GET'])
def deletecomm(request, pk):
    products = commission.objects.get(commission_id=pk)
    commission.delete()  

    return Response("Item Deleted Sucessfully")
