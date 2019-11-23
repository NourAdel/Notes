from rest_framework import serializers
from . import models

# serializing our model and return data from it as Json

class NoteSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = '__all__'