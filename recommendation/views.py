from datetime import datetime, timezone
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.response import Response
from .models import Nutrition, Vaccinations, RecommendedNutritionAndVaccination
from .serializers import  RecommenedNutritionAndVaccinationSerializer,VaccinationsSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
def get_vaccines(request):
    vaccines=Vaccinations.objects.all()
    serializer=VaccinationsSerializer(vaccines,many=True)
    return Response({"data":serializer.data,"msg":"found vaccines","success":True},status=status.HTTP_200_OK)



    


