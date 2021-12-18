from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import tache
from . serializers import tacheSerializers


class tacheList(APIView):
    def get(self,request):
        tache1=tache.objects.all()
        serializer=tacheSerializers(tache1,many=True)
        return Response(serializer.data)


    def post(self):
        pass


