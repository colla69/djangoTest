from django.db import models


# Create your models here.
class Store(models.Model):
    title = models.TextField(default="cool shit")
    desc = models.TextField()
    price = models.TextField()


class ProjectInfos(models.Model):
    name = models.TextField(db_column='Name', max_length=100)  # Field name made lowercase.
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=4000, blank=True, null=True)
    role_name = models.TextField(max_length=50, blank=True, null=True)
    lang = models.CharField(max_length=100, blank=True, null=True)
    company = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'project_infos'



