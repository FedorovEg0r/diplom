# Generated by Django 4.1.7 on 2024-05-27 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("saite", "0006_delete_parser"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("telegram_auth", "0009_alter_parsersetting_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="parsersetting",
            name="excludes",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="parsersetting",
            name="groups",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="parsersetting",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="saite.city",
            ),
        ),
        migrations.AlterField(
            model_name="parsersetting",
            name="keywords",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="parsersetting",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
