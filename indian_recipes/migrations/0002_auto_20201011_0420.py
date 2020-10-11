# Generated by Django 3.1.1 on 2020-10-11 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indian_recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.ManyToManyField(blank=True, to='indian_recipes.Direction'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='indian_recipes.Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='indian_recipes.category'),
        ),
    ]