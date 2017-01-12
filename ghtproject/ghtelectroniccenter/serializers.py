from rest_framework import serializers
from ghtelectroniccenter.models import Customer,Produk,Warna,Harga,Stock,Cart,listCart,Pesanan,Bank,BuktiTransfer,StatusPengiriman

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class WarnaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warna
        fields = '__all__'

class HargaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Harga
        fields = '__all__'

class ProdukSerializer(serializers.HyperlinkedModelSerializer):
    harga = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Produk
        fields = '__all__'
        

class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class listCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = listCart
        fields = '__all__'
class PesananSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Pesanan
        fields = '__all__'
class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BuktiTransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuktiTransfer
        fields = '__all__'

class StatusPengirimanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusPengiriman
        fields = '__all__'
