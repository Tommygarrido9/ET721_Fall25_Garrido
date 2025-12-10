from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=255)

    def average_rating(self):
        qs = self.feedback_set.all()
        if not qs.exists():
            return None
        return round(sum(f.rating for f in qs)/(qs.count()), 2)
    
    def feedback_count(self):
        return self.feedback_set.count()
    
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Feedback for {self.item.name} - {self.rating} stars'
    