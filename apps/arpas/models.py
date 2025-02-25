from autoslug import AutoSlugField
from django.contrib.contenttypes.fields import GenericRelation
from django.core.files.storage import default_storage
from django.db import models
from django.utils.translation import gettext_lazy as _

from adhocracy4.comments import models as comment_models
from adhocracy4.models import query
from adhocracy4.modules import models as module_models


class Object3D(module_models.Item):
    slug = AutoSlugField(populate_from="name", unique=True)
    name = models.CharField(max_length=255, help_text=_("max 255 characters"))
    file = models.FileField(storage=default_storage, upload_to="3d_objects/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    comments = GenericRelation(
        comment_models.Comment,
        related_query_name="object3d",
        object_id_field="object_pk",
    )
    objects = query.CommentableQuerySet.as_manager()

    def __str__(self):
        return self.name


#
# @cached_property
# def comment_creator_count(self):
#     creators = self.comments.values_list("creator", flat=True)
#     comment_creator_count = len(list(set(creators)))
#     return comment_creator_count
#
#
# @cached_property
# def comment_creator_count_minus_three(self):
#     if self.comment_creator_count <= 3:
#         return None
#     else:
#         return self.comment_creator_count - 3
#
#
# @cached_property
# def last_three_creators(self):
#     comments = (
#         self.comments.filter(
#             is_censored=False,
#             is_removed=False,
#         )
#         .select_related("creator")
#         .order_by("-created")
#     )
#
#     last_three_creators = []
#     if comments:
#         for comment in comments:
#             if comment.creator not in last_three_creators:
#                 last_three_creators.append(comment.creator)
#             if len(last_three_creators) >= 3:
#                 break
#
#     return last_three_creators
