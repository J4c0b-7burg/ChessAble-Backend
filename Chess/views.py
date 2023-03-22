from .models import Chess
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ChessSerializer


class ChessViewSet(viewsets.ModelViewSet):

    queryset = Chess.objects.all()

    serializer_class = ChessSerializer

    permission_classes = [permissions.AllowAny]