from django.forms import ModelForm
from memo.models import Memo

class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = ("title", "body")

