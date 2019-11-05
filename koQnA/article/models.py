from django.db import models
from koQnA.models import TimeStampedModel
from accounts.models import User

class Article(TimeStampedModel):
    title = models.CharField(verbose_name='제목', max_length=100, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            verbose_name='작성자'
            )

    def __str__(self):
        return self.title


class Answer(TimeStampedModel):
    article = models.ForeignKey(
            Article,
            related_name='answers',
            on_delete=models.CASCADE
            )
    content = models.TextField()
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            verbose_name='작성자'
            )

    def __str__(self):
        return self.article.title
