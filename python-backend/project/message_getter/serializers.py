import json

from rest_framework import serializers

from .models import UserIdentifierModel, MessageModel, AddressModel
from .model import classify as Ml

from loguru import logger


class UserIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIdentifierModel
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressModel
        fields = '__all__'


class GetMessageSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    author = UserIdentifierSerializer()

    class Meta:
        model = MessageModel
        fields = '__all__'


class UserField(serializers.DictField):
    def to_internal_value(self, data):
        obj = UserIdentifierModel.objects.get_or_create(
            id=data.get('id'),
            name=data.get('firstname'),
            second_name=data.get('lastname')
        )
        return data.get('id')

    def to_representation(self, value):
        return value


class AddressField(serializers.DictField):
    def to_internal_value(self, data):
        obj = AddressModel.objects.get_or_create(
            latitude=data.get('latitude'),
            longtitude=data.get('longtitude')
        )
        return AddressModel.objects.get(
            latitude=data.get('latitude'),
            longtitude=data.get('longtitude')
        )

    def to_representation(self, value):
        return value


class CreateMessageSerializer(serializers.ModelSerializer):
    author_id = UserField()
    addr = AddressField(required=False)
    date = serializers.DateTimeField(required=False)

    address = serializers.SlugRelatedField(slug_field="id", read_only=True)

    danger_level = serializers.ReadOnlyField()
    event_class = serializers.ReadOnlyField()

    def create(self, validated_data):
        ModelClass = self.Meta.model
        if 'addr' in validated_data:
            validated_data['address'] = validated_data.pop('addr')
        validated_data['event_class'] = Ml.classify(validated_data.get('text'))
        validated_data['danger_level'] = Ml.get_danger_level(validated_data.get('text'))
        instance = ModelClass._default_manager.create(**validated_data)
        return instance

    class Meta:
        model = MessageModel
        exclude = ['author', 'id']
