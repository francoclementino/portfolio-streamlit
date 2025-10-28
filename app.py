import streamlit as st
import base64

# --- TRADUCCIONES Y CONTENIDO ---
# Todo el texto de la web se almacena aquí
content = {
    'es': {
        'page_title': "Portfolio de Franco Clementino",
        'page_icon': "📊",
        'nav_projects': "Proyectos",
        'nav_clients': "Clientes",
        'intro_title': "Franco Clementino",
        'intro_subtitle': "Data Analyst & Business Intelligence Developer",
        'intro_body': """
        ¡Bienvenido a mi portfolio! Soy un apasionado del análisis de datos con experiencia
        en transformar datos crudos en insights accionables.

        Me especializo en la creación de dashboards interactivos, automatización de procesos
        y desarrollo de soluciones de BI que impulsan la toma de decisiones.
        """,
        'linkedin_button': "Contactar por LinkedIn",
        'projects_header': "Proyectos Destacados",
        'clients_header': "Clientes que confían en nosotros",
        'projects_list': [
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
        ],
        'clients_list': [
            {"nombre": "Cliente A", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+A"},
            {"nombre": "Cliente B", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+B"},
            {"nombre": "Cliente C", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+C"},
            {"nombre": "Cliente D", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+D"},
            {"nombre": "Cliente E", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+E"},
            {"nombre": "Cliente F", "url": "https://placehold.co/200x100/CCCCCC/999999?text=LOGO+CLIENTE+F"},
        ]
    },
    'en': {
        'page_title': "Franco Clementino's Portfolio",
        'page_icon': "📊",
        'nav_projects': "Projects",
        'nav_clients': "Clients",
        'intro_title': "Franco Clementino",
        'intro_subtitle': "Data Analyst & Business Intelligence Developer",
        'intro_body': """
        Welcome to my portfolio! I am a data analysis enthusiast with experience
        in transforming raw data into actionable insights.

        I specialize in creating interactive dashboards, process automation,
        and developing BI solutions that drive decision-making.
        """,
        'linkedin_button': "Contact via LinkedIn",
        'projects_header': "Featured Projects",
        'clients_header': "Clients Who Trust Us",
        'projects_list': [
            {
                "titulo": "Digital Transformation in Oil & Gas",
                "descripcion": "We developed a comprehensive data strategy for an oil company, including cloud-based collaborative digital workspaces, high-level dashboards, and internal process automation.",
                "imagen_url": "https://placehold.co/600x400/3498DB/FFFFFF?text=Oil+Project",
                "tags": ["Power BI", "Azure", "Python"]
            },
            {
                "titulo": "Oil&Gas Profitability Dashboard",
                "descripcion": "We implemented a data strategy that allows management to monitor business profitability through dynamic, real-time reports.",
                "imagen_url": "https://placehold.co/600x400/2ECC71/FFFFFF?text=Profitability+Project",
                "tags": ["Power BI", "SQL Server", "Power Automate"]
            },
            {
                "titulo": "Mobile App for Field Surveys",
                "descripcion": "We created a tablet application for real-time surveying of facility conditions in oil fields, with a cloud database and Power BI reports.",
                "imagen_url": "https://placehold.co/600x400/E74C3C/FFFFFF?text=Mobile+App+Project",
                "tags": ["Power Apps", "SharePoint", "Dataverse"]
            }
        ],
        'clients_list': [
            {"nombre": "Client A", "url": "https://placehold.co/200x100/CCCCCC/999999?text=CLIENT+A+LOGO"},
            {"nombre": "Client B", "url": "https://placehold.co/200x100/CCCCCC/999999?text=CLIENT+B+LOGO"},
            {"nombre": "Client C", "url": "https://placehold.co/200x100/CCCCCC/999999?text=CLIENT+C+LOGO"},
            {"nombre": "Client D", "url": "https://placehold.co/200x100/CCCCCC/999999?text=CLIENT+D+LOGO"},
            {"nombre": "Client E", "url": "https://placehold.co/200x100/CCCCCC/999999?text=CLIENT+E+LOGO"},
            {"nombre": "Client F", "url": "https://placehold.co/200x100/CCCCCC/999999?text=CLIENT+F+LOGO"},
        ]
    }
}

# --- INICIALIZACIÓN DE ESTADO ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'es'

# Seleccionar el diccionario de contenido actual
current_content = content[st.session_state.lang]

# --- Configuración de la Página ---
st.set_page_config(
    page_title=current_content['page_title'],
    page_icon=current_content['page_icon'],
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- INYECTAR CSS PERSONALIZADO ---
def local_css(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Archivo CSS '{file_name}' no encontrado. Creando...")
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(css_content) # Escribe el contenido si no existe
        local_css(file_name) # Vuelve a intentarlo

# CSS para el fondo, carrusel, estilos de proyecto y HEADER FIJO
css_content = """
/* --- IMAGEN DE FONDO --- */
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.toptal.com/designers/subtlepatterns/uploads/light-sketch-grey.png");
    background-size: cover;
    background-repeat: repeat;
    background-attachment: fixed;
}

/* --- HEADER FIJO (STICKY) --- */
.sticky-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background-color: rgba(255, 255, 255, 0.95); /* Fondo blanco semi-transparente */
    padding: 10px 2rem; /* Padding (2rem es ~32px) */
    box-shadow: 0 2px 10px rgba(0,0,0,0.1); /* Sombra sutil */
    backdrop-filter: blur(10px);
}

/* --- PADDING SUPERIOR PARA EL CONTENIDO --- */
/* Evita que el contenido principal quede oculto detrás del header fijo */
.main-content-padding {
    padding-top: 80px; /* Ajusta esta altura según sea necesario */
}

/* --- Contenedores semi-transparentes --- */
.project-container {
    background-color: rgba(255, 255, 255, 0.85); /* Blanco con 85% opacidad */
    backdrop-filter: blur(5px);
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}
.project-container:hover {
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    transform: translateY(-5px);
}

/* --- Ocultar la barra de scroll del carrusel --- */
.logo-carousel-container {
    display: flex;
    overflow-x: auto;
    padding-bottom: 20px;
    scrollbar-width: none;
    -ms-overflow-style: none;
}
.logo-carousel-container::-webkit-scrollbar {
    display: none;
}

/* --- Estilo de cada logo --- */
.logo-item {
    flex-shrink: 0;
    margin-right: 40px;
    text-align: center;
    filter: grayscale(100%);
    opacity: 0.6;
    transition: all 0.3s ease;
}
.logo-item:hover {
    filter: grayscale(0%);
    opacity: 1.0;
    transform: scale(1.1);
}
.logo-item img {
    max-height: 60px;
    width: auto;
}
.logo-item p {
    font-size: 14px;
    margin-top: 8px;
    font-weight: 500;
}

/* --- Centrar el título de clientes --- */
.clients-header {
    text-align: center;
    margin-bottom: 30px;
}
"""

# Escribir el CSS a un archivo y cargarlo
with open("style.css", "w", encoding="utf-8") as f:
    f.write(css_content)
local_css("style.css")


# --- BARRA DE NAVEGACIÓN Y LENGUAJE (FIJA) ---
# Envolvemos las columnas en un contenedor markdown con la clase "sticky-header"
st.markdown('<div class="sticky-header">', unsafe_allow_html=True)
col_nav, col_lang = st.columns([4, 1])

with col_nav:
    # Usamos markdown con HTML para crear los enlaces de ancla
    st.markdown(f"""
    <div style="margin-top: 10px;">
        <a href="#proyectos" style="text-decoration: none; color: #333; margin-right: 25px; font-weight: 500; font-size: 1.1rem;">{current_content['nav_projects']}</a>
        <a href="#clientes" style="text-decoration: none; color: #333; font-weight: 500; font-size: 1.1rem;">{current_content['nav_clients']}</a>
    </div>
    """, unsafe_allow_html=True)

with col_lang:
    # Botones de radio para seleccionar idioma con BANDERAS
    lang_options = {'es': 'Español 🇪🇸', 'en': 'English 🇬🇧'} # <-- CAMBIO AQUÍ
    
    selected_lang = st.radio(
        "Idioma/Language",
        options=['es', 'en'],
        format_func=lang_options.get, # Usa el diccionario para mostrar "Español 🇪🇸"
        index=0 if st.session_state.lang == 'es' else 1,
        horizontal=True,
        label_visibility="collapsed",
        key="lang_selector"
    )
    
    # Si el idioma cambia, actualiza el estado y recarga
    if st.session_state.lang != selected_lang:
        st.session_state.lang = selected_lang
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Cierra el div del header fijo


# --- SECCIÓN DE INTRODUCCIÓN (Con padding) ---
# Envolvemos el contenido principal en un div con padding
st.markdown('<div class="main-content-padding">', unsafe_allow_html=True)
with st.container():
    st.title(current_content['intro_title'])
    st.subheader(current_content['intro_subtitle'])
    st.write(current_content['intro_body'])
    st.link_button(current_content['linkedin_button'], "https://www.linkedin.com/in/francoclementino/")
st.markdown('</div>', unsafe_allow_html=True) # Cierra el div del padding


st.divider()

# --- SECCIÓN DE PROYECTOS ---
# El "anchor" crea el punto de anclaje para el enlace "#proyectos"
st.header(current_content['projects_header'], anchor="proyectos")

proyectos = current_content['projects_list']

# Iterar y mostrar cada proyecto
for i, proyecto in enumerate(proyectos):
    with st.container():
        st.markdown(f'<div class="project-container">', unsafe_allow_html=True)
        
        if i % 2 == 0:
            col1, col2 = st.columns([1, 2], gap="large")
        else:
            col2, col1 = st.columns([2, 1], gap="large")

        with col1:
            st.image(proyecto["imagen_url"], caption=f"Vista previa de {proyecto['titulo']}")

        with col2:
            st.subheader(proyecto["titulo"], anchor=False)
            st.write(proyecto["descripcion"])
            for tag in proyecto["tags"]:
                st.button(tag, disabled=True, key=f"tag_{i}_{tag}")
        
        st.markdown(f'</div>', unsafe_allow_html=True)

st.divider()

# --- SECCIÓN DE CLIENTES (CARRUSEL SIMULADO) ---
# El "anchor" crea el punto de anclaje para el enlace "#clientes"
st.header(current_content['clients_header'], anchor="clientes")

logos = current_content['clients_list']

logo_html = '<div class="logo-carousel-container">'
for logo in logos:
    logo_html += f"""
    <div class="logo-item">
        <img src="{logo['url']}" alt="{logo['nombre']}">
        <p>{logo['nombre']}</p>
    </div>
    """
logo_html += '</div>'

# --- ¡LA CORRECCIÓN MÁS IMPORTANTE ESTÁ AQUÍ! ---
# Asegúrate de que esta línea esté EXACTAMENTE así
st.markdown(logo_html, unsafe_allow_html=True)

