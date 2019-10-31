from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import LogValidator
from .serializers import LogValidatorSerializer


class LogValidatorViewSet(viewsets.ModelViewSet):
    queryset = LogValidator.objects.all()
    serializer_class = LogValidatorSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
