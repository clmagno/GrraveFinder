# Generated by Django 4.2.1 on 2023-05-31 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_rename_slot_reservation_lot_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="Lot_Id",
            new_name="Lot",
        ),
    ]
