from django.urls import include, path
from rest_framework import routers
from .views import BlogUserviewset

router=routers.DefaultRouter()
router.register('', BlogUserviewset)

urlpatterns=[

    path('', include(router.urls))
]
