from .models import Group, Person, Membership
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Membership
        fields = ['person', 'date_joined', 'invite_reason']


class GroupSerializer(serializers.ModelSerializer):
    members = MembershipSerializer(source='membership_set', many=True)

    class Meta:
        model = Group
        fields = ['name', 'members']
