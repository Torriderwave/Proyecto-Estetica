# Generated by Django 4.1.1 on 2022-09-28 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(max_length=100)),
                ('Hora', models.DateTimeField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cliente')),
                ('Mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mascota')),
            ],
        ),
    ]
