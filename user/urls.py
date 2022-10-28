from django.contrib.auth.views import LoginView
from django.urls import path

from user.views import StudentSignUpView, StudentMainMenu, TeacherMainMenu, TeacherSignUpView, TeacherProfileDetailView

urlpatterns = [
	path("student/signup/", StudentSignUpView.as_view(), name="student_signup"),
	path("student/main_menu/", StudentMainMenu.as_view(), name="student_main_menu"),
	path("teacher/signup/", TeacherSignUpView.as_view(), name="teacher_signup"),
	path("teacher/main_menu/", TeacherMainMenu.as_view(), name="teacher_main_menu"),
	path("teacher/my_profile/", TeacherProfileDetailView.as_view(), name="my_profile_teacher"),
	path("login/", LoginView.as_view(), name="login")
]