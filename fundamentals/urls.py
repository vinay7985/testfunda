from django.urls import path,include
from fundamentals.views import SnippetViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'fundamentals',SnippetViewSet)
urlpatterns = [
    path('', include(router.urls)),
]