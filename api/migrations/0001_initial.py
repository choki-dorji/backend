# Generated by Django 4.0 on 2022-01-18 11:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_name', models.TextField()),
                ('project_category', models.TextField()),
                ('project_cost', models.IntegerField()),
                ('project_duration', models.IntegerField()),
                ('Owner', models.TextField()),
                ('person_in_charge', models.TextField()),
                ('Date_from', models.TextField()),
                ('Date_to', models.TextField()),
                ('status', models.IntegerField()),
                ('previlage', models.IntegerField()),
                ('pyoject_type', models.ImageField(upload_to='')),
            ],
        ),
    ]
