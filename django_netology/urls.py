from django.contrib import admin
from django.urls import path, register_converter
from app import views
from app.converter import DateConverter

register_converter(DateConverter, 'dtc')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('info/<int:year>-<int:month>-<int:day>/', views.info_view, name='info-view')
    path('info/', views.info_view, name='info-view')
]
