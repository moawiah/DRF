from django.shortcuts import render
from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieSerializer

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionMoviesViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='Action')
    serializer_class = MovieSerializer

