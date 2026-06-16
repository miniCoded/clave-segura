# Evaluador de Seguridad de Contraseñas

Aplicación desarrollada con Angular y Python para analizar la fortaleza de una contraseña y generar alternativas más seguras.

## Características

- Validación en tiempo real
- Generación de contraseñas a partir de una palabra base
- Tres niveles de seguridad:
  - **Segura**: 12+ caracteres y todos los requisitos cumplidos
  - **Media**: 7–11 caracteres y todos los requisitos cumplidos
  - **Insegura**: Faltan requisitos o la longitud es insuficiente
- Detección de patrones comunes (`password`, `123`, `qwerty`, etc.)
- Lista detallada de requisitos
- Pruebas BDD con Behave

## Tecnologías

- Frontend: Angular
- Backend: Flask
- Pruebas: Gherkin + Behave

## Instalación

### Backend

```bash
pip install -r requirements.txt
python app.py
```

Disponible en:

```text
http://localhost:5000
```

### Frontend

```bash
npm install
npm start
```

Disponible en:

```text
http://localhost:4200
```

## Pruebas

Ejecutar todas las pruebas:

```bash
python -m behave
```

## Estructura del Proyecto

```text
src/                  Aplicación Angular
app.py                API en Flask
password_validator.py Lógica de validación
features/             Escenarios y pasos BDD
requirements.txt      Dependencias de Python
```

## Consideraciones para Producción

- Usar HTTPS
- Almacenar contraseñas con hash
- Implementar limitación de solicitudes
- Mantener validaciones en el servidor
- Considerar bibliotecas como zxcvbn

## Licencia

MIT
