from django.db import models

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('wish', 'Пожелание'),
        ('issue', 'Проблема'),
        ('complaint', 'Претензия'),
        ('other', 'Другое'),
    ]

    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_TYPES)
    message = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_feedback_type_display()} от {self.created_at.strftime("%Y-%m-%d %H:%M")}'
