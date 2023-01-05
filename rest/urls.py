from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.PostViewSet)
router.register('tags', views.TagViewSet)

urlpatterns = router.urls