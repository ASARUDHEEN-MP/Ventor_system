import django_filters
from .models import PurchaseOrder

class PurchaseOrderFilter(django_filters.FilterSet):
    vendor = django_filters.NumberFilter(field_name='vendor', lookup_expr='exact')

    class Meta:
        model = PurchaseOrder
        fields = ['vendor']
