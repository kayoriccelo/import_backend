from rest_framework import serializers

from .models import SchemaValidator


class SchemaValidatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchemaValidator
        fields = '__all__'
