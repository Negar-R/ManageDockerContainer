from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ManageAppView

router = DefaultRouter()
router.register("apps", ManageAppView)

urlpatterns = [path("", include(router.urls))]
