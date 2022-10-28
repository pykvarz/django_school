from django import forms
from django.db import transaction

from user.models import User, Student, Teacher

from user.helpers.last_id import get_last_id_student, get_last_id_teacher


class StudentSignUpForm(forms.ModelForm):
    surname = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = f"s130t{get_last_id_student()}"
        user.password = User.objects.make_random_password()
        user.is_student = True
        user.save()
        student = Student.objects.create(
            user=user,
            surname=self.cleaned_data.get('surname')
        )
        return user


class TeacherSignupForm(forms.ModelForm):
    surname = forms.CharField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = f"s130t{get_last_id_teacher()}"
        user.password = User.objects.make_random_password()
        user.is_teacher = True
        user.save()
        student = Teacher.objects.create(
            user=user,
        )
        return user
