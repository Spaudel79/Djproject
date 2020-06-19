from django.contrib import admin
from .models import Blog, Club, Players, MainMenu, SubMenu, BlogCricket, BlogNBA,BlogTennis,BlogEPL,BlogChampionsLeague,BlogLaLiga,BlogSerieA
from django.utils.html import format_html

# Register your models here.

@admin.register(MainMenu)
class AdminMainMenu(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(SubMenu)
class AdminSubMenu(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    search_fields = ['title','status']
    list_display = ['title', 'show_image', 'status']
    actions = ['active', 'inactive']
    list_per_page = 5
    ordering = ['title']
    date_hierarchy = 'created_at'

    def show_image(self, obj):
        return format_html('<img src="{}" width="30">', format(obj.image.url))

    def active(self,request,queryset):
        queryset.update(status=True)

    def inactive(self, request, queryset):
        queryset.update(status=False)


@admin.register(BlogCricket)
class BlogCricket(admin.ModelAdmin):
    search_fields = ['title','status']
    list_display = ['title', 'show_image', 'status']
    actions = ['active', 'inactive']
    list_per_page = 5
    ordering = ['title']
    date_hierarchy = 'created_at'

    def show_image(self, obj):
        return format_html('<img src="{}" width="30">', format(obj.image.url))

    def active(self,request,queryset):
        queryset.update(status=True)

    def inactive(self, request, queryset):
        queryset.update(status=False)


@admin.register(BlogNBA)
class BlogNBA(admin.ModelAdmin):
    search_fields = ['title','status']
    list_display = ['title', 'show_image', 'status']
    actions = ['active', 'inactive']
    list_per_page = 5
    ordering = ['title']
    date_hierarchy = 'created_at'

    def show_image(self, obj):
        return format_html('<img src="{}" width="30">', format(obj.image.url))

    def active(self,request,queryset):
        queryset.update(status=True)

    def inactive(self, request, queryset):
        queryset.update(status=False)



@admin.register(BlogTennis)
class BlogTennis(admin.ModelAdmin):
    search_fields = ['title','status']
    list_display = ['title', 'show_image', 'status']
    actions = ['active', 'inactive']
    list_per_page = 5
    ordering = ['title']
    date_hierarchy = 'created_at'

    def show_image(self, obj):
        return format_html('<img src="{}" width="30">', format(obj.image.url))

    def active(self,request,queryset):
        queryset.update(status=True)

    def inactive(self, request, queryset):
        queryset.update(status=False)


@admin.register(BlogEPL)
class BlogEPL(admin.ModelAdmin):
    pass


@admin.register(BlogLaLiga)
class BlogLaLiga(admin.ModelAdmin):
    pass



@admin.register(BlogSerieA)
class BlogSerieA(admin.ModelAdmin):
    pass



@admin.register(BlogChampionsLeague)
class BlogChampionsLeague(admin.ModelAdmin):
    pass



@admin.register(Club)
class AdminClub(admin.ModelAdmin):
    pass

@admin.register(Players)
class AdminClub(admin.ModelAdmin):
    pass