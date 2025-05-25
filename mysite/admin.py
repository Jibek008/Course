from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
import nested_admin



class NetworkInline(admin.TabularInline):
    model = Network
    extra = 1

class NetworkAdmin(admin.ModelAdmin):
    inlines = [NetworkInline]


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class OptionInline(nested_admin.NestedStackedInline):
    model = Option
    extra = 1


class QuestionsInline(nested_admin.NestedStackedInline):
    model = Questions
    extra = 1
    inlines = [OptionInline]


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    inlines = [LessonInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(Exam)
class ExamAdmin(nested_admin.NestedModelAdmin, TranslationAdmin):
    inlines = [QuestionsInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Questions)
class QuestionsAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile,NetworkAdmin)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Network)

