from progetti.models import Docente, Esterno, FunzioneStrumentale, Materiale, Progetto
from progetti.serializers import DocenteSerializer, EsternoSerializer, FunzioneStrumentaleSerializer, MaterialeSerializer, ProgettoSerializer
from rest_framework import generics

class DocenteList(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class DocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

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

class ProgettoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Progetto.objects.all()
    serializer_class = ProgettoSerializer
