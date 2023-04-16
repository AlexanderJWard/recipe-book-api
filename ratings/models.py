from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Rating(models.Model):
    """
    Rating model, related to Owner and Post
    'owner' is a User interface and 'post' is a Post instance
    'unique_together' makes sure a user can't like the same post twice
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='ratings'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    rating_stars = [
        (1, '1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    ]
    rating = models.CharField(
        max_length=10,
        choices=rating_stars,
        default=3,
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post', 'rating']

    def __str__(self):
        return f"{self.owner} {self.rating} {self.post}"
