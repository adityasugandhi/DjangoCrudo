from Finalver.CURD.views import CustomerDelete, Customerlist
from django.urls import path
from .import views

urlpatterns = [
    path('', views.curdoverview, name='curdoveriew'),
    path('Customerlist/', views.Customerlist, name = 'Customer-list'),
    path('Customercreate/', views.CustomerCreate, name = 'Customer-create'),
    path('Customerupdate/<str:pk>', views.CustomerUpdate, name = 'Customer-update'),
    path('Customerdetail/<str:pk>', views.CustomerDetail, name = 'Customer-Details'),
    path('Customerdelelte/<str:pk>', views.CustomerDelete, name = 'Customer-Delete')
    
]