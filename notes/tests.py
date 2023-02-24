from django.test import TestCase
from django.urls import reverse
from .models import Note


class ToDoTests(TestCase):
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def if_about_exists(self):
        response = self.client.get("about")
        self.assertEqual(response.status_code, 200)

    def if_delete_exists(self):
        respone = self.client.get("delete_note")
        self.assertEqual(respone.status_code, 200)

    def if_update_exists(self):
        response = self.client.get("update_note")
        self.assertEqual(response.status_code, 200)

    def if_new_exists(self):
        response = self.client.get("new_note")
        self.assertEqual(response.status_code, 200)


class NotePostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.note = Note.objects.create(title="NOTE1", body="NOTEBODY1")

    def test_model_content(self):
        self.assertEqual(self.note.title, "NOTE1")
        self.assertEqual(self.note.body, "NOTEBODY1")

    def note_update_test(self):
        response = self.client.post(
            reverse("update_note", args="1"),
            {
                "title": "updatednote",
                "body": "updatedbody",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.last().title, "updatednote")
        self.assertEqual(Note.objects.last().body, "updatedbody")

    def note_delete_test(self):
        response = self.client.post(reverse("delete_note", args="1"))
        self.assertEqual(response.status_code, 302)
