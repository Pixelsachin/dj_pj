from django.urls import path
from . import views

app_name = 'notebooks'
urlpatterns = [
    # path('about/', views.about),
    # path('source', views.source),
    path('', views.home, name="home"),

]
