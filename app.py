from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

EMPRESA_INFO = {
    "nombre": "ACOSERVICES, C.A.",
    "aliado": "WEG Cestari",
    "email": "ventas@acoservices.com.ve",
    "telefono": "+58 241 412 1571",
    "direccion": "Av. 104 C.C. La Fundación, Local Nro. 21, Urb. Fundación II, Valencia, Estado Carabobo, Venezuela.",
    "descripcion": (
        "Acoservices, C.A. es una empresa dedicada tanto a la venta de Motorreductores, "
        "Reductores y Motores (siendo una alternativa de venta de equipos en moneda nacional), "
        "así mismo, al servicio técnico, mantenimiento y reparación de accionamientos, con mano "
        "de obra calificada, que garantiza el restablecimiento de la operatividad de su equipo y un "
        "eficiente funcionamiento. Además, contamos con la comercialización de variadores de "
        "frecuencia para la industria."
    ),
    "finalidad": (
        "La finalidad de esta empresa es la venta y servicio técnico de motorreductores, "
        "reductores de alto torque y motores eléctricos."
    )
}


SERVICIOS = [
    {
        "titulo": "Venta de motorreductores",
        "descripcion": "Conozca los motorreductores y todos nuestros productos de la marca WEG Cestari, con alternativa de venta en moneda nacional.",
        "imagen": "catalogo.jpg",
        "ajuste": "object-cover"
    },
    {
        "titulo": "Servicio técnico y reparación",
        "descripcion": "Contamos con un personal capacitado en servicio, mantenimiento preventivo, correctivo y reparación de motorreductores.",
        "imagen": "servicios.jpg",
        "ajuste": "object-cover"
    },
    {
        "titulo": "Presencia de Acoservices en Venezuela",
        "descripcion": "Contacta a nuestros vendedores y asesores técnicos distribuidos en todo el territorio Venezolano.",
        "imagen": "ubicacion.png",
        "ajuste": "object-contain p-6 bg-slate-100"
    }
]

PRODUCTOS = [
    {
        "id": "coaxial",
        "nombre": "Coaxial",
        "categoria": "Reductores",
        "subtitulo": "Reductor Coaxial WEG Cestari",
        "resumen": "Diseño compacto de ejes coaxiales en línea para altas cargas radiales y trabajo continuo.",
        "detalle": "Los reductores coaxiales WEG Cestari ofrecen alta eficiencia mecánica, bajo nivel de ruido y versatilidad de montaje con patas o bridas para múltiples sectores industriales.",
        "imagen": "coaxial1.png"
    },
    {
        "id": "vertimax",
        "nombre": "Vertimax",
        "categoria": "Reductores",
        "subtitulo": "Reductor Vertimax WEG Cestari",
        "resumen": "Especiales para aplicaciones verticales, mezcladores y agitadores industriales.",
        "detalle": "Configuración diseñada específicamente para ejes verticales sometidos a cargas axiales y radiales severas en procesos químicos, alimenticios y tratamiento de aguas.",
        "imagen": "vertimax(2).jpg"
    },
    {
        "id": "conimax",
        "nombre": "Conimax",
        "categoria": "Reductores",
        "subtitulo": "Reductor Conimax WEG Cestari",
        "resumen": "Reductores ortogonales de engranajes cónicos helicoidales de alto rendimiento.",
        "detalle": "Transmisión de potencia en ángulo recto (90°) con engranajes cónicos helicoidales rectificados que garantizan máxima durabilidad y ahorro de espacio.",
        "imagen": "conimax(1).jpg"
    },
    {
        "id": "magma-m",
        "nombre": "Magma-M",
        "categoria": "Reductores",
        "subtitulo": "Reductor Magma-M WEG Cestari",
        "resumen": "Sistemas de ejes paralelos y montaje pendular de alta confiabilidad mecánica.",
        "detalle": "Ideales para transportadores de banda, elevadores de cangilones y maquinaria industrial pesada que requiere transmisión robusta y mantenimiento sencillo.",
        "imagen": "magma-m-1.webp"
    },
    {
        "id": "helimax",
        "nombre": "Helimax",
        "categoria": "Reductores",
        "subtitulo": "Reductor Helimax WEG Cestari",
        "resumen": "Reductores industriales de alto torque para minería, siderurgia y agroindustria.",
        "detalle": "Carcasa monobloque de hierro fundido de alta resistencia diseñada para soportar los mayores torques y condiciones extremas de operación continua.",
        "imagen": "helimax(1).jpg"
    },
    {
        "id": "alumag",
        "nombre": "Alumag",
        "categoria": "Reductores",
        "subtitulo": "Reductor Alumag WEG Cestari",
        "resumen": "Carcasa ligera de aluminio con excelente disipación térmica y resistencia a la corrosión.",
        "detalle": "Solución versátil y liviana para aplicaciones industriales de potencia baja y media, con múltiples posiciones de montaje.",
        "imagen": "catalogo.jpg"
    },
    {
        "id": "variadores-motores",
        "nombre": "Variadores y Motores",
        "categoria": "Accionamientos",
        "subtitulo": "Variadores de Frecuencia y Motores Eléctricos",
        "resumen": "Comercialización de variadores de frecuencia, motores eléctricos y accesorios (acoples, engranajes, repuestos).",
        "detalle": "Suministro integral de soluciones en accionamientos para todos los segmentos de la industria nacional con respaldo y garantía ACOSERVICES.",
        "imagen": "acoservices imagen.jpg"
    }
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        empresa=EMPRESA_INFO,
        servicios=SERVICIOS,
        productos=PRODUCTOS
    )


@app.route("/api/cotizar", methods=["POST"])
def recibir_cotizacion():
    datos = request.get_json() or request.form
    nombre = datos.get("nombre", "").strip()
    telefono = datos.get("telefono", "").strip()
    email = datos.get("email", "").strip()
    equipo = datos.get("equipo", "Consulta general").strip()
    detalles = datos.get("detalles", "").strip()

    if not nombre or not email or not detalles:
        return jsonify({
            "ok": False,
            "mensaje": "Por favor complete los campos obligatorios."
        }), 400

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n" + "=" * 55)
    print(f"NUEVA SOLICITUD DE COTIZACIÓN [{fecha}]")
    print(f"Cliente / Empresa : {nombre}")
    print(f"Teléfono          : {telefono}")
    print(f"Correo            : {email}")
    print(f"Equipo de interés : {equipo}")
    print(f"Detalles          : {detalles}")
    print("=" * 55 + "\n")

    return jsonify({
        "ok": True,
        "mensaje": f"Gracias {nombre}. Su solicitud ha sido registrada y será atendida por nuestro equipo técnico."
    })


if __name__ == "__main__":
    print("Servidor ACOSERVICES iniciado en: http://127.0.0.1:5000")
    app.run(debug=True, host="127.0.0.1", port=5000)