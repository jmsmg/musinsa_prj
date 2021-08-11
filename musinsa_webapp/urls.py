from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'musinsa_webapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_point/', views.get_point, name='get_point'),
    # path('simple_upload/',views.simple_upload, name ='simple_upload'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
