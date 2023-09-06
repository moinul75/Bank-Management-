# Generated by Django 4.2.4 on 2023-09-06 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_balence',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, max_length=20),
        ),
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fullname', models.CharField(max_length=255)),
                ('profile_image', models.ImageField(default='defaults.png', upload_to='profile_pic')),
                ('marital_status', models.CharField(choices=[('married', 'Married'), ('single', 'Single'), ('others', 'Others')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10)),
                ('identity_type', models.CharField(choices=[('national_id_card', 'National_id_card'), ('driving_licence', 'Driving_licence'), ('international_passport', 'International_passport')], max_length=100)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=20)),
                ('signature', models.ImageField(upload_to='signature')),
                ('fax', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
