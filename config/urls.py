from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
import os
from django.views.static import serve as static_serve


def react_assets(request, path):
    # react build assets-lerini (js, css) gonderir
    kok = os.path.join(settings.REACT_BUILD_DIR, 'assets')
    return static_serve(request, path, document_root=kok)


def react_statik_fayllar(request, path):
    # kok qovluqdaki statik fayllar (favicon, svg ve s.)
    return static_serve(request, path, document_root=settings.REACT_BUILD_DIR)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # react build assets (JS, CSS fayllari)
    re_path(r'^assets/(?P<path>.*)$', react_assets),
    # kok statik fayllar (meselen favicon.ico)
    re_path(r'^(?P<path>.*\.\w+)$', react_statik_fayllar),
    # qalan butun url-ler ucun react SPA index.html gonderilir
    re_path(r'^(?!admin|api).*$', TemplateView.as_view(template_name='index.html')),
]
