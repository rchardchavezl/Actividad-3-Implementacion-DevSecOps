# NovaCorp — Company Management Platform + DevSecOps

NovaCorp es una aplicación web desarrollada en Flask para la gestión de empresas y comentarios asociados.  
El sistema implementa control de acceso por roles (admin, owner, user) y un pipeline de DevSecOps integrado para análisis de seguridad automatizado.

---

## 🌍 Aplicación en producción

La aplicación se encuentra desplegada y accesible públicamente en:

👉 https://actividad-3-implementacion-devsecops.onrender.com

---

## Usuarios por defecto

| Usuario | Contraseña | Rol   | Descripción              |
|--------|------------|--------|--------------------------|
| alice  | password1  | user   | Usuario estándar         |
| bob    | password2  | owner  | Propietario de empresa   |
| admin  | admin123   | admin  | Acceso completo          |

---

## Estructura del proyecto

```
.
├── .github/workflows/devsecops.yml   # Pipeline DevSecOps
├── .zap/rules.tsv                   # Reglas personalizadas ZAP
├── db/                              # Base de datos
├── routes/                          # Rutas de la aplicación
├── static/                          # Archivos estáticos
├── templates/                       # Vistas HTML
├── .semgrepignore                   # Exclusiones SAST
├── Dockerfile                       # Contenedor Docker
├── main.py                          # Punto de entrada
├── server.py                        # Configuración Flask
├── init_db.py                       # Inicialización DB
├── requirements.txt                 # Dependencias
├── Pipfile / Pipfile.lock
├── Procfile                         # Configuración Render
├── start.sh                         # Script de arranque
└── README.md
```

---

## Tecnologías utilizadas

- Python 3  
- Flask  
- SQLite  
- Bootstrap  
- Jinja2  
- GitHub Actions  
- Semgrep (SAST)  
- pip-audit (SCA)  
- OWASP ZAP (DAST)  
- Docker  
- Render  

---

## Pipeline DevSecOps

El pipeline definido en:

`.github/workflows/devsecops.yml`

se ejecuta automáticamente con cada push.

### 🔍 SAST — Semgrep

Detecta vulnerabilidades como:

- SQL Injection  
- Uso de funciones inseguras (MD5)  
- Credenciales expuestas  
- Debug activado  

### 📦 SCA — pip-audit

Analiza dependencias del proyecto:

- Detección de librerías vulnerables  
- Identificación de CVEs  

### 🌐 DAST — OWASP ZAP

Realiza análisis dinámico sobre la aplicación desplegada:

- Escaneo automático de endpoints  
- Generación de reporte HTML  
- Uso de reglas personalizadas  

---

## Resultados de Seguridad

### Antes de correcciones

| Tipo | Resultado |
|------|----------|
| SAST (Semgrep) | 17 vulnerabilidades |
| SCA (pip-audit) | 12 vulnerabilidades |
| DAST (ZAP) | Alertas detectadas |




## Conclusión

La implementación de este pipeline DevSecOps permite:

- Integrar seguridad en el ciclo de desarrollo  
- Detectar vulnerabilidades de forma temprana  
- Automatizar pruebas de seguridad  
- Garantizar despliegues más seguros  

---

## Autor

Richard Alfredo Chavez Lopez
