from rest_framework import serializers
from api.models import CustomUser, Game, SquadRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","username","password","email","gamertag"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
        

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class SquadSerializer(serializers.ModelSerializer):
    creador_gamertag = serializers.ReadOnlyField(source="creator.gamertag")
    game_nombre = serializers.ReadOnlyField(source="game.nombre")
    creator_id = serializers.ReadOnlyField(source="creator.id")
    
    class Meta:
        model = SquadRequest
        fields= "__all__"
        read_only_fields=["creator"]