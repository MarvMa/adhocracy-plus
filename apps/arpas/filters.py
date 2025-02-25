from django.utils.translation import gettext_lazy as _

from adhocracy4.filters import filters as a4_filters
from apps.contrib.widgets import AplusOrderingWidget

from . import models


class Object3DFilterSet(a4_filters.DefaultsFilterSet):

    defaults = {"ordering": "name"}

    ordering = a4_filters.DynamicChoicesOrderingFilter(
        choices=(("name", _("Alphabetical")),), widget=AplusOrderingWidget
    )

    class Meta:
        model = models.Object3D
        fields = []


class SubjectCreateFilterSet(a4_filters.DefaultsFilterSet):

    defaults = {"ordering": "name"}

    ordering = a4_filters.DynamicChoicesOrderingFilter(
        choices=(("name", _("Alphabetical")),), widget=AplusOrderingWidget
    )

    class Meta:
        model = models.Object3D
        fields = []
