from django.conf.urls import url, include
from rest_framework import routers
from ghtelectroniccenter import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'Customer', views.CustomerViewSet, base_name = "Customer")
router.register(r'Produk', views.ProdukViewSet, base_name = "ProdukPage")
router.register(r'Warna', views.WarnaViewSet)
router.register(r'Harga', views.HargaViewSet)
router.register(r'Cart', views.CartViewSet,base_name ="Cart")
router.register(r'ListCart', views.listCartViewSet)
router.register(r'Pesanan', views.PesananViewSet)
router.register(r'Bank', views.BankViewSet)
router.register(r'BuktiTransfer', views.BuktiTransferViewSet)
router.register(r'StatusPengiriman', views.StatusPengirimanViewSet)
router.register(r'Alamat', views.AlamatViewSet)
router.register(r'Stock', views.StockViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$',views.LoginViewSet.as_view()),
    #router.register(r'Stock', views.StockViewSet)
    #url(r'^Stock/', include('stock.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
