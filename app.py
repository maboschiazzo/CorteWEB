from flask import Flask, render_template

app = Flask(__name__)

WHATSAPP_NUMERO = "5493513835105"

# Servicio Principal
SERVICIOS_CORTE = [
    {
        "titulo": "Creación de Página Web Inicial",
        "descripcion": "Diseño web simple, moderno y funcional. La solución directa para que tu emprendimiento tenga presencia en internet y recibas consultas por WhatsApp de forma sencilla y directa.",
        "badge": "Para Emprendedores"
    }
]

# Unidad Comercial
SERVICIOS_MODORECITAL = [
    {
        "titulo": "Traslados & Entradas a Recitales",
        "descripcion": "Gestión comercial y canal de venta autorizado para los viajes oficiales de Modo Recital.",
        "badge": "Canal Oficial"
    }
]

# Próximos Shows Destacados (Top 3)
PROXIMOS_SHOWS = [
    {
        "artista": "BTS ARIRANG WORLD TOUR",
        "lugar": "ESTADIO ÚNICO LA PLATA OCTUBRE 2026", 
        "estado": "Últimos Lugares"
    },
    {
        "artista": "MARC ANTHONY",
        "lugar": "MOVISTAR ARENA OCTUBRE 2026",
        "estado": "Reservas Abiertas"
    },
    {
        "artista": "KAROL G",
        "lugar": "ESTADIO RIVER PLATE FEBRERO 2027",
        "estado": "Próximamente",
    }
]

@app.route('/')
def home():
    return render_template(
        'index.html', 
        servicios_corte=SERVICIOS_CORTE,
        servicios_recital=SERVICIOS_MODORECITAL,
        proximos_shows=PROXIMOS_SHOWS,
        whatsapp=WHATSAPP_NUMERO
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)