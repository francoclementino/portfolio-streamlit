import streamlit as st
import base64 # Necesario para el carrusel CSS (simulado)

# --- Configuración de la Página ---
# Usamos 'wide' para que el contenido ocupe más espacio
st.set_page_config(
    page_title="Portfolio de Franco Clementino",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INYECTAR CSS PERSONALIZADO ---
# Esto es para mejorar el diseño, centrar logos y hacer el carrusel
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Vamos a crear un archivo CSS simple
css_content = """
/* Estilo para los contenedores de proyectos */
.project-container {
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 24px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.project-container:hover {
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    transform: translateY(-5px);
}

/* Ocultar la barra de scroll del carrusel */
.logo-carousel-container {
    display: flex;
    overflow-x: auto; /* Permite scroll horizontal */
    padding-bottom: 20px; /* Espacio para que la sombra no se corte */
    scrollbar-width: none; /* Firefox */
    -ms-overflow-style: none;  /* IE y Edge */
}
.logo-carousel-container::-webkit-scrollbar {
    display: none; /* Chrome, Safari y Opera */
}

/* Estilo de cada logo */
.logo-item {
    flex-shrink: 0; /* Evita que los logos se encojan */
    margin-right: 40px; /* Espacio entre logos */
    text-align: center;
    filter: grayscale(100%); /* Los hacemos blanco y negro */
    opacity: 0.6;
    transition: all 0.3s ease;
}
.logo-item:hover {
    filter: grayscale(0%); /* Color al pasar el mouse */
    opacity: 1.0;
    transform: scale(1.1);
}
.logo-item img {
    max-height: 60px; /* Altura máxima para logos */
    width: auto;
}
.logo-item p {
    font-size: 14px;
    margin-top: 8px;
    font-weight: 500;
}

/* Centrar el título de clientes */
.clients-header {
    text-align: center;
    margin-bottom: 30px;
}
"""

# Escribir el CSS a un archivo temporal y cargarlo
with open("style.css", "w") as f:
    f.write(css_content)

local_css("style.css")


# --- SECCIÓN DE INTRODUCCIÓN ---
with st.container():
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        # Reemplaza con una URL de tu propia foto
        st.image("https://placehold.co/400x400/EFEFEF/333333?text=Tu+Foto+Aqui",
                 width=300,
                 use_column_width="auto",
                 caption="Franco Clementino")

    with col2:
        st.title("Franco Clementino")
        st.subheader("Data Analyst & Business Intelligence Developer")
        st.write("""
        ¡Bienvenido a mi portfolio! Soy un apasionado del análisis de datos con experiencia
        en transformar datos crudos en insights accionables.

        Me especializo en la creación de dashboards interactivos, automatización de procesos
        y desarrollo de soluciones de BI que impulsan la toma de decisiones.
        """)
        st.link_button("Contactar por LinkedIn", "https://www.linkedin.com/in/francoclementino/")

st.divider()

# --- SECCIÓN DE PROYECTOS ---
st.header("Proyectos Destacados", anchor=False)

# Datos de los proyectos (reemplaza con los tuyos)
proyectos = [
    {
        "titulo": "Transformación Digital Petrolera",
        "descripcion": "Desarrollamos la estrategia integral de datos de una compañía petrolera, con espacios digitales de trabajo colaborativo en la nube, dashboards de alto nivel y automatizaciones de procesos internos.",
        "imagen_url": "https://placehold.co/600x400/3498DB/FFFFFF?text=Proyecto+Petrolero",
        "tags": ["Power BI", "Azure", "Python"]
    },
    {
        "titulo": "Dashboard de Rentabilidad Oil&Gas",
        "descripcion": "Implementamos una estrategia de datos que permite a la gerencia monitorear la rentabilidad de sus negocios a través de reportes dinámicos en tiempo real.",
        "imagen_url": "https://placehold.co/600x400/2ECC71/FFFFFF?text=Proyecto+Rentabilidad",
        "tags": ["Power BI", "SQL Server", "Power Automate"]
    },
    {
        "titulo": "Aplicación Mobile para Relevamientos",
        "descripcion": "Creamos una aplicación tablet para el relevamiento en tiempo real del estado de instalaciones en yacimientos, con base de datos en la nube y reportes en Power BI.",
        "imagen_url": "https://placehold.co/600x400/E74C3C/FFFFFF?text=Proyecto+App+Mobile",
        "tags": ["Power Apps", "SharePoint", "Dataverse"]
    }
]

# Iterar y mostrar cada proyecto
for i, proyecto in enumerate(proyectos):
    with st.container():
        # Aplicamos la clase CSS que definimos
        st.markdown(f'<div class="project-container">', unsafe_allow_html=True)

        # Alternar el orden de imagen y texto para variar el layout
        if i % 2 == 0:
            col1, col2 = st.columns([1, 2], gap="large")
        else:
            col2, col1 = st.columns([2, 1], gap="large")

        with col1:
            st.image(proyecto["imagen_url"], caption=f"Vista previa de {proyecto['titulo']}")

        with col2:
            st.subheader(proyecto["titulo"], anchor=False)
            st.write(proyecto["descripcion"])
            
            # Mostrar tags/tecnologías
            for tag in proyecto["tags"]:
                st.button(tag, disabled=True, key=f"tag_{i}_{tag}")

        st.markdown(f'</div>', unsafe_allow_html=True)


st.divider()

# --- SECCIÓN DE CLIENTES (CARRUSEL SIMULADO) ---
st.markdown('<h2 class="clients-header">Clientes que confían en nosotros</h2>', unsafe_allow_html=True)

# Lista de logos (reemplaza con los nombres y URLs de los logos)
logos = [
    {"nombre": "Cliente A", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+A"},
    {"nombre": "Cliente B", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+B"},
    {"nombre": "Cliente C", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+C"},
    {"nombre": "Cliente D", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+D"},
    {"nombre": "Cliente E", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+E"},
    {"nombre": "Cliente F", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+F"},
]

# Streamlit no tiene un "carrusel" nativo.
# Usamos un contenedor con scroll horizontal (definido en el CSS)
# para mostrar los logos de forma elegante.
logo_html = '<div class="logo-carousel-container">'
for logo in logos:
    logo_html += f"""
    <div class="logo-item">
        <img src="{logo['url']}" alt="{logo['nombre']}">
        <p>{logo['nombre']}</p>
    </div>
    """
logo_html += '</div>'

st.markdown(logo_html, unsafe_allow_html=True)
