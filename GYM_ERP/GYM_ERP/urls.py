"""
URL configuration for GMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include  # Import the include function

from api import urls as api_urls
# Import the urls.py module from the API app
from attendance import urls as att_urls
from gymfrontend import urls as gymfrontendurl
from developerfrontend import urls as developerfrontendurl

# Import necessary modules
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Define the schema view
schema_view = get_schema_view(
    openapi.Info(
        title="API DOUMENTATION PAGE",
        default_version="v1",
        description="Description of your API",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,  # Set to True to allow access without authentication
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]
)



urlpatterns = [
    # Other URL patterns
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path("", views.login),

    path("api/", include(api_urls)),
    path("attendence/", include(att_urls)),
    path("gymfrontend/", include(gymfrontendurl)),
    path("developerfrontend/", include(developerfrontendurl)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# Additional configurations
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

