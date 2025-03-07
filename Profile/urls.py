from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import handler404, handler400, handler500
from main.views import custom_404_view, custom_400_view, custom_500_view

handler404 = custom_404_view
handler400 = custom_400_view
handler500 = custom_500_view

urlpatterns = [
    path('admin/markanthony', admin.site.urls),
    path('', include('main.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
