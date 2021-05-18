"""[Author: Chanh Duong. Student number: 040-681-356]
    """

from django import forms
from .models import Record

"""[The form so that user can fill the data
    Form model base on the Object model]
    """


class DateInput(forms.DateInput):
    input_type = 'date'

# creating a form


class RecordForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Record

        # specify fields from Model to be used
        fields = '__all__'
# 'pruid', 'prname', 'prnameFR', 'date', 'numconf', 'numprob', 'numdeaths', 'numtotal', 'numtoday', 'ratetotal'
        widgets = {

            # 'date': DateInput(),
            'pruid': forms.TextInput(attrs={'class': 'form-control'}),
            'prname': forms.TextInput(attrs={'class': 'form-control'}),
            'prnameFR': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numconf': forms.TextInput(attrs={'class': 'form-control'}),
            'numprob': forms.TextInput(attrs={'class': 'form-control'}),
            'numdeaths': forms.TextInput(attrs={'class': 'form-control'}),
            'numtotal': forms.TextInput(attrs={'class': 'form-control'}),
            'numtoday': forms.TextInput(attrs={'class': 'form-control'}),
            'ratetotal': forms.TextInput(attrs={'class': 'form-control'}),
            
        }


