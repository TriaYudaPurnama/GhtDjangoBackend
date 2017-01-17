import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Customer(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length = 50)
    def __str__(self):
        return self.email

class Produk(models.Model):
    kode_produk = models.CharField(default=0,max_length=8,primary_key=True)
    nama_produk = models.CharField(max_length=100)
    jenis_produk = models.CharField(max_length=20)
    spesifikasi1 = models.CharField(max_length=100)
    spesifikasi2 = models.CharField(max_length=100)
    spesifikasi3 = models.CharField(max_length=100)
    spesifikasi4 = models.CharField(max_length=100)
    spesifikasi5 = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=200)
    def __str__(self):
        return self.nama_produk


class Warna(models.Model):
    kode_warna = models.CharField(default=0,max_length=7,primary_key=True)
    nama_warna = models.CharField(max_length = 15)
    def __str__(self):
        return self.nama_warna


class Harga(models.Model):
    tanggal_harga = models.DateTimeField(default=datetime.datetime.now,primary_key=True)
    kode_produk = models.ForeignKey(Produk, on_delete = models.CASCADE,related_name = 'harga' )
    harga = models.IntegerField(default=0)
    keterangan = models.CharField(max_length=200)
    def __str__(self):
        return 'Tanggal : %s,Harga :  %s' % (self.tanggal_harga, self.harga)

class Stock(models.Model):
    kode_produk = models.ForeignKey(Produk,on_delete = models.CASCADE,related_name = 'stock')
    kode_warna = models.ForeignKey(Warna, on_delete = models.CASCADE)
    jumlah = models.IntegerField(default=0)
    gambar =  models.ImageField(upload_to = "image/produk")
    def __str__(self):
        return 'Warna : %s,Jumlah :  %s,Gambar :  %s' % (self.kode_warna, self.jumlah, self.gambar )

class Cart(models.Model):
    waktu_cart =  models.DateTimeField(default=datetime.datetime.now,primary_key=True)
    id_customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    total_pembelian = models.IntegerField(default=0)


class listCart(models.Model):
    waktu_cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='barang_pesanan')
    id_produk = models.ForeignKey(Produk, on_delete = models.CASCADE)
    jumlah_pesan = models.IntegerField(default=0)
    total_harga_peritem = models.IntegerField(default=0)
    def __str__(self):
        return 'Id Produk : %s,Jumlah : %s,Total :  %s' % (self.id_produk, self.jumlah_pesan,self.total_harga_peritem)


class Pesanan(models.Model):
    kode_pesanan = models.CharField(max_length=15,primary_key = True)
    id_customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    waktu_cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    nama_pemesan = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=100)
    tanggal_pesanan = models.DateTimeField(default=datetime.datetime.now)

class Alamat(models.Model):
    id_customer = models.ForeignKey(Customer, on_delete = models.CASCADE,related_name = 'alamat')
    provinsi = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    jalan = models.CharField(max_length=100)
    kode_pos = models.CharField(max_length=5)
    def __str__(self):
        return '%s: %s: %s: %s' % (self.provinsi, self.kota,self.jalan,self.kode_pos)

class Bank(models.Model):
    kd_bank = models.CharField(max_length=5,primary_key=True)
    nama_bank = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_bank

class BuktiTransfer(models.Model):
    kode_bukti = models.CharField(max_length=10,primary_key=True)
    kd_pesanan = models.ForeignKey(Pesanan, on_delete = models.CASCADE)
    rekening_pengirim = models.CharField(max_length=50)
    bank_pengirim = models.CharField(max_length=50)
    waktu_transfer = models.DateTimeField(default=datetime.datetime.now)
    rekening_penerima = models.CharField(max_length=50)
    bank_penerima  = models.ForeignKey(Bank, on_delete = models.CASCADE)
    gambar_bukti = models.ImageField(upload_to = "image/bukti")


class StatusPengiriman(models.Model):
    kd_pesanan = models.ForeignKey(Pesanan, on_delete = models.CASCADE)
    bukti_transfer = models.ForeignKey(BuktiTransfer, on_delete = models.CASCADE)
    status =  models.CharField(max_length=50)
    ongkir = models.IntegerField(default = 0)
    keterangan = models.CharField(max_length=200)
