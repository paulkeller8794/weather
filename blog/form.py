from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Article title"}))
    content = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Your description",
                                          "class": "new-class-name two",
                                          "id": "my-id-for-textarea",
                                          "rows": 20,
                                          "columns": 120
                                      }

                                  ))

    class Meta:
        model = Article
        fields = [
            'title',
            'content',

        ]

