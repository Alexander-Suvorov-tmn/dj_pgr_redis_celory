from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Welder)
admin.site.register(Tolerances)
admin.site.register(TypeWelding)
admin.site.register(TypeDetails)
admin.site.register(TypesMaterial)
admin.site.register(DeviceGroup)
admin.site.register(GroupMaterialWelded)
admin.site.register(File)
