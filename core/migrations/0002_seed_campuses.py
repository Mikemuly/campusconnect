"""
Data migration: seeds the Campus table with sample universities.
"""
from django.db import migrations


def seed_campuses(apps, schema_editor):
    Campus = apps.get_model('core', 'Campus')
    campuses = [
        ('University of Nairobi', 'Nairobi, Kenya'),
        ('Technical University of Mombasa', 'Mombasa, Kenya'),
        ('Kenyatta University', 'Nairobi, Kenya'),
        ('University of Eldoret', 'Eldoret, Kenya'),
        ('Jomo Kenyatta University of Agriculture and Technology', 'Nairobi, Kenya'),
        ('Masinde Muliro University of Science and Technology', 'Kakamega, Kenya'),
        ('Masinde Muliro University of Science and Technology', 'Kakamega, Kenya'),
        ('Dedan Kimathi University of Technology', 'Nyeri, Kenya'),
        ('Chuka University', 'Chuka, Kenya'),
        ('Pwani University', 'Kilifi, Kenya'),
        ('Kisii University', 'Kisii, Kenya'),
        ('Masaai Mara University', 'Narok, Kenya'),
        ('Jaramogi Oginga Odinga University of Science and Technology', 'Bondo, Kenya'),
        ('Laikipia University', 'Nanyuki, Kenya'),
        ('Meru University of Science and Technology', 'Meru, Kenya'),
        ('South Eastern Kenya University', 'Kitui, Kenya'),
        ('University of Kabianga', 'Kericho, Kenya'),
        ('Karatina University', 'Karatina, Kenya'),
        ('Kibabii University', 'Bungoma, Kenya'),
        ('Rongo University', 'Rongo, Kenya'),
        ('University of Embu', 'Embu, Kenya'),
        ('The Cooperative University of Kenya', 'Nairobi, Kenya'),
        ('Taita Taveta University', 'Taita Taveta, Kenya'),
        ('Murang’a University of Technology', 'Murang’a, Kenya'),
        ('Machakos University', 'Machakos, Kenya'),
        ('Kirinyaga University', 'Kigumo, Kenya'),
        ('Garissa University', 'Garissa, Kenya'),
        ('Alupe University', 'Busia, Kenya'),
        ('Kaimosi Friends University', 'Kaimosi, Kenya'),
        ('Tom Mboya University College', 'Kisumu, Kenya'),
        ('Tharaka University', 'Tharaka Nithi, Kenya'),
        ('Bomet University College', 'Bomet, Kenya'),
        ('Strathmore University', 'Nairobi, Kenya'),
        ('USIU Africa', 'Nairobi, Kenya'),
        ('Daystar University', 'Nairobi, Kenya'),
        ('Moi University', 'Eldoret, Kenya'),
        ('Egerton University', 'Nakuru, Kenya'),
        ('Maseno University', 'Kisumu, Kenya'),
        ('Makerere University', 'Kampala, Uganda'),
        ('Technical University of Kenya', 'Nairobi, Kenya'),
        ('Multimedia University of Kenya', 'Nairobi, Kenya'),
        ('Turkana University', 'Turkana, Kenya'),
        ('Makueni University', 'Makueni, Kenya'),
    ]
    for name, location in campuses:
        Campus.objects.get_or_create(name=name, defaults={'location': location})


def unseed_campuses(apps, schema_editor):
    pass  # No rollback needed for seed data


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_campuses, unseed_campuses),
    ]
