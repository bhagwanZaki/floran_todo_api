from django.db.models import fields
from rest_framework import serializers
from .models import *

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','title','date_created','completed','date_completed_by','completed_at']