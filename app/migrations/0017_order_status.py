# Generated by Django 4.2.10 on 2024-03-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0016_order_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("delivered", "Delivered"),
                    ("not_delivered", "Not Delivered"),
                ],
                default="not_delivered",
                max_length=20,
            ),
        ),
    ]
