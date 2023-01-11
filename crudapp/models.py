from django.db import models

#table fields and its size
class User(models.Model):
    uname = models.CharField(max_length=100)
    uemail = models.CharField(max_length=100)
    upassword = models.CharField(max_length=100)

#table name
    class Meta:
        db_table="users"
