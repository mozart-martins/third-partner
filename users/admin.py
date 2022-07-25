from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CoworkerModel


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'name_pj', 'name_coworker')
    ordering = ('-start_date',)
    list_filter = ('name_coworker', 'user_name',
                   'email', 'is_active', 'is_staff')
    list_display = ('name_pj', 'name_coworker', 'email', 'phone_number',
                    'is_active', 'is_staff')

    # Campos que aparecerão quando clicarmos num usuário no djangoadmin para alteração do mesmo
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'name_coworker', 'cnpj')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),

    )

    formfield_overrides = {
        CoworkerModel.about: {'widget': forms.Textarea(attrs={'rows': 10, 'cols': 40})},
        CoworkerModel.cnpj: {'widget': forms.TextInput(attrs={'rows': 10, 'cols': 40})},

    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'name_coworker', 'cnpj', 'about', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(CoworkerModel, UserAdminConfig)
