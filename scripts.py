from random import choice
from datacenter.models import (Schoolkid,
                               Subject,
                               Lesson,
                               Commendation,
                               Mark,
                               Chastisement)


COMMENDATION_TEXTS = [
    "Молодец!", "Отлично!", "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!",
    "Ты меня очень обрадовал!"]


def take_schoolkid(name_schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name_schoolkid)
        return schoolkid
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist(
            "Кажется допущена ошибка при заполнение данных, \n"
            "проверь правильность написание ФИО"
        )
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned(
            f"Уточните имя ученика, в дневнике не один {name_schoolkid} "
            "добавь отчество или фамилию"
        )


def create_commendation(name_schoolkid, name_subject):
    schoolkid = take_schoolkid(name_schoolkid)
    try:
        subject = Subject.objects.get(
            title__contains=name_subject, year_of_study=schoolkid.year_of_study
        )
    except Subject.DoesNotExist:
        raise Subject.DoesNotExist(
            "Кажется допущена ошибка при заполнение данных, \n"
            "проверь правильность написание предмета."
        )
    except Subject.MultipleObjectsReturned:
        raise Subject.MultipleObjectsReturned(
            f"Уточните название предмета хотели справить - {name_subject} "
        )
    try:
        lesson = Lesson.objects.select_related(
            "subject", "teacher").filter(subject=subject).order_by(
            "-date").first()
        Commendation.objects.create(
            teacher=lesson.teacher,
            subject=lesson.subject,
            text=choice(COMMENDATION_TEXTS),
            created=lesson.date,
            schoolkid=schoolkid)
    except AttributeError:
        raise print(f"Кажется по предмету {name_subject} ещё не было уроков")


def fix_marks(name_schoolkid):
    schoolkid = take_schoolkid(name_schoolkid)
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)


def delete_chastisement(name_schoolkid):
    schoolkid = take_schoolkid(name_schoolkid)
    schoolkid_chastisement = Chastisement.objects.filter(schoolkid=schoolkid)
    schoolkid_chastisement.delete()
