from rest_framework import serializers
from .models import Collection, Characteristic, Userfavorite

class CollectionSerializer(serializers.ModelSerializer):
    owber = serializers.ReadOnlyField(source='owner.username')
    chacater_count = serializers.IntegerField( read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'name', 'description', 'is_public', 'created_at', 'updated_at']

class CharacteristicSerializer(serializers.ModelSerializer):
    added_by  = serializers.ReadOnlyField(source='added_by.username')
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Characteristic
        fields = ['id', 'external_id', 'name', 'status', 'species', 'gender', 'image','origin_name','location_name','added_by','created_at','is_favorite']
    
    def get_is_favorite(self, obj):
        user = self.context('request').user
        if user.is_authenticated:
            return Userfavorite.objects.filter(user=user, character=obj).exists()
        return False
    
class UserfavoriteSerializer(serializers.ModelSerializer):
    character = CharacteristicSerializer(read_only=True)

    class Meta:
        model = Userfavorite
        fields = ['id', 'character', 'notes', 'created_at']
        