from django.contrib import admin
from . models import (
    Blogs,
    Reviews,
    Contact,
)

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Reviews)
class reviewAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_active')
    readonly_fields = ('slug',)  

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name')
    
