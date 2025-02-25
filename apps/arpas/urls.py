# arpas/urls.py
from django.urls import path

from . import api
from . import views

urlpatterns = [
    # HTML-based views
    path("object3d/", views.Object3DListView.as_view(), name="object3d_list"),
    path(
        "object3d/create/", views.Object3DCreateView.as_view(), name="object3d_create"
    ),
    path(
        "object3d/<int:pk>/", views.Object3DDetailView.as_view(), name="object3d_detail"
    ),
    path(
        "object3d/<int:pk>/update/",
        views.Object3DUpdateView.as_view(),
        name="object3d_update",
    ),
    path(
        "object3d/<int:pk>/delete/",
        views.Object3DDetailView.as_view(),
        name="object3d_delete",
    ),
    # REST API views
    path("api/object3d/", api.Object3DViewSet.as_view(), name="object3d_list_api"),
]
