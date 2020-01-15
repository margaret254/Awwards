from django import forms

from award.models import AwardPost

class CreateAwardPostForm(forms.ModelForm):

    class Meta:
        model = AwardPost
        fields = ['title','body','image']

class UpdateAwardPostForm(forms.ModelForm):

    class Meta:
        model = AwardPost
        fields = ['title','body','image']

    def save(self, commit=True):
        award_post = self.instance
        award_post.title = self.cleaned_data['title']
        award_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            award_post.image = self.cleaned_data['image']

        if commit:
            award_post.save()
        return award_post
