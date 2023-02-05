from random import choice
from datacenter.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


COMMENDATION_TEXTS = [
    "Молодец!", "Отлично!", "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!",
    "Ты меня очень обрадовал!"]


def take_schoolkid(name_schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name_schoolkid)
        return schoolkid
    except ObjectDoesNotExist:
        print("Кажется допущена ошибка при заполнение данных, \n"
              "Проверь правильность написание ФИО")
    except MultipleObjectsReturned:
        print(f"Уточните имя ученика, в дневнике не один {name_schoolkid} "
              "добавь отчество или фамилию")


def create_commendation(name_schoolkid, name_subject):
    schoolkid = take_schoolkid(name_schoolkid)
    try:
        subject = Subject.objects.get(
            title__contains=name_subject, year_of_study=schoolkid.year_of_study
        )
    except ObjectDoesNotExist:
        print("Кажется допущена ошибка при заполнение данных, \n"
              "Проверь правильность написание предмета")
    except MultipleObjectsReturned:
        print(f"Уточните название предмета хотели справить - {name_subject} ")
    lesson_description = Lesson.objects.select_related(
        "subject", "teacher").filter(subject=subject).order_by(
        "-date").first()
    Commendation.objects.create(
        teacher=lesson_description.teacher,
        subject=lesson_description.subject,
        text=choice(COMMENDATION_TEXTS),
        created=lesson_description.date,
        schoolkid=schoolkid)


def fix_marks(name_schoolkid):
    schoolkid = take_schoolkid(name_schoolkid)
    Mark.objects.filter(schoolkid=schoolkid).update(points=5)


def delete_chastisement(name_schoolkid):
    schoolkid = take_schoolkid(name_schoolkid)
    schoolkid_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisement.delete()
