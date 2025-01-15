
from django.urls import path
from . import views
#localshost:8000/vijayapp
#localshost:8000/vijayapp/order

urlpatterns = [
    path('',views.all_chai, name='all_vijay'),
    # path('order',views.order, name='order'),
    
]