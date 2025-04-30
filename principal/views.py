from django.shortcuts import render
from .forms import FiareForm
from django.http import HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth

def draw_wrapped_text(canvas, text, x, y, max_width, line_height=15, font_name="Helvetica", font_size=10):
    canvas.setFont(font_name, font_size)
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        if stringWidth(test_line, font_name, font_size) <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    for line in lines:
        canvas.drawString(x, y, line)
        y -= line_height

def formulario(request):
    if request.method == 'POST':
        form = FiareForm(request.POST)
        if form.is_valid():
            nombre_secretario = form.cleaned_data['nombre_secretario']
            apellidos_secretario = form.cleaned_data['apellidos_secretario']
            NIF_secretario = form.cleaned_data['NIF_secretario']
            nombre_asociacion = form.cleaned_data['nombre_asociacion']
            CIF_asociacion = form.cleaned_data['CIF_asociacion']
            domicilio_asoc = form.cleaned_data['domicilio_asoc']
            numero_registro = form.cleaned_data['numero_registro']
            dia = form.cleaned_data['dia_reunion']
            mes = form.cleaned_data['mes_reunion']
            anno = form.cleaned_data['anno_reunion']
            nombre_presidente = form.cleaned_data['nombre_presidente']
            apellidos_presidente = form.cleaned_data['apellidos_presidente']

            # Fecha compuesta
            fecha = f"{dia:02d}/{mes:02d}/{anno}"


            buffer = BytesIO()
            p = canvas.Canvas(buffer,pagesize=A4)

            parrafo1 = f"D. {nombre_secretario} {apellidos_secretario}, con NIF {NIF_secretario}, en calidad de Secretario de la Asociación {nombre_asociacion}, con CIF {CIF_asociacion} y domicilio en {domicilio_asoc}, inscrita en el Registro General de Asociaciones del País Vasco con número de registro {numero_registro}"
            
            parrafo2= f"CERTIFICO"
            
            parrafo3= f"Que en la Asamblea General Ordinaria (extraordinaria), en su reunión del {fecha}, en el domicilio social, y actuando como Presidente y Secretario D/Dña. {nombre_presidente} {apellidos_presidente} y D/Dña. {nombre_secretario} {apellidos_secretario} respectivamente, cumplidos los requisitos estatutarios y legales, se adoptaron, entre otros los siguientes acuerdos:"


            
            y=800
            draw_wrapped_text(p,parrafo1, x=100, y=y, max_width=450)
            y-=60
            draw_wrapped_text(p,parrafo2, x=100, y=y, max_width=450)
            y-=60
            draw_wrapped_text(p,parrafo3, x=100, y=y, max_width=450)

            p.showPage()
            p.save()

            buffer.seek(0)
            response = HttpResponse(buffer,content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="certificado.pdf"'
            return response
    else:
        form = FiareForm()

    return render(request, 'ModeloCertif.html', {'form': form})

