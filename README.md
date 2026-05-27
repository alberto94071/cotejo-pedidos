# ⚡ Verificador de Pre-Órdenes (IGSS - San Marcos)

> Aplicación de escritorio de nivel profesional diseñada para la verificación automática tripartita entre reportes de compras, formas de pedido A-01 (PDF) y consolidaciones del sistema (Pre-órdenes).

Este software automatiza el proceso de auditoría y conciliación de pedidos del **Consultorio del Instituto Guatemalteco de Seguridad Social (IGSS) en San Marcos**, eliminando errores humanos, detectando subproductos no autorizados y generando reportes analíticos consolidados de manera instantánea.

---

## ✨ Características Principales

*   **Verificación Tripartita Inteligente:** Cruce de datos automático entre Reportes de Compras (Excel), Forma A-01 (PDF) y Consolidaciones (XML/Excel).
*   **Modo Operativo Dual:**
    *   **Automático:** Carga el PDF original del pedido y extrae mediante OCR el correlativo, año, unidad de adscripción e insumos.
    *   **Manual (PDF Opcional):** Permite ingresar de forma interactiva el Correlativo de Pedido, Año y la Unidad de Adscripción utilizando selectores inteligentes cargados con las unidades más frecuentes.
*   **Detección de Restricciones Críticas:** Resalta instantáneamente en **Rojo brillante** cualquier subproducto prohibido (como `'001-019-0005'` o `'001-004-0007'`) para evitar compras no autorizadas.
*   **Consolidación Inteligente de Cantidades:** Agrupa cantidades por Código PPR y Subproducto, previniendo falsos positivos por duplicidades o múltiples códigos internos mapeados al mismo insumo físico.
*   **Exportación Analítica a Excel:** Genera reportes en formato `.xlsx` elegantemente diseñados (libres de marcas de desarrollo genéricas), con resúmenes estadísticos automáticos y anexos para subproductos prohibidos o incorrectos.
*   **Diseño Premium (Glassmorphism):** Interfaz oscura y translúcida (`-alpha 0.98`), con controles personalizados y fluidos de minimizar, maximizar nativo y cierre rápido, libre de decoraciones estándar del sistema operativo.
*   **Auto-Updater Integrado:** Al iniciar, la aplicación verifica silenciosamente en background contra el repositorio de GitHub y alerta al usuario mediante notificaciones *toast* si existe una nueva versión con novedades detalladas, lista para descargar.

---

## 🛠️ Requisitos del Sistema (Para ejecutar desde código fuente)

1.  **Python 3.10 o superior**
2.  **Tesseract OCR (Windows):**
    *   Instalar Tesseract OCR desde su [instalador oficial](https://github.com/UB-Mannheim/tesseract/wiki).
    *   Asegúrate de marcar los diccionarios en español en la instalación.
3.  **Poppler (Windows):**
    *   Es necesario para la conversión de PDF a imágenes del OCR. Coloca la carpeta binaria de poppler junto al script o instálalo a través del sistema.

### Librerías Requeridas
Instala las dependencias ejecutando:
```bash
pip install pandas openpyxl pillow numpy pdf2image pytesseract
```

---

## 📦 Compilación y Empaquetado (`.exe`)

Para empaquetar el verificador en un único archivo ejecutable autónomo, sin pantalla negra de fondo y con todos los recursos incrustados, utiliza la siguiente instrucción de **PyInstaller**:

```bash
python -m PyInstaller --onefile --noconsole --icon="cotejo_icon.ico" --name="VerificadorPreordenes" --add-data "igss_logo.png;." --add-data "igss_azul-removebg-preview.png;." --add-data "cotejo_icon.ico;." cotejo_pedidos.py
```

El ejecutable compilado estará listo para ser distribuido en la carpeta `dist/VerificadorPreordenes.exe`.

---

## 🔄 Gestión de Actualizaciones

El sistema de actualización automatizado lee el archivo `version.json` hospedado en GitHub. 

### Estructura de `version.json`
```json
{
  "version": "3.3",
  "download_url": "https://github.com/alberto94071/cotejo-pedidos/releases/latest/download/VerificadorPreordenes.exe",
  "notes": "✨ Versión Estable Inicial:\n- Rediseño con interfaz premium y modo Glassmorphism.\n- Selector interactivo de guardado de reportes.\n- Validación inteligente de cantidades PPR."
}
```

Cada vez que publiques una nueva versión:
1.  Incrementa `APP_VERSION` en el script.
2.  Compila el nuevo ejecutable con PyInstaller.
3.  Crea un nuevo Release en GitHub (ej. tag `v3.4`) y sube el `.exe`.
4.  Actualiza el archivo `version.json` en tu repositorio con la nueva versión y el resumen de cambios realizados.

---

## ⚖️ Licencia y Autoría
*   **Autor:** RonyAlberto
*   **Organización:** Consultorio del Instituto Guatemalteco de Seguridad Social (IGSS), San Marcos.
*   **Versión:** v3.3 (Estable)
