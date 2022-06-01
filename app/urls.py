from django.urls import path
from . import views

urlpatterns = [
    # path('', views.hi, name='hi'),
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('history/', views.history, name='history')
]
