from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MusicPreferenceViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'preferences', MusicPreferenceViewSet)

urlpatterns = router.urls
