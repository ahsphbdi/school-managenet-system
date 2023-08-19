# Generated by Django 4.2.4 on 2023-08-19 09:52

import core.db.mixins.timestamp
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="student_user",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("school", models.CharField(blank=True, max_length=300)),
                ("degree", models.PositiveSmallIntegerField(blank=True, default=0)),
                ("field", models.CharField(blank=True, max_length=200)),
            ],
            bases=(core.db.mixins.timestamp.TimeStampMixin, models.Model),
        ),
        migrations.CreateModel(
            name="FinancialAids",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("applying_reason", models.TextField()),
                ("annual_income", models.PositiveBigIntegerField()),
                ("ability_to_pay", models.PositiveBigIntegerField()),
                ("result", models.TextField()),
                ("is_accepted", models.BooleanField(default=False)),
                ("reviewed", models.BooleanField(default=False)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="financial_aids",
                        to="students.student",
                    ),
                ),
            ],
            options={
                "db_table": "students_student_enroll",
                "db_table_comment": "It shows the student's enrollment in the course",
            },
            bases=(core.db.mixins.timestamp.TimeStampMixin, models.Model),
        ),
        migrations.AddConstraint(
            model_name="financialaids",
            constraint=models.UniqueConstraint(
                fields=("student", "course"), name="unique_student_course"
            ),
        ),
    ]
