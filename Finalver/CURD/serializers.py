from rest_framework import serializers

from .models import Curd

class Curds(serializers.ModelSerializer):
    class Meta:
        model = Curd
        fields = '__all__'