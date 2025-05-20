import pikepdf
import json

# Cambia esto si tu PDF se llama distinto o está en otra ruta
nombre_pdf = "certificadometadatos.pdf"

with pikepdf.open(nombre_pdf) as pdf:
    metadatos = pdf.docinfo
    if "/fiare_metadata" in metadatos:
        datos = json.loads(str(metadatos["/fiare_metadata"]))
        print("✅ Metadatos JSON encontrados:")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    else:
        print("❌ No se encontró el campo /fiare_metadata en los metadatos.")