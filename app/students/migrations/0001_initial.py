# Generated by Django 4.2.4 on 2023-08-27 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0002_user_created_at_user_deleted_at_user_is_deleted_and_more"),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
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
            options={
                "abstract": False,
            },
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
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
                "db_table": "students_financial_aids",
                "db_table_comment": "It shows the student's financial aids in the course",
            },
        ),
        migrations.AddConstraint(
            model_name="financialaids",
            constraint=models.UniqueConstraint(
                fields=("student", "course"), name="unique_student_course"
            ),
        ),
    ]
