from django.contrib import admin
from my_app.models import player,Booking
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class playerAdmin(BaseUserAdmin):
    list_display=('email', 'name', 'phone','is_admin','is_active')
    search_fields=('email','name')
    readonly_fields=('password','pimg')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','name','phone','password1','password2'),
        }),
    )
    ordering=('name',)

class bookingAdmin(BaseUserAdmin):
    list_display=('p_name','time','date')
    search_fields=('p_name','time','date')
    readonly_fields=('time','date')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('p_name','time','date'),
        }),
    )
    ordering=('p_name',)

admin.site.register(player,playerAdmin)
admin.site.register(Booking,bookingAdmin)