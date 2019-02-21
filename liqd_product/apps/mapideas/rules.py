import rules

from adhocracy4.modules import predicates as module_predicates

from . import models

rules.add_perm(
    'liqd_product_mapideas.view_mapidea',
    module_predicates.is_allowed_view_item
)

rules.add_perm(
    'liqd_product_mapideas.add_mapidea',
    module_predicates.is_allowed_add_item(models.MapIdea)
)

rules.add_perm(
    'liqd_product_mapideas.rate_mapidea',
    module_predicates.is_allowed_rate_item
)

rules.add_perm(
    'liqd_product_mapideas.comment_mapidea',
    module_predicates.is_allowed_comment_item
)

rules.add_perm(
    'liqd_product_mapideas.change_mapidea',
    module_predicates.is_allowed_change_item
)

rules.add_perm(
    'liqd_product_mapideas.moderate_mapidea',
    module_predicates.is_context_moderator |
    module_predicates.is_context_initiator
)
