# Generated by Django 3.2.7 on 2021-09-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Welder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=60)),
                ('parts_thickness', models.CharField(choices=[('1.4 +', '1.4 +'), ('2.31 - 10.31', '2.31 - 10.31'), ('3 +', '3 +'), ('5 +', '5 +')], max_length=20)),
                ('outer_diameter', models.CharField(choices=[('15 +', '15 +'), ('17.2 +', '17.2 +'), ('21.3 +', '21.3 +'), ('25 +', '25 +'), ('30.15 + +', '30.15 +'), ('79.5 +', '79.5 +'), ('150 +', '150 +')], max_length=20)),
                ('ending_NAX', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeldingPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welding_position', models.CharField(choices=[('Л', 'Л'), ('Н1', 'Н1'), ('Н2', 'Н2'), ('Г', 'Г'), ('В1', 'В1'), ('П1', 'П1'), ('П2', 'П2'), ('Т', 'Т'), ('Н45', 'Н45'), ('Л + Т', 'Л + Т')], max_length=10)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
        migrations.CreateModel(
            name='TypeWelding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_welding', models.CharField(choices=[('ААДП', 'Автоматическая аргонодуговая сварка плавящимся электродом'), ('АЛГ', 'Автоматическая сварка плавящимся электродом в среде активных газов и смесяхных газов и смесях'), ('АФ', 'Автоматическая сварка под флюсом'), ('МАДП', 'Механизированная аргонодуговая сварка плавящимся электродомдом'), ('МП', 'Механизированная сварка плавящимся электродом в среде активных газов и смесяхвных газов и смесях'), ('МПГ', 'Механизированная сварка порошковой проволокой в среде активных газов и смесяхивных газов и смесях'), ('МПС', 'Механизированная сварка самозащитой порошковой проволокой'), ('РАД', 'Ручная аргонодуговая сварка неплавящимся электродом'), ('РД', 'Ручная дуговая сварка покрытыми электродами')], max_length=9)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
        migrations.CreateModel(
            name='TypesMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_material', models.CharField(choices=[('M 01', 'M 01'), ('M 02', 'M 02'), ('M 03', 'M 03'), ('M 05', 'M 05'), ('M 11', 'M 11')], max_length=5)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
        migrations.CreateModel(
            name='TypeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_details', models.CharField(choices=[('Л, Л', 'Л, Л'), ('Т, Т', 'Т, Т'), ('Л,Л + Т,Т', 'Л,Л + Т,Т')], max_length=20)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMaterialWelded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_material_welded', models.CharField(choices=[('СК(1)', 'СК(1)'), ('СК(1,3)', 'СК(1,3)'), ('КО(1,2,5)', 'КО(1,2,5)'), ('ОХНВП(1,2,4,5,8,15,16)', 'ОХНВП(1,2,4,5,8,15,16)'), ('КО(2)', 'КО(2)'), ('ОХНВП(4,8,16),', 'ОХНВП(4,8,16),'), ('ОХНВП(1,2,4,8,16)', 'ОХНВП(1,2,4,8,16)')], max_length=60)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_group', models.CharField(choices=[('ГДО', 'Горнодобывающее оборудование'), ('КСМ', 'Конструкции стальных мостов'), ('ГО', 'Газовое оборудование'), ('МО', 'Металлургическое оборудование'), ('ОТОГ', 'Оборудование для транспортировки опасных грузов'), ('ПТО', 'Подъемно-транспортное оборудование'), ('КО', 'Котельное оборудование'), ('НГДО', 'Нефтегазодобывающее оборудование'), ('ОХНВП', 'Оборудование химических нефтехимических нефтеперерабатывающих и взрывопожароопасных производствающих и взрывопожароопасных производств'), ('СК', 'Строительные конструкции')], max_length=10)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tolerances', models.CharField(choices=[('ААДП', 'Автоматическая аргонодуговая сварка плавящимся электродом'), ('АЛГ', 'Автоматическая сварка плавящимся электродом в среде активных газов и смесяхных газов и смесях'), ('АФ', 'Автоматическая сварка под флюсом'), ('МАДП', 'Механизированная аргонодуговая сварка плавящимся электродомдом'), ('МП', 'Механизированная сварка плавящимся электродом в среде активных газов и смесяхвных газов и смесях'), ('МПГ', 'Механизированная сварка порошковой проволокой в среде активных газов и смесяхивных газов и смесях'), ('МПС', 'Механизированная сварка самозащитой порошковой проволокой'), ('РАД', 'Ручная аргонодуговая сварка неплавящимся электродом'), ('РД', 'Ручная дуговая сварка покрытыми электродами')], max_length=9)),
                ('welder', models.ManyToManyField(to='myparser.Welder')),
            ],
        ),
    ]