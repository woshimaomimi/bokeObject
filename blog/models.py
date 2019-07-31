from django.db import models


class YptPower(models.Model):
    powerid = models.CharField(primary_key=True, max_length=255)
    powecontent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ypt_power'


class YptRole(models.Model):
    roleid = models.CharField(primary_key=True, max_length=255)
    rolename = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    powerid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ypt_role'


class YptUser(models.Model):
    userid = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    creattime = models.DateTimeField(blank=True, null=True)
    schooltime = models.DateTimeField(blank=True, null=True)
    logname = models.CharField(max_length=255, blank=True, null=True)
    schoolnumeral = models.CharField(max_length=255, blank=True, null=True)
    roleid = models.CharField(max_length=255, blank=True, null=True)
    usertype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ypt_user'