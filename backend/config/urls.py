from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from products.api.viewsets import ProductsListViewSet

router = DefaultRouter()
router.register(r'products', ProductsListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
