from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    date = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['date']
