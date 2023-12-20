from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException


from secrets import compare_digest
from django.conf import settings

from xploit.users.models import BusinessProfile


class SignatureHeaderMissing(APIException):
    """Raised when the request does not have the signature."""
    status_code = 401
    default_detail = "Signature header is missing. Make sure Xpt-Authentication-Token is present in header."
    default_code = "signature_header_missing"



class XploitPermission(BasePermission):

    def has_permission(self, request, *args, **kwargs):
        # Checking if the KOK auth is been authorized
        # is been authorized by switching it to true
       
        given_token = request.headers.get("Xpt-Authentication-Token", None)
        if settings.XPT_AUTH:
            if not given_token:
                raise SignatureHeaderMissing()
            return given_token == settings.KOK_AUTH_KEYS
        
        else:
            # given_token = None
            # return given_token == None
            raise SignatureHeaderMissing()


