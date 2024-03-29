# Generated by Django 4.2.4 on 2023-08-19 12:33

import accounts.authtoken.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthToken",
            fields=[
                (
                    "digest",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("token_key", models.CharField(db_index=True, max_length=15)),
                ("last_use", models.DateTimeField(auto_now=True)),
                (
                    "expiry",
                    models.DateTimeField(default=accounts.authtoken.models.expiry_set),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auth_token_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "authtoken_auth_token",
            },
        ),
        migrations.CreateModel(
            name="AuthTokenInformation",
            fields=[
                (
                    "authToken",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="authtoken.authtoken",
                    ),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True,
                        default="",
                        null=True,
                        verbose_name="The IP address of this session",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user_agent",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=256,
                        verbose_name="HTTP User Agent",
                    ),
                ),
            ],
            options={
                "db_table": "authtoken_auth_token_information",
            },
        ),
    ]
