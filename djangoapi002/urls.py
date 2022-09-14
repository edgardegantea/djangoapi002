from django.urls import include, path
from rest_framework import routers
from api import views as vistas
from django.contrib import admin
from employee import views as ve

router = routers.DefaultRouter()
router.register(r'users', vistas.UserViewSet)
router.register('empleados', ve.Employee)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]
