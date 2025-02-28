from django.urls import path
from .views import AddressCreate, AddressList,AddressUpdate, AddressDetail,AddressDelete

app_name = 'usuarios'

urlpatterns = [
    path('cep/', cep_search_view, name='cep'),
]

urlpatterns = [
    path('criar/', AddressCreate.as_view(), name ='criar'),
    path('listar/', AddressList.as_view(), name ='listar'),
    path('editar/<int:pk>/', AddressUpdate.as_view(), name ='atualizar'),
    path('detalhes/<int:pk>/', AddressDetail.as_view(), name ='detalhes'),
    path('deletar/<int:pk>/', AddressDelete.as_view(), name ='deletar'),
]