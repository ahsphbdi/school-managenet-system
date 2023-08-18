# Generated by Django 4.2.4 on 2023-08-17 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("exams", "0007_alter_ftquestion_created_datetime_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ftquestion",
            name="exam",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ftquestions",
                to="exams.exam",
            ),
        ),
    ]
