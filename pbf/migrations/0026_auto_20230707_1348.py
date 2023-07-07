# Generated by Django 4.0.1 on 2023-07-07 13:48

from django.db import migrations

def add_waters_cards(apps, schema_editor):
    Card = apps.get_model("pbf", "Card")
    Card(name="Waters Renew", cost=0, type=3).save()
    Card(name="Serene Waters", cost=0, type=3).save()
    Card(name="Roiling Waters", cost=0, type=3).save()
    Card(name="Waters Taste of Ruin", cost=0, type=3).save()

def delete_waters_cards(apps, schema_editor):
    Card = apps.get_model("pbf", "Card")
    Card.objects.get(name="Waters Renew").delete()
    Card.objects.get(name="Serene Waters").delete()
    Card.objects.get(name="Roiling Waters").delete()
    Card.objects.get(name="Waters Taste of Ruin").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('pbf', '0025_fix_costs'),
    ]

    operations = [
        migrations.RunPython(add_waters_cards, delete_waters_cards),
    ]
