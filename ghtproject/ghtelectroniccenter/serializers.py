from rest_framework import serializers
from ghtelectroniccenter.models import Customer,Alamat,Produk,Warna,Harga,Stock,Cart,listCart,Pesanan,Bank,BuktiTransfer,StatusPengiriman

class AlamatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alamat
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    alamat = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ('email','password','alamat')


class WarnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warna
        fields = '__all__'


class HargaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Harga
        fields = '__all__'

class ProdukSerializer(serializers.ModelSerializer):
    harga = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Produk
        fields = ('kode_produk','nama_produk','jenis_produk','spesifikasi1','spesifikasi2','spesifikasi3','spesifikasi4','spesifikasi5','harga','deskripsi')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class listCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = listCart
        fields = '__all__'
class PesananSerializer(serializers.ModelSerializer):
    class Meta :
        model = Pesanan
        fields = '__all__'
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BuktiTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuktiTransfer
        fields = '__all__'

class StatusPengirimanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPengiriman
        fields = '__all__'
