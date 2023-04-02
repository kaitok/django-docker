from django import forms
from django.core.validators import RegexValidator
import re

from .models import Event


class EventForm(forms.ModelForm):
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message=(
        "Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))

    tel_number = forms.CharField(
        validators=[tel_number_regex], max_length=15, label='電話番号')

    class Meta:
        model = Event
        fields = ['title', 'text', 'start_datetime',
                  'end_datetime', 'mail', 'tel_number']
        labels = {
            'title': 'タイトル',
            'text': '本文',
            'start_datetime': '開始日時',
            'end_datetime': '終了日時',
            'mail': 'メールアドレス',
        }
        widgets = {
            'start_datetime': forms.TextInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.TextInput(attrs={'type': 'datetime-local'}),
        }

    def is_valid_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def clean_mail(self):
        mail = self.cleaned_data['mail']
        if not self.is_valid_email(mail):
            raise forms.ValidationError('有効なメールアドレスを入力してください。')
        return mail

    def clean_tel_number(self):
        tel_number = self.cleaned_data['tel_number']
        if len(tel_number) < 10:
            raise forms.ValidationError('電話番号は10桁以上で入力してください。')
        return tel_number

    def clean(self):
        cleaned_data = super().clean()
        start_day = cleaned_data['start_datetime']
        end_day = cleaned_data['end_datetime']
        if start_day > end_day:
            raise forms.ValidationError("開始日は終了日より前にしてください。")
        return cleaned_data
