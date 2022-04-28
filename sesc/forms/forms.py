from forms.models import Gum, Sgum, SocEk, MatInf, FizMat, FizTech
from django import forms
from core.generators import generate_id


class GumForm(forms.ModelForm):
    class Meta:
        model = Gum
        fields = ('name', 'subm', 'slug', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11')
    
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control',}),
            "subm": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": forms.TextInput(attrs={"value": generate_id(), "type": 'hidden'}),

            "d1": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d2": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d3": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d4": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d5": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d6": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d7": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d8": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d9": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d10": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d11": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise forms.ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL = sum((
            int(self.cleaned_data['d1']) * 2,
            int(self.cleaned_data['d2']),
            int(self.cleaned_data['d3']) * 3,
            int(self.cleaned_data['d4']),
            int(self.cleaned_data['d5']),
            int(self.cleaned_data['d6']) * 3,
            2,
            int(self.cleaned_data['d7']),
            int(self.cleaned_data['d8']),
            int(self.cleaned_data['d9']),
            2,
            int(self.cleaned_data['d10']) * 2,
            int(self.cleaned_data['d11']) * 2,
        ))
        if ALL > 8:
            raise forms.ValidationError('Слишком много часов недельной нагрузки!')


class SgumForm(forms.ModelForm):
    class Meta:
        model = Sgum
        fields = ('name', 'subm', 'slug', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11')
    
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control',}),
            "subm": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": forms.TextInput(attrs={"value": generate_id(), "type": 'hidden'}),

            "d1": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d2": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d3": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d4": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d5": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d6": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d7": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d8": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d9": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d10": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d11": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise forms.ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL = sum((
            int(self.cleaned_data['d1']),
            int(self.cleaned_data['d2']),
            int(self.cleaned_data['d3']),
            int(self.cleaned_data['d4']),
            int(self.cleaned_data['d5']) * 3,
            1,
            int(self.cleaned_data['d6']) * 2,
            int(self.cleaned_data['d7']),
            int(self.cleaned_data['d8']),
            2,
            int(self.cleaned_data['d9']) * 2,
            int(self.cleaned_data['d10']) * 2,
            int(self.cleaned_data['d11']) * 2,
        ))
        if ALL > 9 or 3 >= ALL:
            raise forms.ValidationError('Слишком много или мало часов недельной нагрузки!')


class SocEkForm(forms.ModelForm):
    class Meta:
        model = SocEk
        fields = ('name', 'subm', 'slug', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8')
    
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control',}),
            "subm": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": forms.TextInput(attrs={"value": generate_id(), "type": 'hidden'}),

            "d1": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d2": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d3": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d4": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d5": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d6": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d7": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d8": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise forms.ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL = sum((
            int(self.cleaned_data['d1']),
            int(self.cleaned_data['d2']),
            int(self.cleaned_data['d3']),
            int(self.cleaned_data['d4']),
            int(self.cleaned_data['d5']) * 3,
            int(self.cleaned_data['d6']),
            2,
            int(self.cleaned_data['d7']) * 2,
            int(self.cleaned_data['d8']) * 2,
        ))
        if ALL > 7:
            raise forms.ValidationError('Слишком много или мало часов недельной нагрузки!')


class MatInfForm(forms.ModelForm):
    class Meta:
        model = MatInf
        fields = ('name', 'subm', 'slug', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8')
    
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control',}),
            "subm": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": forms.TextInput(attrs={"value": generate_id(), "type": 'hidden'}),

            "d1": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d2": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d3": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d4": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d5": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d6": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d7": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d8": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise forms.ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL = sum((
            int(self.cleaned_data['d1']) * 2,
            int(self.cleaned_data['d2']),
            int(self.cleaned_data['d3']),
            int(self.cleaned_data['d4']),
            int(self.cleaned_data['d5']),
            2,
            3,
            int(self.cleaned_data['d6']) * 2,
            int(self.cleaned_data['d7']) * 2,
            int(self.cleaned_data['d8']) * 2,
        ))
        if ALL > 9:
            raise forms.ValidationError('Слишком много или мало часов недельной нагрузки!')


class FizMatForm(forms.ModelForm):
    class Meta:
        model = FizMat
        fields = ('name', 'subm', 'slug', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8')
    
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control',}),
            "subm": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": forms.TextInput(attrs={"value": generate_id(), "type": 'hidden'}),

            "d1": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d2": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d3": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d4": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d5": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d6": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d7": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d8": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) >= 255:
            raise forms.ValidationError(f'Длина текста ({len(name)}) превышает допустимые 255 символов!')
        return name
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL = sum((
            int(self.cleaned_data['d1']) * 2,
            int(self.cleaned_data['d2']),
            int(self.cleaned_data['d3']),
            int(self.cleaned_data['d4']),
            int(self.cleaned_data['d5']),
            int(self.cleaned_data['d6']) * 2,
            int(self.cleaned_data['d8']) * 2,
            4,
        ))
        if ALL > 8:
            raise forms.ValidationError('Слишком много или мало часов недельной нагрузки!')


class FizTechForm(forms.ModelForm):
    class Meta:
        model = FizTech
        fields = ('name', 'subm', 'slug', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9')
    
        widgets = {
            "name": forms.TextInput(attrs={"class": 'form-control',}),
            "subm": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "slug": forms.TextInput(attrs={"value": generate_id(), "type": 'hidden'}),

            "d1": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d2": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d3": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d4": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d5": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d6": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d7": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d8": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            "d9": forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
    
    def clean(self):
        self.cleaned_data['slug'] = generate_id()
        ALL = sum((
            int(self.cleaned_data['d1']) * 2,
            int(self.cleaned_data['d2']),
            int(self.cleaned_data['d3']),
            int(self.cleaned_data['d4']),
            int(self.cleaned_data['d5']),
            int(self.cleaned_data['d6']) * 2,
            int(self.cleaned_data['d7']) * 2,
            int(self.cleaned_data['d9']) * 2,
            4,
        ))
        if ALL > 8:
            raise forms.ValidationError('Слишком много или мало часов недельной нагрузки!')
