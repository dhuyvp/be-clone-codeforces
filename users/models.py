from django.db import models

# Create your models here.
class CodeforcesUser(models.Model) :
    id = models.IntegerField(primary_key=True, null=False)
    username = models.CharField(max_length=256)

    class Meta:
        db_table = 'test_table'