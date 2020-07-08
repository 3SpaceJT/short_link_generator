from django.contrib import admin

from links_app.models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ("short_url", "long_url")


admin.site.register(Link, LinkAdmin)
