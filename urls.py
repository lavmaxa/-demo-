from django.contrib import admin
from django.views.static import serve
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('',include('main.urls')),

    path('',include ('rating.urls')),
    path('',include ('timesheet.urls')),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

