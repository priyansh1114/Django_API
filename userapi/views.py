from django.shortcuts import render
from rest_framework import viewsets
from userapi.models import Company
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
