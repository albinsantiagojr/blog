from django import forms
from .models import Post, Category, Comment

# hard code the categories, dont use this, we want a dynamic way to do this
#choices = [('programming', 'Programming'), ('web', 'Web'), ('other', 'Other')]


choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'body', 'snippet', 'header_image' )
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'elder', 'type':'hidden'}), #using javascript to set the author to hide and auto fill
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),
            }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            #'title-tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tag'}),
            #'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'who wrote this?'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet':forms.Textarea(attrs={'class': 'form-control'}),
        
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body' )
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }