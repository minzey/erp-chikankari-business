# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Assignment(models.Model):

    challanid = models.IntegerField()
    process = models.CharField(max_length=10, null=False, blank=False)
    karigar = models.ForeignKey('Karigar', models.DO_NOTHING, db_column='karigar')
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='product')
    qty = models.IntegerField(default=0)
    assignmentdate = models.DateField(null=False, blank=False)
    assignment_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        #db_table = 'assignments'
        unique_together = (('challanid', 'process','karigar','product'),)
        verbose_name_plural="Assignments"

    def __str__(self):
        return str(self.challanid)

class Bill(models.Model):
    billingid = models.IntegerField(primary_key=True)
    karigar = models.ForeignKey('Karigar', models.DO_NOTHING, db_column='karigar', blank=True, null=True)
    billingdate = models.DateField(blank=True, null=True)
    amountpaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        #db_table = 'bills'
        verbose_name_plural = "Bills"

    def __str__(self):
        return self.billingid


class Karigar(models.Model):
    STITCH = "stitch"
    BLOCK = "block"
    EMBROIDER = "emb"
    WASH = "wash"
    ADDON = "addon"
    PROFILE_CHOICES = (
        (STITCH,'Stitch'),
        (BLOCK,'Block'),
        (EMBROIDER,'Embroider'),
        (WASH,'Wash'),
        (ADDON,'Addon'),
    )
    name = models.CharField(primary_key=True, max_length=20)
    profile = models.CharField(max_length=20, choices=PROFILE_CHOICES, null=False, blank=False)
    phone = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    pan = models.CharField(max_length=11, blank=True, null=True)
    #photo = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='karigars/', blank=True, null=True)

    class Meta:
        managed = False
        #db_table = 'karigars'
        verbose_name_plural = "Karigars"

    def __str__(self):
        return self.name


class Product(models.Model):
    prodid = models.CharField(primary_key=True, max_length=100)
    colour = models.CharField(max_length=100, blank=True, null=True)
    fabric = models.CharField(max_length=100, blank=True, null=True)
    #photo = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    cost_stitch = models.IntegerField(blank=True, null=True)
    cost_block = models.IntegerField(blank=True, null=True)
    cost_emb = models.IntegerField(blank=True, null=True)
    cost_wash = models.IntegerField(blank=True, null=True)
    cost_addon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        #db_table = 'products'
        verbose_name_plural = "Products"

    def __str__(self):
        return self.prodid