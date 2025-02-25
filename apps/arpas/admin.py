from django.contrib import admin

from .models import Object3D


@admin.register(Object3D)
class Object3DAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "file", "uploaded_at")
    search_fields = ("name", "file")
    list_filter = ("uploaded_at",)
