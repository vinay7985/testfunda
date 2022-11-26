from rest_framework import serializers
from fundamentals.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Snippet
        fields="__all__"

    