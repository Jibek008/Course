
from .models import Category, Course, Lesson, Exam, Option, Questions
from modeltranslation.translator import register, TranslationOptions

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name','description','course_lan',)

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('lesson',)

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('exam_name',)


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('variant',)


@register(Questions)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('questions_name',)



