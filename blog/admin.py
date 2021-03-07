from django.contrib import admin
from.models import blog
from.models import Profile,news
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','author','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(blog,PostAdmin)
admin.site.register(Profile)
admin.site.register(news)
