from django.urls import path

from send.views.informationView import InformationView
from send.views.userView import CustomLoginView

urlpatterns = [
    path('Informations/',InformationView.as_view()),
    path('login/', CustomLoginView.as_view()),
]