from django.contrib import admin

# Register your models here.

from .models import Post, Author, Tag


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


class TagAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    search_fields = ('title', 'excerpt')
    list_filter = ('date', 'author', 'tags')
    date_hierarchy = 'date'
    filter_horizontal = ('tags',)
    prepopulated_fields = {'slug': ['title']}

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('tags', 'author')
        return queryset


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
