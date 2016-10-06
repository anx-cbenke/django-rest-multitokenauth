""" URL Configuration for core auth
"""
from django.conf.urls import url, include
from eric.coreauth.views import login_and_obtain_auth_token, logout_and_delete_auth_token

urlpatterns = [
    url(r'^login', login_and_obtain_auth_token),  # normal login with session
    url(r'^logout', logout_and_delete_auth_token),
]