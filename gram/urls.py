from django.conf.urls import url, include
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    # url(r'signup', views.signup, name='signup'),
    url(r'^index/$', views.index, name='index'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^update_profile/', views.update_profile, name='update_profile'),
    url(r'^accounts/profile/', views.profile, name='profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
