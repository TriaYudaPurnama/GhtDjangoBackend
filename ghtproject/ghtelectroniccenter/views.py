from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Customer,Produk,Warna,Harga,Stock,Cart,listCart,Pesanan,Bank,BuktiTransfer,StatusPengiriman
from .serializers import CustomerSerializer,ProdukSerializer,WarnaSerializer,HargaSerializer,StockSerializer,CartSerializer,listCartSerializer,PesananSerializer,BankSerializer,BuktiTransferSerializer,StatusPengirimanSerializer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
class HargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Harga.objects.all()
    serializer_class = HargaSerializer

class ProdukViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    
    serializer_class = ProdukSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Produk.objects.all()
        jenisProduk = self.request.query_params.get('jenis_produk',None)
        if jenisProduk is not None:
            queryset = queryset.filter(jenis_produk=jenisProduk)
        kodeProduk = self.request.query_params.get('kode_produk',None)
        if kodeProduk is not None:
            queryset = queryset.filter(kode_produk=kodeProduk)
        return queryset
        

class WarnaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Warna.objects.all()
    serializer_class = WarnaSerializer

class HargaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Harga.objects.all()
    serializer_class = HargaSerializer
class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class listCartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = listCart.objects.all()
    serializer_class = listCartSerializer

class PesananViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BuktiTransferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BuktiTransfer.objects.all()
    serializer_class = BuktiTransferSerializer

class StatusPengirimanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = StatusPengiriman.objects.all()
    serializer_class = StatusPengirimanSerializer
