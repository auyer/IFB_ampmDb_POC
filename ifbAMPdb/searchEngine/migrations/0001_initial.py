# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='peptide',
            fields=[
                ('pdb_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('is_amp', models.BooleanField()),
                ('hfobic_area', models.CharField(max_length=96)),
                ('hfobic_avg', models.FloatField()),
                ('hairpin', models.BooleanField()),
                ('beta_sheet', models.BooleanField()),
                ('alpha_helix', models.BooleanField()),
                ('alpha_helix_beta_sheet', models.BooleanField()),
                ('alpha_helix_beta_sheet_hairpin', models.BooleanField()),
                ('charge', models.FloatField()),
                ('m_dipol', models.FloatField()),
                ('charge_amt_atm', models.FloatField()),
                ('m_dipol_amt_atm', models.FloatField()),
                ('sequence', models.TextField(blank=True, null=True)),
                ('organism', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]