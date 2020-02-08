from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from. import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('acc/', include('accounts.urls')),
    path('j/', include('jobs.urls')),
    path('about/', views.about,name='about'),
    path('contact/', views.contact),
    path('send/',views.sendemail),
    path('', views.home),
]
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()