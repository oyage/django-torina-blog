# Generated by Django 2.0.4 on 2018-04-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180411_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='commend_uploads/%Y/%m/%d/', verbose_name='ファイル'),
        ),
        migrations.AddField(
            model_name='recomment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='commend_uploads/%Y/%m/%d/', verbose_name='ファイル'),
        ),
    ]