# Generated by Django 4.2.4 on 2023-08-19 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("exams", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memberexamftquestion",
            name="member_take_exam",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member_take_exam_ftquestions",
                to="exams.membertakeexam",
            ),
        ),
    ]
