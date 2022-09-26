from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

@admin.register(Companie)
class CompanieAdmin(ImportExportModelAdmin):
    model = Companie
    list_display = (
        "id",
        "email",
        "name",
    )
    list_filter = (
        "country",
    )


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    model = Product
   
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    model = Service


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(WebToScrape)
class WebToScrapeAdmin(admin.ModelAdmin):
    model = WebToScrape

@admin.register(DraftPost)
class DraftPostAdmin(admin.ModelAdmin):
    model = DraftPost
    list_display = (
        "id",
        "title",
        "sitename",
    )
    list_filter = (
        "sitename",
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "published",
    )
    list_filter = (
        "published",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    save_on_top = True