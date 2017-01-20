from rest_framework import serializers
from ghtelectroniccenter.models import Customer,Alamat,Produk,Warna,Harga,Stock,Cart,listCart,Pesanan,Bank,BuktiTransfer,StatusPengiriman
from django.db.models import Max

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
        fields = ('tanggal_harga','harga')


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('kode_produk','kode_warna','jumlah','gambar')

class ProdukSerializer(serializers.ModelSerializer):
    #harga = serializers.StringRelatedField(many=True, read_only=True)
    harga = serializers.SerializerMethodField('get_latest_harga')

    stock = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Produk
        fields = ('kode_produk','nama_produk','jenis_produk','spesifikasi1','spesifikasi2','spesifikasi3','spesifikasi4','spesifikasi5','harga','deskripsi','stock')
    def get_latest_harga(self,kode_produk):
        #print(kode_produk.kode_produk)
        #harga =
        #serializer = HargaSerializer(instance=harga, many=True)
        return Produk.objects.values('harga__kode_produk').annotate(latest_date=Max('harga__tanggal_harga')).filter(kode_produk = kode_produk.kode_produk).annotate(latest_harga= Max('harga__harga'))

class listCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = listCart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    barang_pesanan = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ('waktu_cart','id_customer','barang_pesanan','total_pembelian')


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
