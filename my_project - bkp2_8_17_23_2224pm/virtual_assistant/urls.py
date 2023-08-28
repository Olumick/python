from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('specific',views.specific,name='specific'),

    # Ajax url: to send the data from frontend to back end
    path('getResponse',views.getResponse,name='getResponse')


]

