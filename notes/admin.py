from django.contrib import admin
from .models import Note


@admin.action(description="Mark selected Note as Completed")
def completed(modeladmin, request, queryset):
    queryset.update(status="DONE")


@admin.action(description="Mark selected Note as Not Completed")
def not_completed(modeladmin, request, queryset):
    queryset.update(status="PENDING")


class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "created"]
    ordering = ["created"]
    actions = [completed, not_completed]


admin.site.register(Note, NoteAdmin)
