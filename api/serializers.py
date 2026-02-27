from rest_framework import serializers
from .models import Abuneci, ElaqeMesaji


class AbunecilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abuneci
        fields = ['id', 'email', 'tarix']
        read_only_fields = ['tarix']


class ElaqeMesajiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElaqeMesaji
        fields = ['id', 'ad', 'email', 'mesaj', 'tarix']
        read_only_fields = ['tarix']
