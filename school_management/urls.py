from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from school.views import redirect_to_school

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include("school.urls")),
    path('', redirect_to_school),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
