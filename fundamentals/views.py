from django.shortcuts import render
from rest_framework import viewsets
from fundamentals.models import Snippet
from fundamentals.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer