from . models import Gum
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, ValidationError
from core.generators import generate_id


class GumForm(ModelForm):
    class Meta:
        model = Gum
        fields = ('name', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd16', 'd17', 'd18', 'd19', 'd20', 'd21', 'd22', 'd23', 'd24', 'd25', 'd26', 'd27', 'd28', 'subm', 'slug')
    
        widgets = {
            "name": TextInput(attrs={"class": 'form-control',}),
            "d1": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d2": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d3": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d4": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d5": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d6": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d7": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d8": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d9": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d10": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d11": NumberInput(attrs={"class": 'form-control', "max": '3'}),
            "d12": NumberInput(attrs={"class": 'form-control', "max": '3'}),
            "d13": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d14": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d15": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d16": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d17": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d18": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d19": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d20": NumberInput(attrs={"class": 'form-control', "max": '1'}),
            "d21": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d22": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d23": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d24": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d25": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d26": NumberInput(attrs={"class": 'form-control', "max": '2'}),
            "d27": NumberInput(attrs={"class": 'form-control', "max": '10'}),
            "d28": NumberInput(attrs={"class": 'form-control', "max": '10'}),
            "subm": CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": TextInput(attrs={"value": generate_id(), "class": 'form-control'})
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL1 = sum((self.cleaned_data['d1'], self.cleaned_data['d3'], self.cleaned_data['d5'], self.cleaned_data['d7'], self.cleaned_data['d9'], self.cleaned_data['d11'], self.cleaned_data['d13'], self.cleaned_data['d15'], self.cleaned_data['d17'], self.cleaned_data['d19'], self.cleaned_data['d21'], self.cleaned_data['d23'], self.cleaned_data['d25']))

        ALL2 = sum((self.cleaned_data['d2'], self.cleaned_data['d4'], self.cleaned_data['d6'], self.cleaned_data['d8'], self.cleaned_data['d10'], self.cleaned_data['d12'], self.cleaned_data['d14'], self.cleaned_data['d16'], self.cleaned_data['d18'], self.cleaned_data['d20'], self.cleaned_data['d22'], self.cleaned_data['d24'], self.cleaned_data['d26']))

        if not (2 <= ALL1 <= 8 and 3 <= ALL2 <= 9):
            raise ValidationError('Слишком много или слишком мало часов недельной нагрузки!')
