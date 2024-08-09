from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class ChangeUserAdmin(admin.ModelAdmin):  
    search_fields = ('username', 'email', 'first_name', 'last_name') 
    list_filter = ('gender', 'is_staff', 'is_superuser', 'is_active') 
    ordering = ['username']  
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',]  
    fieldsets = (  
        (None,  
         {  
            'fields': (  
                'username',   
                'password',  
            ),
         }),  
        ('Personal info',   
         {  
            'fields': (  
                'first_name',   
                'last_name',  
                'email',  
                'gender',  
                'age',       
                'description'   
            ),  
        }),  
        ('Contact info',   
         {  
            'fields': (  
                'phone',   
                'address',  
            ),   
        }),  
        ('Permissions', {  
            "fields": (  
                "is_active",  
                "is_staff",  
                "is_superuser",  
                "groups",  
                "user_permissions",  
            ),  
        }),  
        ('Important dates', {"fields": ("last_login", "date_joined")}),  
    )  
    filter_horizontal = ('groups', 'user_permissions')
admin.site.register(User, ChangeUserAdmin)

