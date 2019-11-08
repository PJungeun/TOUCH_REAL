from django.contrib import admin
from django.urls import path
import count.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', count.views.main, name="main"),
    path('count/',count.views.count, name ="count"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
