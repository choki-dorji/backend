# Generated by Django 4.0.1 on 2022-01-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='project_category',
            field=models.CharField(max_length=10),
        ),
    ]