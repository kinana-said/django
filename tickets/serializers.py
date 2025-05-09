from rest_framework import serializers
from tickets.models import  Guest,Movie,Resevation


class MovieSerializer (serializers.ModelSerializer):
    class Meta:
        model=Movie
        Fields='__all__'

class ResevationSerializer (serializers.ModelSerializer):
    class Meta:
        model=Resevation
        Fields='__all__'

class GuestSerializer (serializers.ModelSerializer):
    class Meta:
        model=Guest
        Fields=['pk','Resevation','name','mobile']       