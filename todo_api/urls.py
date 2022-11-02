from .views import *
from rest_framework import routers
from django.urls import path
router = routers.DefaultRouter()

router.register('api/todos',TodoViewSet,'todos')
urlpatterns = [
    path("api/ftodos/<str:date>",TodoAPI.as_view()),
    path('api/chart',ChartData.as_view()),
    path('api/flutterchart',FlutterChartData.as_view())
]
urlpatterns += router.urls