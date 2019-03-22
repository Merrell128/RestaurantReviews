from django.contrib import admin
from rango.models import Category, Page, Review
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = {'slug':('name',)}


class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'address')
	prepopulated_fields = {'slug':('title',)}
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Review)
admin.site.register(UserProfile)