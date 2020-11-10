from django.urls import path, include

from produtos.views import CamisaViewSet, ChuteiraViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'camisas', CamisaViewSet)
router.register(r'chuteiras', ChuteiraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]