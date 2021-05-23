from rest_framework import serializers
from .models import commission



class commissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = commission
        fields = '__all__'


