from django.db import models

STATUS_CHOICE = (
    ("Done","DONE"),
    ("Pending","PENDING"),
)


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, default="Pending")

    def __str__(self):
        return self.title
