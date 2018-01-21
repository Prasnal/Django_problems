from django.shortcuts import render
from rest_framework.response import Response
from .models import Country, Company, Product,Country_Products
from rest_framework import viewsets
from .serializers import CountrySerializer, CompanySerializer, ProductSerializer
from rest_framework.decorators import detail_route

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        company = self.request.query_params.get('company', None)

        if company is not None:
            queryset = queryset.filter(company_id=company)

        return queryset

    @detail_route()
    def countries(self, request, pk=None):
        cntr_prodc = Country_Products.objects.all()
        country_products=cntr_prodc.filter(product_id=pk)

        countries=[]
        for i in country_products:
            countries.append(i.country_id)

        json=CountrySerializer(countries,context={'request':request},many=True)
        return Response(json.data)


