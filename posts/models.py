from django.db import models


class Post(models.Model):
    difficulty_choice = [
        ('beginner', 'Beginner'),
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
        ('expert', 'Expert'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    prep_time_minutes = models.PositiveIntegerField(default=0, max_value=480)
    cooking_time_minutes = models.PositiveIntegerField(
        default=0,
        max_value=480
    )
    ingredients = models.TextField(blank=True)
    method = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ribt4r',
        blank=True
    )
    difficulty = models.CharField(
        max_length=10, choices=difficulty_choice, default='medium'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
