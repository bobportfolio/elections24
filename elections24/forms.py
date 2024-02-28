from django import forms
from django.core.exceptions import ValidationError
from elections24.models import Postcode


class PostcodeForm(forms.Form):
    postcode = forms.CharField(label="Postcode", max_length=8)

    def clean_postcode(self):
        postcode = self.cleaned_data["postcode"].upper()
        if postcode[-4] != ' ':
            postcode = postcode[:-3] + ' ' + postcode[-3:]
        try:
            Postcode.objects.get(postcode=postcode)
        except Postcode.DoesNotExist:
            raise ValidationError("Invalid Postcode!")
        return postcode
