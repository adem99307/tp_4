from rest_framework import serializers
from . models import tache

class tacheSerializers(serializers.ModelSerializer):
    class Meta:
        model=tache
        fields='__all__'

