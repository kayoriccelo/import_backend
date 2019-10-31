from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from apps.log.urls import router as log_routers
from apps.schema.urls import router as schema_routers


router = DefaultRouter()

urlpatterns = (
    router.urls + 

    schema_routers.urls +
    log_routers.urls
)
