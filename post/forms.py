from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:

        model = Post

        fields = ["title", "content", "image"]

        widgets = {

            "title": forms.TextInput(

                attrs={

                    "placeholder": "Enter post title",

                    "class": "form-control"

                }

            ),

            "content": forms.Textarea(

                attrs={

                    "placeholder": "Write your post here...",

                    "rows": 10,

                    "class": "form-control"

                }

            ),

            "image": forms.ClearableFileInput(

                attrs={

                    "class": "form-control"

                }

            ),

        }

    def clean_title(self):

        title = self.cleaned_data.get("title")

        if title and len(title) < 5:

            raise forms.ValidationError(

                "Title must not be less than 5 characters."

            )

        return title

    def clean_content(self):

        content = self.cleaned_data.get("content")

        if content and len(content) < 100:

            raise forms.ValidationError(

                "Content must not be less than 100 characters."

            )

        return content