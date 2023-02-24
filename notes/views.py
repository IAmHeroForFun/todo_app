from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Note
from django.urls import reverse_lazy


class HomeNoteView(ListView):
    model = Note
    template_name = "home.html"


class NewNoteView(CreateView):
    model = Note
    template_name = "new_note.html"
    fields = (
        "title",
        "body",
    )
    success_url = "/"


class UpdateNoteView(UpdateView):
    model = Note
    fields = (
        "title",
        "body",
        "status",
    )
    template_name = "update_note.html"
    success_url = reverse_lazy("note_list")


class DeleteNoteView(DeleteView):
    model = Note
    template_name = "note_delete.html"
    success_url = reverse_lazy("note_list")


class AboutView(TemplateView):
    template_name = "about.html"
