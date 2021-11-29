from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view

from api.views import (
    user_account,
    logs
)

schema_view = get_swagger_view(title='Phone Logs')
urlpatterns = [
    url(r'^docs/', schema_view, name='walletcore-api-docs'),
    url(r"^auth/register", user_account.user_registration, name="register user"),
    url(r"^auth/login", user_account.user_login, name="login user"),
    url(r"^users", user_account.view_users, name="user list"),
    url(r"^password-reset", user_account.reset_password, name="reset user password"),
    url(r"^logs/", logs.call_log_list, name="call logs"),
    # url(r"^logs/", logs.create_and_analyze_logs, name="create call logs"),

]
