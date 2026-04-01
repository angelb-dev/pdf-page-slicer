from pypdf import PdfReader, PdfWriter

def extraer_exactas(archivo_in, archivo_out, inicio, cantidad):
    try:
        reader = PdfReader(archivo_in)
        writer = PdfWriter()

        idx_inicio = inicio - 1
        idx_final = idx_inicio + cantidad

        for i in range(idx_inicio, idx_final):
            if i < len(reader.pages):
                writer.add_page(reader.pages[i])
            else:
                break

        with open(archivo_out, "wb") as f:
            writer.write(f)
        
        print(f"¡Listo! Se extrajeron exactamente {cantidad} páginas comenzando desde la {inicio}.")
    except Exception as e:
        print(f"Error: {e}")

# --- SOLO EDITA ESTOS DOS NÚMEROS ---
DESDE_QUE_PAGINA = 20
CUANTAS_PAGINAS = 20
# ------------------------------------

extraer_exactas("pdf1.pdf", "resultado_final.pdf", DESDE_QUE_PAGINA, CUANTAS_PAGINAS)
# Usar el comando "python pdf-slicer.py"