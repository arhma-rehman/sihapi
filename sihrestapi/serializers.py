from dataclasses import fields
from xml.parsers.expat import model
from rest_framework import serializers
from .models import student


class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'