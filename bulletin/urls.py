from rest_framework.routers import DefaultRouter

from .apps import BulletinConfig
from .views import BulletinViewSet

app_name = BulletinConfig.name

# /api/bulletin/bulletins/ - обычный CRUD
# /api/bulletin/bulletins/page/ — отдельный эндпоинт с 4 объектами на страницу
router = DefaultRouter()
router.register(r"bulletins", BulletinViewSet, basename="bulletins")

urlpatterns = router.urls
