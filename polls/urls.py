from rest_framework.routers import DefaultRouter
from .views import PollViewSet
from django.urls import path,include

router = DefaultRouter()
router.register(r'poll',PollViewSet,basename='poll')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls))
]