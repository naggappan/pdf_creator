from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Document, DocType, DocValue

class DocValueAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_type', 'place', 'ar_no')
    list_filter = ('doc_name', 'doc_type')


admin.site.register(Document)
admin.site.register(DocType)
admin.site.register(DocValue, DocValueAdmin)
