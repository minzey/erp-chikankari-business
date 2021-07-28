# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

import json

from django.db import models


class Assignment(models.Model):
    XS="XS"
    S="S"
    M="M"
    L="L"
    XL="XL"
    XXL="XXL"
    DEFAULT="--"
    challanid = models.CharField(max_length=255,null=False,blank=False)
    process = models.CharField(max_length=10, null=False, blank=False)
    karigar = models.ForeignKey('Karigar', models.DO_NOTHING, db_column='karigar')
    product = models.ForeignKey('Product', models.DO_NOTHING, db_column='product')
    SIZE_CHOICES = (
        (DEFAULT, '--'),
        (XS, 'XS'),
        (S, 'S'),
        (M, 'M'),
        (L, 'L'),
        (XL, 'XL'),
        (XXL, 'XXL'),
    )
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default="--")
    qty = models.IntegerField(default=0)
    assignmentdate = models.DateField(null=False, blank=False)
    assignment_id = models.AutoField(primary_key=True)

    class Meta:
        unique_together = (('challanid', 'process','karigar','product', 'size'),)
        verbose_name_plural = "Assignments"

    def __str__(self):
        return str(self.challanid)

class Bill(models.Model):
    billingid = models.IntegerField(null=False)
    karigar = models.ForeignKey(to='Karigar', on_delete=models.CASCADE, null=False)
    billingdate = models.DateField(blank=True, null=True)
    amountpaid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.billingid)

class Company(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.name


class Karigar(models.Model):
    STITCH = "stitch"
    BLOCK = "block"
    EMBROIDER = "emb"
    WASH = "wash"
    ADDON = "addon"
    FINISH = "finish"
    PROFILE_CHOICES = (
        (STITCH,'Stitch'),
        (BLOCK,'Block'),
        (EMBROIDER,'Embroider'),
        (WASH,'Wash'),
        (ADDON,'Addon'),
        (FINISH, 'Finish'),
    )
    name = models.CharField(max_length=40)
    profile = models.CharField(max_length=20, choices=PROFILE_CHOICES, null=False, blank=False)
    phone = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    pan = models.CharField(max_length=11, blank=True, null=True)
    photo = models.ImageField(upload_to='karigars/', blank=True, null=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.id, self.__str__()


class Product(models.Model):
    prodid = models.CharField(max_length=100, null=False, blank=False)
    colour = models.CharField(max_length=100, blank=True, null=True)
    fabric = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='products/', blank=True, null=True)
    company = models.ForeignKey(to=Company, on_delete=models.SET_NULL, null=True)
    cost_stitch = models.IntegerField(blank=True, null=True)
    cost_block = models.IntegerField(blank=True, null=True)
    cost_emb = models.IntegerField(blank=True, null=True)
    cost_wash = models.IntegerField(blank=True, null=True)
    cost_addon = models.IntegerField(blank=True, null=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.prodid

    def natural_key(self):
        return self.id, self.__str__()

    class Meta:
        unique_together = (('prodid', 'company'),)