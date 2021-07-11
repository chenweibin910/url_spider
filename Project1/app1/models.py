from django.db import models

# Create your models here.
class Home(models.Model):
    date = models.DateField(max_length=15)
    exec_time = models.DateTimeField(max_length=20)
    info = models.TextField(max_length=1000)

    class Meta:
        verbose_name = "Page1"
        verbose_name_plural = "页面1"

    # def __iter__(self):
    #     return self.date, self.exec_time, self.info
    def __unicode__(self):
        return u"id:%s" % self.id
