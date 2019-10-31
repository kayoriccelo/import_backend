from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import SchemaValidator
from .serializers import SchemaValidatorSerializer


class SchemaValidatorViewSet(viewsets.ModelViewSet):
    queryset = SchemaValidator.objects.all()
    serializer_class = SchemaValidatorSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
