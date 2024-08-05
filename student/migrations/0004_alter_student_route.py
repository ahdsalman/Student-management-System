# Generated by Django 5.0.4 on 2024-08-03 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolbus", "0001_initial"),
        ("student", "0003_student_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="route",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to="schoolbus.route",
            ),
        ),
    ]
