from django.urls import path
from . import views

urlpatterns = [
    path('',views.WillDecideLater,name='WillDecideLater'),
]