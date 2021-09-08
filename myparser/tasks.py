from celery import shared_task
from myproject.celery import celery_app
from .models import *

import openpyxl
import os

@celery_app.task
def adding_task(file_path):
    
    try:
        ad =os.path.abspath(file_path)
        print(ad)
        book = openpyxl.open("book.xlsx", read_only=True)
        sheet = book.active
        for row in range(2, sheet.max_row + 1):
            #добавляем клеймо в основную модель
            brand = sheet[row][0].value
            print(brand)
            b = Welder(brand=brand)
            b.save()

            # добавляем вид сварки
            type_welding = sheet[row][1].value
            welding = type_welding.split()
            if len(welding) > 1:
                for i in welding:
                    t__welding = Tolerances(type_welding=i)
                    t__welding.save()
                    t__welding.wolder.add(b)

            # добавляем вид деталей
            type_details = sheet[row][2].value
            detail = type_details.split()
            if len(detail) > 1:
                for i in detail:
                    t__details = Tolerances(type_details=i)
                    t__details.save()

            
            #группа свариваемого материала
            group_material_welded = sheet[row][3].value
            material_welded = group_material_welded.split()
            if len(material_welded) > 1:
                for i in material_welded:
                    mat_welded = GroupMaterialWelded(group_material_welded=i)
                    mat_welded.save()

            #добавляем толщину деталей
            thickness_parts = sheet[row][4].value
            t_parts = thickness_parts.split()
            if len(t_parts) > 1:
                for i in t_parts:
                    th_parts = Welder(thickness_parts=i)
                    th_parts.save()

            # добавляем наружный диаметр
            outer_diameter = sheet[row][5].value
            b = Welder(outer_diameter=outer_diameter)
            b.save()

            # добавляем тип материала, положение при сварке
            type_material_welding_position = sheet[row][6].value
            a = type_material_welding_position.split(';')
            b = [x.replace(' ', '') for x in a]
            for i in range(len(b)):
                ls = [b[i]]
                e = ':'.join(ls)
                e = e.split(':')
                ty_material = e[0]
                wel_position = e[1]
                typ_material = TypesMaterial(types_material=ty_material)
                w_position = WeldingPosition(welding_position=wel_position)
                typ_material.save()
                w_position.save()

            # добавляем группы устройств
            device_groups = sheet[row][7].value
            d_group= device_groups.split()
            if len(d_group) > 1:
                for i in d_group:
                    dev_group = DeviceGroup(device_group=i)
                    dev_group.save()
                    dev_group.wolder.add(b)

            # окончание НАКС
            # ending_NAX =  sheet[row][8].value
            # e_NAX = Welder(outer_diameter=outer_diameter)
            # b.save()
        print('ДАННЫЕ ЗАГРУЖЕНЫ В БД')
    except IOError as e:
        print("Произошла ошибка загрузки данных в БД")
