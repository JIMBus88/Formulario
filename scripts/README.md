# Scripts de utilidad

Este directorio contiene herramientas auxiliares para pruebas y validación durante el desarrollo del proyecto.

## comprobar_metadatos.py

Este script comprueba que un archivo PDF contiene correctamente los metadatos JSON en el campo `/fiare_metadata`.

### Uso

1. Asegúrate de tener instalado `pikepdf`:
   ```bash
   pip install pikepdf

2. Coloca el PDF generado en la misma carpeta que este script (o ajusta la ruta en el código).

3. Ejecuta el script:
    ```bash
    python comprobar_metadatos.py

Devolverá los metadatos JSON si están presentes, o un aviso si no se encuentran.