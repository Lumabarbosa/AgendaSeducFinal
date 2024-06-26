from django.contrib import admin
from django.urls import path, include # adicionar include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", include("usuarios.urls")),
    path('usuarios/', include('django.contrib.auth.urls')), # Adicionar esta linha
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Adicionar Isto
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adicionar Isto