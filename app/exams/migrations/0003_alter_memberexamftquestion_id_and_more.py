# Generated by Django 4.2.4 on 2023-08-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exams", "0002_alter_exam_deleted_at_alter_ftquestion_deleted_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memberexamftquestion",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="membertakeexam",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
