from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer


class CustomerAdmin(UserAdmin):
    model = Customer
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone_number",)}),
    )


admin.site.register(Customer, CustomerAdmin)