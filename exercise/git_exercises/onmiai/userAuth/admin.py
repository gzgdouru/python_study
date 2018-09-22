from django.contrib import admin
from .models import Boy, Girl, B2G

class BoyAdmin(admin.ModelAdmin):
    list_display = ["nickname"]

class GirlAdmin(admin.ModelAdmin):
    list_display = ["nickname"]

# Register your models here.
admin.site.register(Boy, BoyAdmin)
admin.site.register(Girl, GirlAdmin)
admin.site.register(B2G)