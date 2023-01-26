from random import choice
from datacenter.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(name_schoolkid):
    schoolkid = Schoolkid.objects.get(full_name__contains=name_schoolkid)
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid)
    for mark in schoolkid_marks:
        mark.points = 5
        mark.save()


def create_commendation(name_schoolkid, name_subject):
    commendation_text = choice([
        "Молодец!", "Отлично!", "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!",
        "Ты меня очень обрадовал!"])
    schoolkid = Schoolkid.objects.get(full_name__contains=name_schoolkid)
    subject = Subject.objects.get(title__contains=name_subject,
                                  year_of_study=6)
    lesson_description = Lesson.objects.filter(subject=subject).order_by(
        'date').first()
    Commendation.objects.create(
        teacher=lesson_description.teacher,
        subject=subject,
        text=commendation_text,
        created=lesson_description.date,
        schoolkid=schoolkid)


def delete_chastisement(name_schoolkid):
    schoolkid = Schoolkid.objects.get(full_name__contains=name_schoolkid)
    schoolkid_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisement.delete()


def catch_exception(function_name, *args):
    try:
        function_name(*args)
    except ObjectDoesNotExist:
        print("Кажется допущена ошибка при заполнение данных, \n"
              "Проверь правильность написание ФИО или Предмета.")
    except MultipleObjectsReturned:
        print("Уточните имя ученика и/или предмета,"
              " и убедитесь что заполнили данные")