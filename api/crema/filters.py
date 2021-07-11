import django_filters
from .models import Products, Reviews

class ProductFilter(django_filters.FilterSet):
    min_score = django_filters.NumberFilter(field_name="representative_score", lookup_expr="gte")
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr="lte")

    class Meta:
        model = Products
        fields = [
            'product_status', 
            'created_at',
            'code',
            "min_score",
            "start_date",
            "end_date",
        ]

# model filter?
class ReviewFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(field_name="message", lookup_expr="contains")
    min_score = django_filters.NumberFilter(field_name="score_final", lookup_expr="gte")
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr="gte")
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr="lte")

    class Meta:
        model = Reviews
        fields = [
            'created_at', 
            'product_id', 
            'product_code', 
            'code',
            'keyword',
            "min_score",
            "start_date",
            "end_date",
        ]