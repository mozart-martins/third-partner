# Generated by Django 4.0.6 on 2022-07-20 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_workedhours_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workedhours",
            old_name="worker_id_id",
            new_name="worker",
        ),
    ]