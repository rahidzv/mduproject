from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Abuneci, ElaqeMesaji
from .serializers import AbunecilSerializer, ElaqeMesajiSerializer


@api_view(['POST'])
def abune_ol(request):
    # bulletene abune olma
    serializer = AbunecilSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'mesaj': 'Ugurla abune oldunuz!'},
            status=status.HTTP_201_CREATED
        )

    # eyni e-poct artiq qeydiyyatdan kecibse
    if 'email' in serializer.errors:
        for xeta in serializer.errors['email']:
            if 'unique' in str(xeta).lower() or 'exists' in str(xeta).lower():
                return Response(
                    {'mesaj': 'Bu e-poct artiq abunedir.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def elaqe_gonder(request):
    # elaqe formu melumatlari
    serializer = ElaqeMesajiSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'mesaj': 'Mesajiniz ugurla gonderildi!'},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
