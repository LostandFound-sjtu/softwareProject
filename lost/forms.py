from django import forms
from item.models import Item

#  这里的这个人是没什么用处的


class LostItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'status',
            'name',
            'tags',
            'phone_number',
            'category',
            'location',
            'image',
            'identification_mark',
            'secret_information',
        ]

