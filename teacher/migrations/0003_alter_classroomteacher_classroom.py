# Generated by Django 5.0.4 on 2024-05-17 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_classroomteacher_classroom_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomteacher',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_teachers', to='teacher.classroom'),
        ),
    ]
