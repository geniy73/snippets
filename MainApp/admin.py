from django.contrib import admin
from MainApp.models import Snippet

# Register your models here.
# 1 variant
#admin.site.register(Snippet)

# 2 variant
@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ["name", "lang", "code", "creation_date"]
    list_filter = ["lang", "creation_date"]
    ordering = ["creation_date"]
    search_fields = ["name", "code"]