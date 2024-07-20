from django.shortcuts import render
from .models import Empresa
from .serializers import EmpresaSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class EmpresaView(APIView):
    def get(self, request):
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa,many=True)
        data = {
            'data' : serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)
    
    def post(self, request,*args, **kwargs):
        data= {
            'empresa_id' : request.data.get('empresa_id'),
            'nro_ruc' : request.data.get('nro_ruc'),
            'razon_social' : request.data.get('razon_social'),
            'direccion' : request.data.get('direccion'),
            'acronimo' : request.data.get('acronimo')
        }
        serializer = EmpresaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

