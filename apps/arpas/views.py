from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView

from adhocracy4.dashboard import mixins
from adhocracy4.filters import views as filter_views
from adhocracy4.projects.mixins import DisplayProjectOrModuleMixin
from adhocracy4.projects.mixins import ProjectMixin
from adhocracy4.rules import mixins as rules_mixins

from ..contrib.django_standard_messages import _
from ..contrib.views import CanonicalURLDetailView
from . import filters
from . import forms
from . import models


class Object3DListView(
    ProjectMixin, filter_views.FilteredListView, DisplayProjectOrModuleMixin
):
    model = models.Object3D
    filter_set = filters.Object3DFilterSet


class Object3DDetailView(
    ProjectMixin,
    rules_mixins.PermissionRequiredMixin,
    CanonicalURLDetailView,
    DetailView,
):
    model = models.Object3D
    permission_required = "a4_candy_arpas.view_object3d"


class Object3DListDashboardView(
    ProjectMixin,
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    filter_views.FilteredListView,
):
    model = models.Object3D
    template_name = "a4_candy_arpas/object3d_dashboard_list.html"
    permission_required = "a4projects.change_project"
    filter_set = filters.SubjectCreateFilterSet

    def get_queryset(self):
        return super().get_queryset().filter(module=self.module)

    def get_permission_object(self):
        return self.project


class AbstractObject3DCreateView(
    ProjectMixin, rules_mixins.PermissionRequiredMixin, generic.CreateView
):
    def get_permission_object(self, *args, **kwargs):
        return self.module

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.module = self.module
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs["module"] = self.module
        # kwargs["user"] = self.request.user
        kwargs.pop("module", None)  # Remove the 'module' argument
        kwargs.pop("user", None)  # Remove the 'user' argument

        if self.module.settings_instance:
            kwargs["settings_instance"] = self.module.settings_instance
        return kwargs


class Object3DCreateView(
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    mixins.DashboardComponentFormSignalMixin,
    AbstractObject3DCreateView,
):
    model = models.Object3D
    form_class = forms.Object3DForm
    permission_required = "a4_candy_arpas.add_object3d"
    template_name = "a4_candy_arpas/object3d_create_form.html"

    def get_success_url(self):
        return reverse(
            "a4dashboard:object3d-list",
            kwargs={
                "organisation_slug": self.module.project.organisation.slug,
                "module_slug": self.module.slug,
            },
        )

    def get_permission_object(self):
        return self.module


class Object3DUpdateView(
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    mixins.DashboardComponentFormSignalMixin,
    ProjectMixin,
    rules_mixins.PermissionRequiredMixin,
    # UserFormViewMixin,
    generic.UpdateView,
):
    model = models.Object3D
    form_class = forms.Object3DForm
    permission_required = "a4_candy_arpas.change_object3d"
    template_name = "a4_candy_arpas/object3d_update_form.html"


@property
def organisation(self):
    return self.project.organisation


def get_success_url(self):
    return reverse(
        "a4dashboard:object3d-list",
        kwargs={
            "organisation_slug": self.module.project.organisation.slug,
            "module_slug": self.module.slug,
        },
    )


def get_permission_object(self):
    return self.get_object()


class Object3DDeleteView(
    mixins.DashboardBaseMixin,
    mixins.DashboardComponentMixin,
    mixins.DashboardComponentFormSignalMixin,
    ProjectMixin,
    rules_mixins.PermissionRequiredMixin,
    generic.DeleteView,
):
    model = models.Object3D
    success_message = _("Your 3D-Object has been deleted")
    permission_required = "a4_candy_debate.change_object3d"
    template_name = "a4_candy_arpas/object3d_delete_form.html"

    def get_success_url(self):
        return reverse(
            "a4dashboard:object3d-list",
            kwargs={
                "organisation_slug": self.module.project.organisation.slug,
                "module_slug": self.module.slug,
            },
        )
