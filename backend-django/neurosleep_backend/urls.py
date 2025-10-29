from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from sleep.views import home  # import your home view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sleep.urls')),  # ✅ All your model endpoints live here
    path('', home, name='home'),        # render index.html here
]

