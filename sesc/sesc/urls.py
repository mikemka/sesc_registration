from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from main import views as main__views
from forms import views as forms__views
from core import views as core__views


urlpatterns = [
    path('lk/', admin.site.urls, name='admin'),
    path('terms/', main__views.terms, name='terms'),

    path('1/<slug:pk>/', forms__views.result),
    path('1/', forms__views.form, name='10gum'),

    path('2/<slug:pk>/', forms__views.result2),
    path('2/', forms__views.form2, name='10sgum'),

    path('<int:pk>/', forms__views.not_ready),
    
    path('export/', core__views.export, name='export'),
    path('', main__views.home, name='home'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
