# Generated by Django 4.1.7 on 2023-02-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksapi', '0002_task_user_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finish_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
