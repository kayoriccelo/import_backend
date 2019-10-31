from rest_framework import serializers

from .models import LogValidator


class LogValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogValidator
        fields = '__all__'