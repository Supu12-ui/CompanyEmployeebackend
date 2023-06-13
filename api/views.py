

from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializaers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class= CompanySerializer

    #companies/{companyId}/employee
    @action(detail=True,methods=['get'])
    def employee(self,request,pk=None):
       try:
           company=Company.objects.get(pk=pk)
           print("***********")
           print(company)
           emps=Employee.objects.filter(company=company)
           emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
           return Response(emps_serializer.data)
       except Exception as e:
           print(e)
           return Response({'message': 'Company does not exits'})
           

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer