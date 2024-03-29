from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
router.register(r'country', views.CountryViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
