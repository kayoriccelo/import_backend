from rest_framework.routers import DefaultRouter

from .viewsets import SchemaValidatorViewSet


router = DefaultRouter()
router.register(r'schemas', SchemaValidatorViewSet)
