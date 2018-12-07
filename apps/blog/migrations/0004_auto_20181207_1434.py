# Generated by Django 2.1.2 on 2018-12-07 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181207_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '攻略对应标签', 'verbose_name_plural': '攻略对应标签'},
        ),
        migrations.AlterModelOptions(
            name='strategyarticle',
            options={'verbose_name': '攻略文章', 'verbose_name_plural': '攻略文章'},
        ),
        migrations.AlterModelOptions(
            name='strategyclass',
            options={'verbose_name': '攻略主题', 'verbose_name_plural': '攻略主题'},
        ),
        migrations.AddField(
            model_name='strategyarticle',
            name='strategyClass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.StrategyClass', verbose_name='所属主题'),
        ),
    ]
