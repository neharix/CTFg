from django.contrib import admin

from .models import Answer, Challenge, HashResponse, Hint, Quizz, TrueAnswers

# Register your models here.


class siteAdmin(admin.ModelAdmin):
    readonly_fields = ("id",)


class answerAdmin(admin.ModelAdmin):
    readonly_fields = ("answered_at",)


admin.site.register(Challenge, siteAdmin)
admin.site.register(Hint, siteAdmin)
admin.site.register(Quizz, siteAdmin)
admin.site.register(Answer, answerAdmin)
admin.site.register(TrueAnswers)
admin.site.register(HashResponse)
# class NoteAdmin(admin.ModelAdmin):
#     list_filter = ('day_created',)
#     list_display = ('name', 'day_created', 'date_start', 'date_end', 'description')
# admin.site.register(Challenge)
