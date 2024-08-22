from typing import Any
from django import forms
from .models import Article
# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model=Article
#         fields=['title','content']
#     def clean(self):
#         data=self.cleaned_data
#         title=data.get('title')
#         query_set=Article.objects.filter(title__icontains=title)
#         if query_set.exists():
#             self.add_error("title",f"{title} is already in use")
#         return data
        



class ArticleForm(forms.Form):
    title=forms.CharField()
    content=forms.CharField()
    
    def clean_title(self):
        cleaned_data=self.cleaned_data
        title=cleaned_data.get('title')
        return title