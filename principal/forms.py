from django import forms

class FiareForm(forms.Form):
    nombre_secretario = forms.CharField(label='Nombre del secretario', max_length=100)
    apellidos_secretario = forms.CharField(label='Apellidos del secretario', max_length=100)
    NIF_secretario = forms.CharField(label='NIF del secretario', max_length=9)
    nombre_asociacion = forms.CharField(label='Nombre de la asociación', max_length=100)
    CIF_asociacion = forms.CharField(label='CIF de la asociación', max_length=9)
    domicilio_asoc = forms.CharField(label='Domicilio de la asociación', max_length=100)
    numero_registro = forms.CharField(label='Numero de registro', max_length=9)
    dia_reunion = forms.IntegerField(label='Dia de la reunión', min_value=1, max_value=31)
    mes_reunion = forms.IntegerField(label='Mes de la reunión', min_value=1, max_value=12)
    anno_reunion = forms.IntegerField(label='Año de la reunión', min_value=1900, max_value=2100)
    nombre_presidente = forms.CharField(label='Nombre del presidente', max_length=100)
    apellidos_presidente = forms.CharField(label='Apellidos del presidente', max_length=100)
    cantidad_acciones = forms.CharField(label='Cantidad de acciones', max_length=100)
    importe_acciones = forms.CharField(label='Importe de las acciones', max_length=100)
    nombre_accionista = forms.CharField(label='Nombre del accionista', max_length=100)
    apellidos_accionista = forms.CharField(label='Apellidos del accionista', max_length=100)
    NIF_accionista = forms.CharField(label='NIF del accionista', max_length=9)
    ciudad_reunion = forms.CharField(label='Ciudad de la reunión', max_length=100)

