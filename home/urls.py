from django.urls import path
from . import views

urlpatterns = [
    path('registrate/', views.signup, name='sign_up'),
]
urlpatterns += [
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('activate/(?P<uidb64>[0-9a-z-]+)/(?P<token>[0-9a-z-]+)/$',
        views.activate, name='activate'),
]