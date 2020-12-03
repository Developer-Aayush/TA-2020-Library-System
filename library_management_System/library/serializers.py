from rest_framework import serializers
from .models import allInformation


class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = allInformation
        fields = '__all__'
