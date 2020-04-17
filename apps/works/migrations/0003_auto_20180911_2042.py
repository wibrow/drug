# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import works.models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_auto_20180907_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admet',
            name='mol_file',
            field=models.FileField(upload_to='media/admet/%Y/%m/%d/', verbose_name='\u5c0f\u5206\u5b50\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='autoduck',
            name='pdb_file',
            field=models.FileField(upload_to=works.models.upload_to, verbose_name='pdb\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='media/banner/', verbose_name='\u8f6e\u64ad\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='frcmod_file',
            field=models.FileField(default='', upload_to='media/dynamic/%Y/%m/%d/', verbose_name='frcmod\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='lig_file',
            field=models.FileField(default='', upload_to='media/dynamic/%Y/%m/%d/', verbose_name='lig\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='mol_file',
            field=models.FileField(upload_to='media/dynamic/%Y/%m/%d/', verbose_name='\u5c0f\u5206\u5b50\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='protein_file',
            field=models.FileField(upload_to='media/dynamic/%Y/%m/%d/', verbose_name='\u86cb\u767d\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='s_file',
            field=models.FileField(default='', upload_to='media/dynamic/%Y/%m/%d/', verbose_name='S\u4fe1\u606f\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='reversevirtualscreen',
            name='mol_file',
            field=models.FileField(upload_to='media/reversevirtualscreen/%Y/%m/%d/', verbose_name='\u9776\u70b9\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='virtualscreen',
            name='pdb_file',
            field=models.FileField(upload_to='media/virtualscreen/%Y/%m/%d/', verbose_name='pdb\u6587\u4ef6'),
        ),
    ]
