from rest_framework.routers import DefaultRouter

from .apps import BulletinConfig
from .views import BulletinViewSet

app_name = BulletinConfig.name

router = DefaultRouter()
router.register(r"bulletins", BulletinViewSet, basename="bulletins")  # /api/bulletin/bulletins/ - CRUD

urlpatterns = router.urls
