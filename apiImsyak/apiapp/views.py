from django.shortcuts import render
from . models import Jadwal
from apiapp.serializers import JadwalSerializer
from rest_framework import serializers
from django.http import JsonResponse

def getJadwal(request):
    if request.method == 'GET':
        jadwal = Jadwal.objects.all()
        serializer = JadwalSerializer(jadwal, many=True)

        return JsonResponse(serializer.data, safe=False)