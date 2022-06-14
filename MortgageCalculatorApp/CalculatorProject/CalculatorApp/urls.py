from django.urls import path, include

from rest_framework import routers

from .views import *


router = routers.SimpleRouter()

router.register(r'about', BanksViewSet)

urlpatterns = [
        path('banks/', include(router.urls)),
        path('calculator/', calculate_value),

]
