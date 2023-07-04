from rest_framework import serializers
from .models import *

class clothmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = clothmodel
        fields = '__all__'