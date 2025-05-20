from django.shortcuts import render
from .forms import FiareForm
from django.http import HttpResponse
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors

def formulario(request):
    if request.method == 'POST':
        form = FiareForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
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
            cantidad_acciones = form.cleaned_data['cantidad_acciones']
            importe_acciones = form.cleaned_data['importe_acciones']
            nombre_accionista = form.cleaned_data['nombre_accionista']
            apellidos_accionista = form.cleaned_data['apellidos_accionista']
            NIF_accionista = form.cleaned_data['NIF_accionista']
            ciudad_reunion = form.cleaned_data['ciudad_reunion']

            fecha = f"{dia:02d}/{mes:02d}/{anno}"

            # Crear el PDF
            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=A4)

            styles = getSampleStyleSheet()
            estilo_justificado = ParagraphStyle(
                name="Justificado",
                parent=styles["Normal"],
                alignment=TA_JUSTIFY,
                fontName="Helvetica",
                fontSize=10,
                leading=14
            )
            estilo_negrita = ParagraphStyle(
                name="Negrita",
                parent=styles["Normal"],
                alignment=TA_JUSTIFY,
                fontName="Helvetica-Bold",
                fontSize=10,
                leading=14
            )

            contenido = []

            parrafos = [
                f"D. {nombre_secretario} {apellidos_secretario}, con NIF {NIF_secretario}, en calidad de Secretario de la Asociación {nombre_asociacion}, con CIF {CIF_asociacion} y domicilio en {domicilio_asoc}, inscrita en el Registro General de Asociaciones del País Vasco con número de registro {numero_registro}.",
                "CERTIFICO:",
                f"Que en la Asamblea General Ordinaria (extraordinaria), en su reunión del {fecha}, en el domicilio social, y actuando como Presidente y Secretario D/Dña. {nombre_presidente} {apellidos_presidente} y D/Dña. {nombre_secretario} {apellidos_secretario} respectivamente, cumplidos los requisitos estatutarios y legales, se adoptaron, entre otros los siguientes acuerdos:",
                f"PRIMERO: Se aprueba la decisión de comprar {cantidad_acciones} acciones de Banca Popolare Etica S.C.P.A. Sucursal España por importe de {importe_acciones} euros.",
                f"SEGUNDO: Otorgar poder tanto amplio como sea posible a D. {nombre_accionista} {apellidos_accionista} con NIF {NIF_accionista} para representar de forma solidaria a esta asociación, para realizar todos los trámites necesarios y formalizar la compra de acciones aprobada en Asamblea General.",
                "TERCERO: La vigencia de esta autorización se extenderá desde la fecha de emisión de este documento, hasta la fecha en la que sea revocada.",
                f"Y para que así conste y surta los efectos que proceda, se extiende el presente en {ciudad_reunion} el día {fecha}."
            ]

            for texto in parrafos:
                if texto == "CERTIFICO:":
                    contenido.append(Paragraph(texto, estilo_negrita))
                else:
                    contenido.append(Paragraph(texto, estilo_justificado))
                contenido.append(Spacer(1, 12))

            # Espacios antes de tabla
            contenido.append(Spacer(1, 24))
            contenido.append(Spacer(1, 24))

            # Tabla con nombres centrados y línea
            tabla_firmas = Table([
                ["PRESIDENTE", "SECRETARIO"],
                [f"D./Dña. {nombre_presidente} {apellidos_presidente}", f"D./Dña. {nombre_secretario} {apellidos_secretario}"]
            ], colWidths=[250, 250])

            tabla_firmas.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LINEBELOW', (0, 1), (-1, 1), 0.25, colors.white),
                ('TOPPADDING', (0, 0), (-1, -1), 12),
            ]))

            contenido.append(tabla_firmas)

            # Generar el PDF
            doc.build(contenido)
            buffer.seek(0)

            # Añadir metadatos JSON al PDF usando pikepdf
            import pikepdf
            import json

            # Diccionario con los datos del formulario
            metadatos_json = {
                "nombre_secretario": nombre_secretario,
                "apellidos_secretario": apellidos_secretario,
                "NIF_secretario": NIF_secretario,
                "nombre_asociacion": nombre_asociacion,
                "CIF_asociacion": CIF_asociacion,
                "domicilio_asoc": domicilio_asoc,
                "numero_registro": numero_registro,
                "fecha_reunion": fecha,
                "ciudad_reunion": ciudad_reunion,
                "nombre_presidente": nombre_presidente,
                "apellidos_presidente": apellidos_presidente,
                "cantidad_acciones": cantidad_acciones,
                "importe_acciones": importe_acciones,
                "nombre_accionista": nombre_accionista,
                "apellidos_accionista": apellidos_accionista,
                "NIF_accionista": NIF_accionista
            }

            # Abrir el PDF generado con pikepdf desde el buffer
            temp_pdf = BytesIO()
            temp_pdf.write(buffer.getvalue())
            temp_pdf.seek(0)

            with pikepdf.open(temp_pdf) as pdf:
                pdf.docinfo["/fiare_metadata"] = json.dumps(metadatos_json)
                
                final_buffer = BytesIO()
                pdf.save(final_buffer)

            final_buffer.seek(0)

            # Devolver el PDF con metadatos al navegador
            return HttpResponse(final_buffer, content_type='application/pdf', headers={
                'Content-Disposition': 'attachment; filename="certificadometadatos.pdf"'
            })

    else:
        form = FiareForm()

    return render(request, 'ModeloCertif.html', {'form': form})
