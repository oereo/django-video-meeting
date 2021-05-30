from django.urls import path
from agora.views import index, pusher_auth, generate_agora_token, call_user


urlpatterns = [
    path(' ', views.index, name='agora-index'),
    path('pusher/auth/', views.pusher_auth, name='agora-pusher-auth'),
    path('token/', views.generate_agora_token, name='agora-token'),
    path('call-user/', views.call_user, name='agora-call-user'),
]