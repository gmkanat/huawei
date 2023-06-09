# Generated by Django 4.1.3 on 2023-04-15 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_courier_center_id_alter_order_courier_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('otp', models.CharField(max_length=255, verbose_name='OTP')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
            ],
            options={
                'verbose_name': 'OTP',
                'verbose_name_plural': 'OTPs',
            },
        ),
    ]
