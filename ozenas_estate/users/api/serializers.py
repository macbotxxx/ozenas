from django.contrib.auth import get_user_model
from rest_framework import serializers

from ozenas_estate.users.models import User as UserType


User = get_user_model()

# serializers
class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = ["name", "url"]
        ref_name = "ozeansmodelsuser"

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
