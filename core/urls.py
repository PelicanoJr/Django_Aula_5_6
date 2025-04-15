
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from filmes.views import filmes_view
from filmes.views import novo_filmes_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmes/', filmes_view, name='filmes_list'),
    path('novo_filme/', novo_filmes_view, name='novo_filmes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
