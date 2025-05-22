from rest_framework.routers import DefaultRouter

from .apps import BulletinConfig
from .views import BulletinViewSet, ReviewViewSet

app_name = BulletinConfig.name

router = DefaultRouter()
router.register(r"bulletins", BulletinViewSet, basename="bulletins")  # /api/bulletin/bulletins/ - CRUD
router.register(r"reviews", ReviewViewSet, basename="reviews")  # /api/bulletin/reviews/ - CRUD

urlpatterns = router.urls
