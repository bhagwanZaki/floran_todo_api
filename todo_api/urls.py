from .views import *
from rest_framework import routers
from django.urls import path
router = routers.DefaultRouter()

router.register('api/todos',TodoViewSet,'todos')
router.register('api/test',test,'test')
urlpatterns = [
    path('api/chart',ChartData.as_view()),
    path('api/flutterchart',FlutterChartData.as_view())
]
urlpatterns += router.urls