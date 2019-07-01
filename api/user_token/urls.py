from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from views import ValidateToken
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
    url(r'^api/v0/login/$', rest_framework_views.obtain_auth_token,
        name="get_tokin_login"),
    url(r'^api/v0/validate/', ValidateToken.as_view(), name="validator")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
