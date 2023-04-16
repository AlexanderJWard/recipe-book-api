from django.db import models
from django.contrib.auth.models import User


class Support(models.Model):
    ticket_status = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('resolved', 'Resolved'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=25,
        choices=ticket_status,
        default='new'
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    issue = models.TextField(blank=False)
    screenshot = models.ImageField(
        upload_to='images/', default='../default_post_ribt4r',
        blank=True
    )

    class Meta:
        ordering = ['status']

    def __str__(self):
        return f'{self.id} {self.title}'
