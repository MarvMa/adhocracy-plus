from django.utils.translation import gettext_lazy as _

from adhocracy4 import phases

from . import apps
from . import models
from . import views


class ArpasPhase(phases.PhaseContent):
    app = apps.Config.label
    phase = "arpas"
    view = views.Object3DListView

    name = _("ARPAS phase")
    description = _("Review and rate 3D objects) Ideas.")
    module_name = _("arpas")

    features = {"rate": (models.Object3D,)}


phases.content.register(ArpasPhase())
