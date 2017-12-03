from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='')
    name.widget.attrs.update({'id' : 'name'})
    name.widget.attrs.update({'placeholder' : 'Tu Nombre'})
    name.widget.attrs.update({'class' : 'form-control form-control-white'}) 
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
