from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Posts, UserRegistration


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserRegistration
        fields = ("username", "email", "user_image", 'password1', 'password2')

    def clean(self):
        image = self.cleaned_data["user_image"]
        if image is None or len(image) == 0:
            raise ValidationError("Image field in empty")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


class PostsForm(forms.Form):
    post = forms.CharField(max_length=255, widget=forms.Textarea)
    title = forms.CharField(max_length=10)
    topings = forms.MultipleChoiceField(choices = [('1','1'),('2','2')],widget =forms.CheckboxSelectMultiple)
