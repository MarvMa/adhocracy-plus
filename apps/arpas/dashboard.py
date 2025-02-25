from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from adhocracy4.dashboard import DashboardComponent
from adhocracy4.dashboard import components

from . import models
from . import views


class Object3DEditComponent(DashboardComponent):
    identifier = "object3d_edit"
    weight = 20
    label = _("3D Objects")

    def is_effective(self, module):
        return module.blueprint_type == "AR"

    def get_progress(self, module):
        if models.Object3D.objects.filter(module=module).exists():
            return 1, 1
        return 0, 1

    def get_base_url(self, module):
        return reverse(
            "a4dashboard:object3d-list",
            kwargs={
                "organisation_slug": module.project.organisation.slug,
                "module_slug": module.slug,
            },
        )

    def get_urls(self):
        return [
            (
                r"^object3d/module/(?P<module_slug>[-\w_]+)/$",
                views.Object3DListDashboardView.as_view(component=self),
                "object3d-list",
            ),
            (
                r"^object3d/create/module/(?P<module_slug>[-\w_]+)/$",
                views.Object3DCreateView.as_view(component=self),
                "object3d-create",
            ),
            (
                r"^object3d/(?P<pk>\d+)/update/$",
                views.Object3DUpdateView.as_view(component=self),
                "object3d-update",
            ),
            (
                r"^object3d/(?P<pk>\d+)/delete/$",
                views.Object3DDeleteView.as_view(component=self),
                "object3d-delete",
            ),
        ]


components.register_module(Object3DEditComponent())
