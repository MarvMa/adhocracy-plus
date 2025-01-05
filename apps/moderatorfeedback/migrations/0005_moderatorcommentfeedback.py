# Generated by Django 3.2.18 on 2023-03-30 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("a4comments", "0010_verbose_name_created_modified"),
        ("a4_candy_moderatorfeedback", "0004_verbose_name_created_modified"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModeratorCommentFeedback",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, editable=False, null=True, verbose_name="Modified"
                    ),
                ),
                (
                    "feedback_text",
                    models.TextField(blank=True, verbose_name="Moderator feedback"),
                ),
                (
                    "comment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="moderator_feedback",
                        to="a4comments.comment",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
