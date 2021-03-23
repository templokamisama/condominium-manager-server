from rest_framework import serializers

from reservation.models import Structure


class MessageResponseSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)


class StructureSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Structure
        fields = '__all__'

    def create(self, validated_data):
        structure = Structure.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            longitude=validated_data.get('longitude'),
            latitude=validated_data.get('latitude'),
            available=validated_data.get('available'),
            image=validated_data.get('image')
        )
        return structure


class StructureEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ('name', 'description', 'longitude', 'latitude', 'available', 'image')


class StructureSearchParamSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)
    available = serializers.BooleanField(required=False)
