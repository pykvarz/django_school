from django.contrib import admin

from user.models import User, Teacher, Student


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ("id", "username", "first_name", "last_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ("user_id",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ("user_id", "iin")

