# Generated by Django 5.0 on 2023-12-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_onetimepassword"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="auth_provider",
            field=models.CharField(default="email", max_length=50),
        ),
    ]
