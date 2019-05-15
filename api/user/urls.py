from django.conf.urls import url
from user.views import (
    AddNewUser,
    DeleteUser)

urlpatterns = [
    url(r'^api/v0/create/', AddNewUser.as_view(), name='create_user'),
    url(r'^api/v0/destroy/(?P<username>\w+)/$', DeleteUser.as_view(),
        name='destroy_user')
]
