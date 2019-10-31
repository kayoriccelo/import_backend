from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.log.urls import router as log_routers


router = DefaultRouter()

urlpatterns = (
    router.urls + 

    log_routers.urls
)
