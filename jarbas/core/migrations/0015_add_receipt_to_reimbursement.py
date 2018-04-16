# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_add_suspicions_and_probability_to_reimbursements'),
    ]

    operations = [
        migrations.AddField(
            model_name='reimbursement',
            name='receipt_fetched',
            field=models.BooleanField(default=False, verbose_name='Was the receipt URL fetched?'),
        ),
        migrations.AddField(
            model_name='reimbursement',
            name='receipt_url',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='Receipt URL'),
        ),
    ]