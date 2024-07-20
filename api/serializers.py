from rest_framework import serializers
from models import Empresa

class EmpresaSerializer(serializers.Serializer):
    empresa_id = serializers.CharField(max_length=2)
    nro_ruc = serializers.CharField(max_length=11,required=True,source="empresa_nro_ruc")
    razon_social = serializers.CharField(required=True,source="empresa_razon_social")
    acronimo = serializers.CharField(required=True, source="empresa_acronimo")
    direccion = serializers.CharField(required=True, source="empresa_direccion")
    avatar = serializers.ImageField(max_length=None, source="empresa_avatar")

    class Meta:
        model = Empresa
        fields = ['empresa_id','empresa_nro_ruc','empresa_razon_social','empresa_acronimo','empresa_direccion','empresa_avatar']
    
    def create(self, validated_data):
        empresa = Empresa.objects.create(**validated_data)
        return empresa
    
    def update(self, instance, validated_data):
        instance.empresa_id = validated_data.get('empresa_id', instance.empresa_id)
        instance.empresa_razon_social = validated_data.get('empresa_razon_social')
        instance.empresa_direccion = validated_data.get('empresa_direccion',instance.empresa_direccion)
        instance.empresa_nro_ruc = validated_data.get('empresa_nro_ruc',instance.empresa_nro_ruc)
        instance.empresa_acronimo = validated_data.get('empresa_acronimo',instance.empresa_acronimo)
        instance.empresa_avatar = validated_data.get('empresa_avatar',instance.empresa_avatar)
        instance.save()
        return instance