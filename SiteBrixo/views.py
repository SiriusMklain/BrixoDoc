from rest_framework import generics, viewsets
from rest_framework.views import APIView
from . import serializers
from .models import Suppliers, Articles, ArticleOem, VehicleBrands, VehicleModels, Vehicles, DisplayBra


class DisplayBraList(generics.ListAPIView):
    queryset = DisplayBra.objects.all()
    serializer_class = serializers.DisplayBraSerializer


class DisplayBraDetail(generics.RetrieveAPIView):
    queryset = DisplayBra.objects.all()
    serializer_class = serializers.DisplayBraSerializer


class SuppliersList(generics.ListAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = serializers.SuppliersSerializer


class SuppliersDetail(generics.RetrieveAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = serializers.SuppliersSerializer


class ArticlesList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="FIT").values('ArticleNumber', 'ArticleOem__NormalizerOemNumber')[:3] #ArticleOem__NormalizerOemNumber=
    serializer_class = serializers.ArticlesSerializer


class ArticlesDetail(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticlesSerializer


class ArticlesOemList(generics.ListAPIView):
    queryset = ArticleOem.objects.all()
    serializer_class = serializers.ArticleOemSerializer


class ArticlesOemDetail(generics.RetrieveAPIView):
    queryset = ArticleOem.objects.all()
    serializer_class = serializers.ArticleOemSerializer


class VehicleBrandList(generics.ListAPIView):
    queryset = VehicleBrands.objects.all()
    serializer_class = serializers.VehicleBrandSerializer


class VehicleBrandDetail(generics.RetrieveAPIView):
    queryset = VehicleBrands.objects.all()
    serializer_class = serializers.VehicleBrandSerializer


class VehicleModelList(generics.ListAPIView):
    queryset = VehicleModels.objects.all()
    serializer_class = serializers.VehicleModelSerializer


class BrandModelList(viewsets.ModelViewSet):
    queryset = VehicleBrands.objects.all()
    serializer_class = serializers.VehicleBrandSerializer


class VehicleModelDetail(generics.RetrieveAPIView):
    queryset = VehicleModels.objects.all()
    serializer_class = serializers.VehicleModelSerializer


class VehicleList(generics.ListAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = serializers.VehicleSerializer


class VehicleDetail(generics.RetrieveAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = serializers.VehicleSerializer


#Сортировка по производителям запчастей
class FitList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="FIT")[:3]
    serializer_class = serializers.ArticlesSerializer


class BrixoList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="BRIXO")[:3]
    serializer_class = serializers.ArticlesSerializer


class SureList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="SURE FILTER")[:3]
    serializer_class = serializers.ArticlesSerializer


class NiBKList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="NiBK")[:3]
    serializer_class = serializers.ArticlesSerializer


class JSList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="JS ASAKASHI")[:3]
    serializer_class = serializers.ArticlesSerializer


class SacuraList(generics.ListAPIView):
    queryset = Articles.objects.filter(SupplierId__Name="SAKURA Automotive")[:3]
    serializer_class = serializers.ArticlesSerializer


#Связанные артикулы с авто


class ArtInCar(generics.ListAPIView):
    pass