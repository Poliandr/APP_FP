# Generated by Django 5.0.3 on 2024-03-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notes",
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
                ("title", models.CharField(max_length=50, verbose_name="Название")),
                (
                    "description",
                    models.CharField(max_length=250, verbose_name="Описание"),
                ),
                ("full_text", models.TextField(verbose_name="Заметка")),
                ("date", models.DateTimeField(verbose_name="Дата публикации")),
            ],
        ),
    ]
