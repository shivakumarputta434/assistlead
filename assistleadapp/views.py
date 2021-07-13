from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("WELCOME TO HOME")




from rest_framework.views import APIView
from .serializers import CompanySerializer,Company_Serializer,Profile_Serializer
from  rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Testtable,Company,Profile

#testing api

class CompanyData(APIView):
    def get(self,request,*args,**kwargs):
        if kwargs.get('id'):
            id=kwargs.get('id')
            try:
                singleEmpdata=Testtable.objects.get(id=id)
                saved_data=CompanySerializer(singleEmpdata)
                return Response(saved_data.data)
            except:
                return Response({'msg':'data doesnot exist'})
        data=Testtable.objects.all()
        saved_data=CompanySerializer(data,many=True)
        return Response(saved_data.data)

    def post(self,request,*args,**kwargs):
        empdata=CompanySerializer(data=request.data)
        if empdata.is_valid():
            empdata.save()
            return Response(empdata.data,status=status.HTTP_201_CREATED)
        else:
            return Response(empdata.errors,status=status.HTTP_400_BAD_REQUEST)


#Production Company Api Function

class Company_Data(APIView):
    def get(self,request,*args,**kwargs):
        if kwargs.get('id'):
            id=kwargs.get('id')
            try:
                single_Company_data=Company.objects.get(id=id)
                saved_data=Company_Serializer(single_Company_data)
                return Response(saved_data.data)
            except:
                return Response({'msg':'data doesnot exist'})
        data=Company.objects.all()
        saved_data=Company_Serializer(data,many=True)
        return Response(saved_data.data)

    def post(self,request,*args,**kwargs):
        Company_data=Company_Serializer(data=request.data)
        if Company_data.is_valid():
            Company_data.save()
            return Response(Company_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(Company_data.errors,status=status.HTTP_400_BAD_REQUEST)



#Production Profile Api Function

class Profile_Data(APIView):
    def get(self,request,*args,**kwargs):
        if kwargs.get('id'):
            id=kwargs.get('id')
            try:
                single_profile_data=Profile.objects.get(id=id)
                saved_data=Profile_Serializer(single_profile_data)
                return Response(saved_data.data)
            except:
                return Response({'msg':'data doesnot exist'})
        data=Profile.objects.all()
        saved_data=Profile_Serializer(data,many=True)
        return Response(saved_data.data)

    def post(self,request,*args,**kwargs):
        Profile_data=Profile_Serializer(data=request.data)
        if Profile_data.is_valid():
            Profile_data.save()
            return Response(Profile_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(Profile_data.errors,status=status.HTTP_400_BAD_REQUEST)
