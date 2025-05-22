from rest_framework.routers import DefaultRouter

from .views import BulletinViewSet

# /api/bulletin/bulletins/ - обычный CRUD
# /api/bulletin/bulletins/ads/ — отдельный эндпоинт с 4 объектами на страницу
router = DefaultRouter()
router.register(r"bulletin", BulletinViewSet, basename="bulletin")

urlpatterns = router.urls
