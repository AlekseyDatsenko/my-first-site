from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.main_en, name='index'),
	url(r'^contact/$', views.tel, name='contact'),
	url(r'^info/$', views.info, name='info'),
	url(r'^ru/$', views.main_ru, name='ru'),
	url(r'^contact_ru/$', views.tel_ru, name='contact_ru'),
	url(r'^info_ru/$', views.info_ru, name='info_ru'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
