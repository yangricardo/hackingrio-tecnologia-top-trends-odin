# Generated by Django 2.0.7 on 2018-07-28 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DonatedBeneficiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_doado_ao_beneficiario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beneficiario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='donation.Beneficiary')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_doado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(auto_now=True)),
                ('doado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='donatedbeneficiary',
            name='doacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='donation.Donation'),
        ),
    ]
