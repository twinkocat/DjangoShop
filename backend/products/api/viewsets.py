from rest_framework.viewsets import ReadOnlyModelViewSet

from products.api.serializers import ProductsListSerializer
from products.models.product import Product
from products.paginations import StandardResultsSetPagination


class ProductsListViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all().select_related('type', 'brand', 'discount').prefetch_related('model', 'photos')
    serializer_class = ProductsListSerializer
    pagination_class = StandardResultsSetPagination

