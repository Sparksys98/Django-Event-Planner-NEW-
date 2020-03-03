from rest_framework import serializers
from events.models import Event,Booking
from django.contrib.auth.models import User
class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['title','datetime']

class ListEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=['title','datetime']

    def get_queryset(self):
        queryset = super(UserInfo, self).get_queryset()
        user = self.request.user
        return queryset.filter(user=user)

class RegisterSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)
        class Meta:
            model = User
            fields = ['username', 'password']

        def create(self, validated_data):
            username = validated_data['username']
            password = validated_data['password']
            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()
            return validated_data
