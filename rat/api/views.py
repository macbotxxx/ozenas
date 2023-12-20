from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from ozenas_estate.users.api.serializers import UserSerializer
from rat.chrome import get_chrome

User = get_user_model()


class TestUrlViewset(
    GenericViewSet,
    ListModelMixin
    ):
    authentication_class = [ AllowAny, ]
    queryset = User.objects.all()
    lookup_field = "pk" 

    def list(self, request, *args, **kwargs):
        report = get_chrome()
        return Response({'data':'working', 'report':report})