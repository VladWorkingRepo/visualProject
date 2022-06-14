from rest_framework import serializers
from .models import Banks


class DataClientSerializeModel(serializers.Serializer):
    total_cost = serializers.IntegerField()
    initial_fee = serializers.IntegerField()
    time = serializers.IntegerField()


class BanksSerializeModel(serializers.ModelSerializer):

    class Meta:
        model = Banks
        fields = '__all__'

