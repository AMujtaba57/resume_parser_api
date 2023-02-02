from django import forms


class KeyAlterForm(forms.ModelForm):

    class Meta:
        # model = KeywordAlternative
        # fields = "__all__"
        widgets = {
            "alter_keyword_list": forms.TextInput(attrs={
                "type": "text",
                "class": "form-control p-4",
                "data-role": "tagsinput",
            })
        }

    class Media:
        js = (
            'custom/js/tagger.js',
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.0/js/bootstrap.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-tagsinput/0.8.0/bootstrap-tagsinput.min.js'
        )
        css = {
            "all": (
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.0/css/bootstrap.min.css',
                'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css',
                'https://cdnjs.cloudflare.com/ajax/libs/bootstrap-tagsinput/0.8.0/bootstrap-tagsinput.css',
                'custom/css/tagger.css'
            )
        }
