from polls.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Represent the Poll Admin Page
class PollAdmin(admin.ModelAdmin):
    # Fields shown is a poll detail
    fieldsets = [(None, {'fields':['question']}), ('Date Information', {'fields':['pub_date'], 'classes':['collapse']})]
    # Show a post of choirces
    inlines = [ChoiceInline]

    # Attributes displayed in the list
    list_display = ('question', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
