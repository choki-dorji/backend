# Generated by Django 4.0.1 on 2022-01-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_projectdetail_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetail',
            name='project_category',
            field=models.TextField(),
        ),
    ]