from django.shortcuts import render
from progetti.models import User, Esterno, FunzioneStrumentale, Materiale, Progetto
from progetti.serializers import UserSerializer, EsternoSerializer, FunzioneStrumentaleSerializer, MaterialeSerializer, ProgettoSerializer
from rest_framework import generics, permissions

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EsternoList(generics.ListCreateAPIView):
    queryset = Esterno.objects.all()
    serializer_class = EsternoSerializer

class EsternoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Esterno.objects.all()
    serializer_class = EsternoSerializer

class FunzioneStrumentaleList(generics.ListCreateAPIView):
    queryset = FunzioneStrumentale.objects.all()
    serializer_class = FunzioneStrumentaleSerializer

class FunzioneStrumentaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FunzioneStrumentale.objects.all()
    serializer_class = FunzioneStrumentaleSerializer

class MaterialeList(generics.ListCreateAPIView):
    queryset = Materiale.objects.all()
    serializer_class = MaterialeSerializer

class MaterialeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materiale.objects.all()
    serializer_class = MaterialeSerializer

class ProgettoList(generics.ListCreateAPIView):
    queryset = Progetto.objects.all()
    serializer_class = ProgettoSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProgettoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progetto.objects.all()
    serializer_class = ProgettoSerializer

def index(request):
    """View function for home page of site."""

    context = {
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
