from django.db import models


class Tweet(models.Model):
    content = models.TextField()

    def __str__(self):
        return 'Tweet - {0}'.format(self.id)
