from rest_framework import serializers
from .models import Testtable,Company,Profile

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Testtable
        fields='__all__'

    def create(self,validated_data):
        return Testtable.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.linkedin_url=validated_data.get('linkedin_url',instance.linkedin_url)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.save()
        return instance



class Company_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'

    def create(self,validated_data):
        return Company.objects.create(**validated_data)


class Profile_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

    def create(self,validated_data):
        return Profile.objects.create(**validated_data)
