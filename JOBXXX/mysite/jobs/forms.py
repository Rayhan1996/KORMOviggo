from django import forms

from .models import Job, Apply


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'name',
            'phone',
            'description',
            'salary',

        ]
class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = [
            'name',
            'phone',
            'mail',
            'cv',
            'student_id',

        ]
