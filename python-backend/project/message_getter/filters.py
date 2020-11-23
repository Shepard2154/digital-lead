from django_filters import rest_framework as filters

from .models import MessageModel


class MessageFilter(filters.FilterSet):
    author = filters.NumberFilter(field_name='author')
    date = filters.IsoDateTimeFromToRangeFilter(field_name='date')
    event = filters.CharFilter(field_name='event_class')
    danger = filters.NumberFilter(field_name='danger_level')
    address = filters.CharFilter(field_name='address')

    class Meta:
        model = MessageModel
        exclude = ['text']