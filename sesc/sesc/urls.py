from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from main import views as main_views
from forms import views as forms_views


urlpatterns = [
    path('lk/', admin.site.urls, name='admin'),
    path('terms/', main_views.terms, name='terms'),
    path('1/<slug:pk>/export/', forms_views.not_ready),
    path('1/<slug:pk>/', forms_views.result),
    path('1/', forms_views.form, name='10gum'),
    path('<int:pk>/', forms_views.not_ready),
    path('', main_views.home, name='home'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
