from django.contrib import admin
from loco_app.models import *


#Admins can have
#   list_filter 
#   filter_horizontal for manytomanyfields


class AboAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "bezieher"]
    filter_horizontal = ["users"]
    search_fields = ["users__username", "users__first_name", "users__last_name"]


class HistoryAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "action", "fm", "to"]
    readonly_fields = ["timestamp", "action", "fm", "to"]
    #can_delete = False


admin.site.register(Depot)
admin.site.register(AboType)
admin.site.register(ExtraAboType)
admin.site.register(Abo, AboAdmin)
admin.site.register(Loco)
admin.site.register(abo_user_audit, HistoryAdmin)
admin.site.register(extraabo_audit, HistoryAdmin)

