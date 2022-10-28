from user.models import User


def get_last_id_student():
	try:
		last_id_student = User.objects.filter(is_student=1).last().id
		last_id_student = last_id_student + 1
		return last_id_student
	except:
		last_id_student = 1
		return last_id_student


def get_last_id_teacher():
	try:
		last_id_teacher = User.objects.filter(is_teacher=1).last().id
		last_id_teacher = last_id_teacher + 1
		return last_id_teacher
	except:
		last_id_teacher = 1
		return last_id_teacher
