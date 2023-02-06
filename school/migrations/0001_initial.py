# Generated by Django 4.1.6 on 2023-02-06 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StudentRegisteration",
            fields=[
                ("Student_id", models.AutoField(primary_key=True, serialize=False)),
                ("Student_first_name", models.CharField(max_length=100)),
                ("Student_last_name", models.CharField(max_length=100)),
                ("Student_age", models.IntegerField()),
                ("Student_mail", models.EmailField(max_length=254)),
                ("Student_exam_pass", models.BooleanField()),
            ],
        ),
    ]