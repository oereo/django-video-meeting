from django.urls import path
from agora.views import index, pusher_auth, generate_agora_token, call_user


urlpatterns = [
    path('', index, name='agora-index'),
    path('pusher/auth/', pusher_auth, name='agora-pusher-auth'),
    path('token/', generate_agora_token, name='agora-token'),
    path('call-user/', call_user, name='agora-call-user'),
]