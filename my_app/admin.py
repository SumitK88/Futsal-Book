from django.contrib import admin
from my_app.models import player,Booking
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
class playerAdmin(BaseUserAdmin):
    list_display=('email', 'name', 'phone','is_admin','is_active')
    search_fields=('email','name')
    readonly_fields=('password',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email','name','phone','pimg','password1','password2'),
        }),
    )
    ordering=('name',)

class bookingAdmin(BaseUserAdmin):
    list_display=('bokked_d','player','time','date')
    search_fields=('time','date','player__name','bokked_d')
    readonly_fields=('time','date')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('bokked_d','player','time','date'),
        }),
    )
    ordering=('bokked_d',)

admin.site.register(player,playerAdmin)
admin.site.register(Booking,bookingAdmin)