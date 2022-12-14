from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import StudentSignUpForm, TeacherSignupForm
from .models import User, Student, Teacher


class StudentSignUpView(LoginRequiredMixin, CreateView):
	model = User
	form_class = StudentSignUpForm
	template_name = 'registration/student_register.html'

	def get_context_data(self, **kwargs):
		kwargs["user_type"] = "student"
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect("student_main_menu")


class TeacherSignUpView(CreateView):
	model = User
	form_class = TeacherSignupForm
	template_name = 'registration/teacher_register.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'teacher'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('teacher_main_menu')


class TeacherListView(ListView):
	model = User

	def get_context_data(self, **kwargs):
		context = super(TeacherListView, self).get_context_data(**kwargs)
		context["teachers"] = User.objects.filter(is_teacher=True)
		return context


class TeacherProfileDetailView(DetailView):
	model = User
	template_name = "templates/teacher_profile.html"
	context_object_name = "teacher"

	# def get_context_data(self, **kwargs):
	# 	context = super(TeacherProfileDetailView, self).get_context_data(**kwargs)
	# 	context["my_profile"] = User.objects.filter(pk=self.object.pk).select_related("Teacher")

	def get_object(self, queryset=None):
		return get_object_or_404(User, pk=self.request.user.id)

# @never_cache
# def dispatch(self, *args, **kwargs):
# 	return super(TeacherProfileDetailView, self).dispatch(*args, **kwargs)


class StudentMainMenu(TemplateView):
	template_name = "templates/student_main_menu.html"


class TeacherMainMenu(TemplateView):
	template_name = "templates/teacher_main_menu.html"


# @login_required
# def get_request_teacher_profile(request):
# 	teacher = Teacher.objects.filter(user_id=request.user.id)
# 	# profile = ProfileEmployee.objects.filter(employee_id=request.user.id)
# 	return render(request, "templates/teacher_profile.html", context={"teacher": teacher})


def register(request):
	if request.method == "POST":
		user_form = TeacherSignupForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save()
			new_user.save()
			return render(request, "templates/teacher_main_menu.html", {"new_user": new_user})
	else:
		user_form = TeacherSignupForm()
	return render(request, "registration/teacher_register.html", {'form': user_form})
