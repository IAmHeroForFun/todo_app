from django.urls import path
from .views import HomeNoteView, AboutView, NewNoteView, DeleteNoteView, UpdateNoteView

urlpatterns = [
    path("", HomeNoteView.as_view(), name="note_list"),
    path("new/", NewNoteView.as_view(), name="new_note"),
    path("<int:pk>/delete/", DeleteNoteView.as_view(), name="delete_note"),
    path("<int:pk>/update/", UpdateNoteView.as_view(), name="update_note"),
    path("about/", AboutView.as_view(), name="about"),
]
