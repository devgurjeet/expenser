from django.urls import path

from .views import AccountListCreateView, AccountRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('account/', AccountListCreateView.as_view(), name='account-list-create'),
    path('account/<int:id>/', AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-list-create')

]
