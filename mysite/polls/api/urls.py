from django.conf.urls import include, url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'choice', views.ChoiceViewSet)
router.register(r'question', views.QuestionViewSet)

urlpatterns = [
    url('^', include(router.urls)),
]
