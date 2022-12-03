
from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'role')
    search_fields = ('username', )
    list_editable = ('is_active', 'role')


admin.site.register(models.User, UserAdmin)


