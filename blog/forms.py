from django.forms import ModelForm, ValidationError

from .models import BlogPost


class BlogPostModelForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "content"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        instance = self.instance
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise ValidationError(
                "This title already exista, please try a different one")
        return title
