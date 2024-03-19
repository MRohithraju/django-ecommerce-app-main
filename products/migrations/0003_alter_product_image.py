

from django.db import migrations, models
import products.models
import products.storage


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=products.models.get_default_image, storage=products.storage.OverriteFile(), upload_to=''),
        ),
    ]
