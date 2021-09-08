from django.db import models

# Create your models here.
#сварщик
class Welder(models.Model):
    PART_THICKNESS = (
        ('1.4 +', '1.4 +'),
        ('2.31 - 10.31', '2.31 - 10.31'),
        ('3 +', '3 +'),
        ('5 +', '5 +'),
    )
    OUTER_DIAMETER = (
        ('15 +', '15 +'),
        ('17.2 +', '17.2 +'),
        ('21.3 +', '21.3 +'),
        ('25 +', '25 +'),
        ('30.15 + +', '30.15 +'),
        ('79.5 +', '79.5 +'),
        ('150 +', '150 +'),
    )
    brand = models.CharField(max_length=60)
    parts_thickness = models.CharField(max_length=20, choices=PART_THICKNESS)
    outer_diameter = models.CharField(max_length=20, choices=OUTER_DIAMETER)
    ending_NAX = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['brand']

    def __str__(self):
        return self.brand


#допущен к
class Tolerances(models.Model):
    TOLERANCES = (
        ('ААДП', 'Автоматическая аргонодуговая сварка плавящимся электродом'),
        ('АЛГ', 'Автоматическая сварка плавящимся электродом в среде активных газов и смесяхных газов и смесях'),
        ('АФ', 'Автоматическая сварка под флюсом'),
        ('МАДП', 'Механизированная аргонодуговая сварка плавящимся электродомдом'),
        ('МП', 'Механизированная сварка плавящимся электродом в среде активных газов и смесяхвных газов и смесях'),
        ('МПГ', 'Механизированная сварка порошковой проволокой в среде активных газов и смесяхивных газов и смесях'),
        ('МПС', 'Механизированная сварка самозащитой порошковой проволокой'),
        ('РАД', 'Ручная аргонодуговая сварка неплавящимся электродом'),
        ('РД', 'Ручная дуговая сварка покрытыми электродами'),
    )
    tolerances = models.CharField(max_length=9, choices=TOLERANCES)
    welder = models.ManyToManyField(Welder)

    class Meta:
        ordering = ['tolerances']


#виды сварок - справочник
class TypeWelding(models.Model):
    TYPE_WELDING = (
        ('ААДП', 'Автоматическая аргонодуговая сварка плавящимся электродом'),
        ('АЛГ', 'Автоматическая сварка плавящимся электродом в среде активных газов и смесяхных газов и смесях'),
        ('АФ', 'Автоматическая сварка под флюсом'),
        ('МАДП', 'Механизированная аргонодуговая сварка плавящимся электродомдом'),
        ('МП', 'Механизированная сварка плавящимся электродом в среде активных газов и смесяхвных газов и смесях'),
        ('МПГ', 'Механизированная сварка порошковой проволокой в среде активных газов и смесяхивных газов и смесях'),
        ('МПС', 'Механизированная сварка самозащитой порошковой проволокой'),
        ('РАД', 'Ручная аргонодуговая сварка неплавящимся электродом'),
        ('РД', 'Ручная дуговая сварка покрытыми электродами'),
    )
    type_welding = models.CharField(max_length=9, choices=TYPE_WELDING)
    welder = models.ForeignKey(Welder, on_delete=models.CASCADE)
    

#виды деталей - справочник
class TypeDetails(models.Model):
    TYPE_DETAILS = (
        ('Л, Л', 'Л, Л'),
        ('Т, Т', 'Т, Т'),
        ('Л,Л + Т,Т', 'Л,Л + Т,Т'),
    )
    type_details = models.CharField(max_length=20, choices=TYPE_DETAILS)
    welder = models.ForeignKey(Welder, on_delete=models.CASCADE)


#тип материала - справочник
class TypesMaterial(models.Model):
    # TYPES_MATERIAL = (
    #     ('M 01', 'M 01'),
    #     ('M 02', 'M 02'),
    #     ('M 03', 'M 03'),
    #     ('M 05', 'M 05'),
    #     ('M 11', 'M 11'),
    # )
    types_material = models.CharField(max_length=10)
    welder = models.ForeignKey(Welder, on_delete=models.CASCADE)

#положение при сварке - справочник
class WeldingPosition(models.Model):

    welding_position = models.CharField(max_length=10)
    welder = models.ForeignKey(Welder, on_delete=models.CASCADE)


#группа устройств
class DeviceGroup(models.Model):
    DEVICE_GROUP = (
        ('ГДО', 'Горнодобывающее оборудование'),
        ('КСМ', 'Конструкции стальных мостов'),
        ('ГО', 'Газовое оборудование'),
        ('МО', 'Металлургическое оборудование'),
        ('ОТОГ', 'Оборудование для транспортировки опасных грузов'),
        ('ПТО', 'Подъемно-транспортное оборудование'),
        ('КО', 'Котельное оборудование'),
        ('НГДО', 'Нефтегазодобывающее оборудование'),
        ('ОХНВП', 'Оборудование химических нефтехимических нефтеперерабатывающих и взрывопожароопасных производствающих и взрывопожароопасных производств'),
        ('СК', 'Строительные конструкции'),
    )
    device_group = models.CharField(max_length=10, choices=DEVICE_GROUP)
    welder = models.ManyToManyField(Welder)

    class Meta:
        ordering = ['device_group']


#группа свариваемого материала
class GroupMaterialWelded(models.Model):
    GROUP_MATERIAL_WELDED = (
        ('M 01', 'M 01'),
        ('M 02', 'M 02'),
        ('M 03', 'M 03'),
        ('M 05', 'M 05'),
        ('M 11', 'M 11'),
    )
    group_material_welded = models.CharField(max_length=60, choices=GROUP_MATERIAL_WELDED)
    welder = models.ForeignKey(Welder, on_delete=models.CASCADE)

class File(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='files/%Y-%m-%d/')

    def __str__(self):
        return self.title
