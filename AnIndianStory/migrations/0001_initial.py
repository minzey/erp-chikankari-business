# Generated by Django 3.2.5 on 2021-07-26 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Karigar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('profile', models.CharField(choices=[('stitch', 'Stitch'), ('block', 'Block'), ('emb', 'Embroider'), ('wash', 'Wash'), ('addon', 'Addon'), ('finish', 'Finish')], max_length=20)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('pan', models.CharField(blank=True, max_length=11, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='karigars/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodid', models.CharField(max_length=100)),
                ('colour', models.CharField(blank=True, max_length=100, null=True)),
                ('fabric', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('cost_stitch', models.IntegerField(blank=True, null=True)),
                ('cost_block', models.IntegerField(blank=True, null=True)),
                ('cost_emb', models.IntegerField(blank=True, null=True)),
                ('cost_wash', models.IntegerField(blank=True, null=True)),
                ('cost_addon', models.IntegerField(blank=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AnIndianStory.company')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billingid', models.IntegerField()),
                ('billingdate', models.DateField(blank=True, null=True)),
                ('amountpaid', models.IntegerField(blank=True, null=True)),
                ('karigar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnIndianStory.karigar')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('challanid', models.CharField(max_length=255)),
                ('process', models.CharField(max_length=10)),
                ('size', models.CharField(choices=[('--', '--'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='--', max_length=10)),
                ('qty', models.IntegerField(default=0)),
                ('assignmentdate', models.DateField()),
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('karigar', models.ForeignKey(db_column='karigar', on_delete=django.db.models.deletion.DO_NOTHING, to='AnIndianStory.karigar')),
                ('product', models.ForeignKey(db_column='product', on_delete=django.db.models.deletion.DO_NOTHING, to='AnIndianStory.product')),
            ],
            options={
                'verbose_name_plural': 'Assignments',
                'unique_together': {('challanid', 'process', 'karigar', 'product', 'size')},
            },
        ),
    ]
