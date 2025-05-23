from django.urls import re_path

from oauth2_provider import views


app_name = "oauth2_provider"


base_urlpatterns = [
    re_path(r"^authorize/$", views.AuthorizationView.as_view(), name="authorize"),
    re_path(r"^token/$", views.TokenView.as_view(), name="token"),
    re_path(r"^revoke_token/$", views.RevokeTokenView.as_view(), name="revoke-token"),
    re_path(r"^introspect/$", views.IntrospectTokenView.as_view(), name="introspect"),
]


management_urlpatterns = [
    # Application management views
    re_path(r"^applications/$", views.ApplicationList.as_view(), name="list"),
    re_path(r"^applications/register/$", views.ApplicationRegistration.as_view(), name="register"),
    re_path(r"^applications/(?P<pk>[\w-]+)/$", views.ApplicationDetail.as_view(), name="detail"),
    re_path(r"^applications/(?P<pk>[\w-]+)/delete/$", views.ApplicationDelete.as_view(), name="delete"),
    re_path(r"^applications/(?P<pk>[\w-]+)/update/$", views.ApplicationUpdate.as_view(), name="update"),
    # Token management views
    re_path(r"^authorized_tokens/$", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    re_path(r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$", views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
]


urlpatterns = base_urlpatterns + management_urlpatterns
