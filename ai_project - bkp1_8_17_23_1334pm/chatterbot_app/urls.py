from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    
    path('machine_learning',views.machine_learning,name='machine_learning'),

    path('specific',views.specific,name='specific')

    # path('article/<int:article_id>',views.article,name='article'),

    # Ajax url: to send the data from frontend to back end
    # path('getResponse',views.getResponse,name='getResponse')


]

