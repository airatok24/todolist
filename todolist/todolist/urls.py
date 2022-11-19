from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/login/', include('rest-framework.urls', namespace='rest-framework')),
    path('core/', include('core.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]
