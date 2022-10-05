from django.contrib import admin
from .models import Cliente,Mascota,Citas,Login,Producto

# Register your models here.

admin.site.register(Login)
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Citas)
admin.site.register(Producto)
