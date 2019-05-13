from django.conf.urls import url
from user.views import AddNewUser

urlpatterns = [
    url(r'^api/v0/create/', AddNewUser.as_view(), name='create_user')
]
