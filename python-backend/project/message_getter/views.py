from datetime import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView
)

from .models import UserIdentifierModel, MessageModel, AddressModel
from .serializers import UserIdentifierSerializer, GetMessageSerializer, CreateMessageSerializer, AddressSerializer
from .filters import MessageFilter
from .model.classify import get_file
from . import services

from loguru import logger


class UpdateAddressView(UpdateAPIView):
    serializer_class = AddressSerializer
    queryset = AddressModel.objects.all()

# Upload File and check it
class UploadPhotoView(APIView):
    def post(self, request, format=None):
        r = get_file(request.FILES['file'])
        return Response(r, status=status.HTTP_200_OK)

# User methods
class CreateUserView(CreateAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

class GetUserView(RetrieveAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

class DeleteUserView(DestroyAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

class GetAllUsersView(ListAPIView):
    queryset = UserIdentifierModel.objects.all()
    serializer_class = UserIdentifierSerializer

# Message methods
class CreateMessageView(CreateAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = CreateMessageSerializer

class GetMessageView(RetrieveAPIView):
    queryset = MessageModel.objects.all().order_by('-date')
    serializer_class = GetMessageSerializer

class DeleteMessageView(DestroyAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = GetMessageSerializer

class GetAllMessagesView(ListAPIView):
    queryset = MessageModel.objects.all()
    serializer_class = GetMessageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MessageFilter

    # добавляем время запроса в выдачу, чтобы делать последующие запросы, начиная с заданного момента
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'data': serializer.data,
            'timestamp': datetime.now()
        }
        return Response(response)

# получение данных для графиков
class GetHourView(APIView):
    def post(self, request, format=None):
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')
        hour = request.data.get('hour')
        danger = request.data.get('danger')
        if not danger: danger = ''
        event = request.data.get('event')
        if not event: event = ''
        return Response(data=services.get_hour_data(
            month = month, 
            day = day, 
            year = year, 
            hour = hour, 
            danger = danger,
            event = event
        ), status=status.HTTP_200_OK)

class GetDayView(APIView):
    def post(self, request, format=None):
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')
        danger = request.data.get('danger')
        if not danger: danger = ''
        event = request.data.get('event')
        if not event: event = ''
        return Response(data=services.get_day_data(
            month = month, 
            day = day, 
            year = year, 
            danger = danger,
            event = event
        ), status=status.HTTP_200_OK)

class GetMonthView(APIView):
    def post(self, request, format=None):
        month = request.data.get('month')
        year = request.data.get('year')
        danger = request.data.get('danger')
        if not danger: danger = ''
        event = request.data.get('event')
        if not event: event = ''
        return Response(data=services.get_month_data(
            month = month,
            year = year, 
            danger = danger,
            event = event
        ), status=status.HTTP_200_OK)

class GetYearView(APIView):
    def post(self, request, format=None):
        year = request.data.get('year')
        danger = request.data.get('danger')
        if not danger: danger = ''
        event = request.data.get('event')
        if not event: event = ''
        return Response(data=services.get_year_data(
            year = year, 
            danger = danger,
            event = event
        ), status=status.HTTP_200_OK)