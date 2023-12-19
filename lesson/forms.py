from django import forms


class QuizForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        choices = question.answers.all()
        self.fields['choices'] = forms.ModelChoiceField(
            queryset=choices,
            widget=forms.RadioSelect,
            empty_label=None,
        )
