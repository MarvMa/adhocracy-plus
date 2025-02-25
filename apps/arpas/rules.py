import rules

from adhocracy4.modules import predicates as module_predicates

rules.add_perm(
    "a4_candy_arpas.add_object3d", module_predicates.is_allowed_moderate_project
)

rules.add_perm(
    "a4_candy_arpas.change_object3d", module_predicates.is_allowed_moderate_project
)

rules.add_perm(
    "a4_candy_arpas.view_object3d",
    (
        module_predicates.is_allowed_moderate_project
        | module_predicates.is_allowed_view_item
    ),
)

rules.add_perm(
    "a4_candy_arpas.comment_object3d", module_predicates.is_allowed_comment_item
)
