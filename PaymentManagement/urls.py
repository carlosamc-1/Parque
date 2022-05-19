from django.urls import path, include
#from .views import contrato_detail_view, contrato_create_view, contrato_update_view, contrato_delete_view
from . import views

app_name = "contrato"
urlpatterns = [
    path('', views.contratos_list.as_view(), name='contrato-list'), #
    path('<int:id>/', views.contrato_detail_view, name="contrato-detail"),
    path('create/', views.contrato_create_view, name="contrato-create"),
    path('<int:id>/update/', views.contrato_update_view, name="contrato-update"),
    path('<int:id>/delete/', views.contrato_delete_view, name="contrato-delete"),
]
