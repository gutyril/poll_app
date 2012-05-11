from django.db import models
import datetime
from django.utils import timezone


# Poll
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #Unicode method
    def __unicode__(self):
        return self.question

    #Method that return if a poll has been published until 1 day before
    def was_published_recently(self):
        return self.pub_date <= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


#Choice
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    #Self method
    def __unicode__(self):
        return self.choice
