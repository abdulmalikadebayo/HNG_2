from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def personCreate(self, serializer):
        name = self.request.data.get('name')
        user = Person(name = name)
        user.save()

    def get_queryset(self):
        queryset =  super().get_queryset()
        name = self.request.query_params.get('name', None)
        
        if name:
                # Filter the queryset based on the provided name
            queryset= queryset.filter(name=name)
        return queryset
    

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def personUpate(self, serializer):
        name = self.request.data.get('name')
        if name:
            serializer.instance.name = name
        serializer.save()
