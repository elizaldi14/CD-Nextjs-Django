from rest_framework import routers
from .api import TaskViewSet

# Creo un router apartir de routers

router = routers.DefaultRouter()

# Cuando llamen a esta ruta va ejecutar TaskViewSet y le agregan el nombre de task

router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls