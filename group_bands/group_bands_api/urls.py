from django.urls import path
from .views import ListGroupsApiView


urlpatterns = [
    path('get-all-groups/', ListGroupsApiView.as_view())
]
