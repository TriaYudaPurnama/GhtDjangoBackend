from django.contrib import admin
from ghtelectroniccenter.models import Customer,Alamat,Produk,Warna,Harga,Stock,Cart,listCart,Pesanan,Bank,BuktiTransfer,StatusPengiriman

admin.site.register(Customer)
admin.site.register(Produk)
admin.site.register(Warna)
admin.site.register(Harga)
admin.site.register(Stock)
admin.site.register(Cart)
admin.site.register(listCart)
admin.site.register(Pesanan)
admin.site.register(Bank)
admin.site.register(BuktiTransfer)
admin.site.register(StatusPengiriman)
admin.site.register(Alamat)
# Register your models here.
