from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import BanksSerializeModel, DataClientSerializeModel
from .models import Banks
from .permissions import CustomPermissions
from .services import data_for_client


class BanksViewSet(viewsets.ModelViewSet):
    """This is modelViewSet provides CRUD functionality for Banks model.
       Additionally organized filter functional"""
    queryset = Banks.objects.all()
    serializer_class = BanksSerializeModel
    permission_classes = [CustomPermissions, ]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['bank_name', 'interest_rate']


@api_view(['POST'])
def calculate_value(request):
    """Return a list of JSON objects to the client."""
    serial = DataClientSerializeModel(data=request.data)
    serial.is_valid()
    validate = serial.validated_data
    client_response = data_for_client(validate)
    return Response(client_response)
