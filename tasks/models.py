from django.db import models
from django.contrib.auth.models import User
from sprints.models import Sprint


class Task(models.Model):
    """
    Stores a single task.
    account ties task with a :model:`auth.User`
    categories tie task with :model:`tasks.Category`
    """
    account = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    categories = models.ForeignKey("Category")
    sprint = models.ForeignKey(Sprint, blank=True, null=True, related_name='tasks')

    completed = models.BooleanField(default=False)

    weight = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def is_backlog(self):
        if not self.sprint:
            return True
        else:
            return False


class Category(models.Model):
    """
    Stores User Categories
    account ties category with a :model:`auth.User`
    """
    account = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_open_tasks(self):
        return self.task_set.filter(completed=False)