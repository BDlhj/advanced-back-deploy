from django.urls import path, include
from todos import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.TodoViewSet, basename="todos")

app_name = 'todos'
urlpatterns = [
  path('', include(router.urls))
]
