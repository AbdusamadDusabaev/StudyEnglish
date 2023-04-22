from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("authentication/", include("authentication.urls")),
    path("personal-area/", include("personal_area.urls")),
]

urlpatterns.extend(static(STATIC_URL, document_root=STATIC_ROOT))
urlpatterns.extend(static(MEDIA_URL, document_root=MEDIA_ROOT))
