from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Creation of User's serializer """
    class Meta:
        model = User
        fields = "__all__"
