from django.conf.urls import url, include
from rest_framework import routers
from ghtelectroniccenter import views

router = routers.DefaultRouter()
router.register(r'Customer', views.CustomerViewSet, base_name = "Customer")
router.register(r'Produk', views.ProdukViewSet, base_name = "ProdukPage")
router.register(r'Warna', views.WarnaViewSet)
router.register(r'Harga', views.HargaViewSet)
router.register(r'Stock', views.StockViewSet)
router.register(r'Cart', views.CartViewSet)
router.register(r'ListCart', views.listCartViewSet)
router.register(r'Pesanan', views.PesananViewSet)
router.register(r'Bank', views.BankViewSet)
router.register(r'BuktiTransfer', views.BuktiTransferViewSet)
router.register(r'StatusPengiriman', views.StatusPengirimanViewSet)
router.register(r'Alamat', views.AlamatViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
