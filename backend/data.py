# backend/data.py

# Mapeo de Número de Ruta a Programa
NUM_RUTA_TO_PROGRAMA = {
    1: ["Crecimiento Empresarial"],
    2: ["Emprendimiento, Ruta Bogotá/Cundinamarca Emprende, Innovación"],
    3: ["Emprendimiento, Ruta Bogotá/Cundinamarca Emprende, Innovación"],
    4: ["Consolidación y escalamiento empresarial"],
    5: ["Consolidación y escalamiento empresarial"],
    6: ["Consolidación y escalamiento empresarial"],
    7: ["Consolidación y escalamiento empresarial"],
    8: ["Consolidación y escalamiento empresarial"],
    9: ["Consolidación y escalamiento empresarial"],
    10: ["Foro presidentes"]
}

# Mapeo de Programa a Nombre de Ruta
PROGRAMA_TO_NOMBRE_RUTA = {
    "Crecimiento Empresarial": ["Economia popular"],
    "Emprendimiento, Ruta Bogotá/Cundinamarca Emprende, Innovación": ["INNOVACION", "EMPRENDIMIENTO"],
    "Consolidación y escalamiento empresarial": [
        "ESTRATEGIA FINANCIERA Y RENDICIÓN DE CUENTAS PARA EL SECTOR MODA E INDUSTRIAS CREATIVAS Y CULTURALES",
        "FORTALECIMIENTO DE EQUIPOS DE VENTA PARA EL SECTOR MODA",
        "PROGRAMACIÓN ABIERTA Y REGIÓN",
        "CICLOS FOCALIZADOS - MULTISECTORIAL",
        "SECTOR ALIMENTOS",
        "FINANCIERO Y PRODUCTIVIDAD",
        "INTERNACIONALIZACIÓN",
        "Plan de internacinalización"
    ],
    "Foro presidentes": ["ESCUELA DE MENTORES, VOLUNTARIADO Y PROGRAMACIÓN REGIÓN (FORO PRESIDENTES)"]
}

# Mapeo de Nombre de Ruta a Sector
NOMBRE_RUTA_TO_SECTOR = {
    "Economia popular": ["Economia popular"],
    "INNOVACION": ["Innovación"],
    "EMPRENDIMIENTO": ["Bogota Emprende y Cundinamarca Emprende"],
    "ESTRATEGIA FINANCIERA Y RENDICIÓN DE CUENTAS PARA EL SECTOR MODA E INDUSTRIAS CREATIVAS Y CULTURALES": ["Estrategia Financiera y Rendición de Cuentas para el Sector Moda e Industrias Creativas y Culturales"],
    "FORTALECIMIENTO DE EQUIPOS DE VENTA PARA EL SECTOR MODA": ["Fortalecimiento de Equipos de Venta para el Sector Moda"],
    "PROGRAMACIÓN ABIERTA Y REGIÓN": ["No aplica"],
    "CICLOS FOCALIZADOS - MULTISECTORIAL": [
        "Gestión del Talento Humano para el sector construcción",
        "Excelencia para el sector Turismo",
        "Proyectos financieros con proposito y Gestion financiera en empresas de servicios empresariales",
        "Transformación digital",
        "Tecnología en modelos de negocio y servicios de Consultoria",
        "Tecnología en Cadena de abastecimiento - (Logistica)",
        "Programa de Desarrollo proveedores"
    ],
    "SECTOR ALIMENTOS": [
        "Marketing Experiencial",
        "Servicio al Cliente para el sector gastronomico",
        "Mercadeo para Impulsar el Crecimiento",
        "Inteligencia Artificial",
        "Fidelización y atracción del Talento Humano"
    ],
    "FINANCIERO Y PRODUCTIVIDAD": [
        "Indicadores de gestión",
        "Metodologias de mejoramiento de la Productividad",
        "Gestión Finaciero"
    ],
    "INTERNACIONALIZACIÓN": ["Talleres", "Asesorias individales"],
    "Plan de internacinalización": [
        "INTERNACIONALIZACION - Entregable - Preseleccion de mercado",
        "INTERNACIONALIZACION - Entregable - MarketFit",
        "INTERNACIONALIZACION - Entregable - One Pager"
    ],
    "ESCUELA DE MENTORES, VOLUNTARIADO Y PROGRAMACIÓN REGIÓN (FORO PRESIDENTES)": ["ESCUELA DE MENTORES"]
}

# Lista completa de programas, nombres de ruta y sectores (pueden ser útiles pero no son estrictamente necesarios para la lógica actual)
ALL_PROGRAMAS = list(set(sum(NUM_RUTA_TO_PROGRAMA.values(), [])))
ALL_NOMBRES_RUTA = list(set(sum(PROGRAMA_TO_NOMBRE_RUTA.values(), [])))
ALL_SECTORES = list(set(sum(NOMBRE_RUTA_TO_SECTOR.values(), [])))