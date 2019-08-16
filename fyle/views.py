
from django.shortcuts import render, get_object_or_404
# Create your views here.
from rest_framework.views import APIView
from fyle.models import bank_details,branches,banks
from rest_framework.permissions import IsAuthenticated


class ALL(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request) :
        bankdetails = bank_details.objects.all()
        return render(request, 'TestFyle/first.html', {'details': bankdetails})

class ById(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,ifscCode) :
        details = bank_details.objects.filter(ifsc= ifscCode)
        return render(request, 'TestFyle/first.html', {'details': details})

class ByBandC(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,bname,City) :
        details = bank_details.objects.filter(bank_name = bname,city=City)
        return render(request, 'TestFyle/first.html', {'details': details})
