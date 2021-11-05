from rest_framework import serializers
from exercise.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'attack', 'life', 'origin')
    
    def create(self, validated_data):
        hero = Hero.objects.create(
            name=validated_data['name'],
            attack=validated_data['attack'],
            life=validated_data['life'],
            origin=validated_data['origin']
        )

        hero.save()
        return hero
    
    def validate(self, attrs):
        name = str(attrs['name'])
        origin = str(attrs['origin'])

        if not name.isalpha():
            raise serializers.ValidationError({"name": "Votre nom contient des caractères incorrects"})
            
        if attrs['attack'] > 10 or attrs['attack'] < 1:
            raise serializers.ValidationError({"attack": "Votre attaque doit être entre 1 et 10"})
        
        if attrs['life'] > 15 or attrs['life'] < 1:
            raise serializers.ValidationError({"life": "Votre vie doit être entre 1 et 15"})
        
        if not origin.isalpha():
            raise serializers.ValidationError({"origin": "l'origine contient des caractères incorrects"})

        return attrs

        
        

        
        


