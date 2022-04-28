from random import randint
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.urls import path
from main import views as main
from forms import views as forms
from core.views import export


urlpatterns = [
    path('lk/', admin.site.urls, name='admin'),
    path('terms/', main.terms, name='terms'),
    path('export/', export, name='export'),
    
    path('aboba/', (lambda request: HttpResponse(' '.join([f'<span style=\'color: rgb({randint(1, 255)}, {randint(1, 255)}, {randint(1, 255)});\'>абоба</span>' for _ in range(500)]))), name='aboba'),

    path('', main.home, name='home'),

    path('1/<slug:pk>/', forms.result),
    path('1/', forms.form, name='10gum'),

    path('2/<slug:pk>/', forms.result2),
    path('2/', forms.form2, name='10sgum'),

    path('3/<slug:pk>/', forms.result3),
    path('3/', forms.form3, name='10socek'),

    path('4/<slug:pk>/', forms.result4),
    path('4/', forms.form4, name='10matinf'),

    path('5/<slug:pk>/', forms.result5),
    path('5/', forms.form5, name='10fizmat'),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
