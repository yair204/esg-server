from django.db import migrations

def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('items', 'Category')
    Category.objects.create(name='Electronics')
    Category.objects.create(name='Books')
    Category.objects.create(name='Clothing')
    Category.objects.create(name='Home Appliances')

class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),  # Ensure this depends on the initial migration
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]
