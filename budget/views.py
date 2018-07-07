from rest_framework import generics

from .models import Account
from .serializer import AccountSerializer


class AccountListCreateView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
