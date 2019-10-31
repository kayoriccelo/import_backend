from rest_framework.routers import DefaultRouter

from .viewsets import LogValidatorViewSet


router = DefaultRouter()
router.register(r'logs', LogValidatorViewSet)
