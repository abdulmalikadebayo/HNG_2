from django.urls import path
from .views import PersonListCreate, PersonDetail

urlpatterns = [
    path('api/', PersonListCreate.as_view(), name='person-list-create'),
    path('api/<int:pk>/', PersonDetail.as_view(), name='person-detail'),
]
 