from django.urls import *
from .views import *

urlpatterns = [
   path('home/',home,name='home'),
   path('add/',add,name='add'),
   path('view/',view,name='view')


]
