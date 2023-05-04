from django.urls import path
from web import views


app_name = "web"


urlpatterns = [
    path('', views.index, name='index'),
    path('facility/<int:id>/', views.facility, name='facility'),
    path('department/<int:id>/', views.department, name='department'),
    path('event/<int:id>/', views.event, name='event'),
    path('application/', views.form, name='form'),
    path('application/download/<int:id>/', views.download, name='download'),
]