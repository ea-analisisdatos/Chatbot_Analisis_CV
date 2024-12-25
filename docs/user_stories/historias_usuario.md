
# Historias de Usuario del Proyecto: Chatbot de Análisis de Currículum Vitae

## Introducción

Este documento recoge las historias de usuario del proyecto "Chatbot de Análisis de Currículum Vitae" siguiendo las mejores prácticas de metodologías ágiles. Las historias de usuario describen las funcionalidades que el sistema debe proporcionar desde la perspectiva de los usuarios involucrados.

----------

## Formato de las Historias de Usuario

Cada historia de usuario está escrita en el siguiente formato:

-   **ID de la Historia de Usuario:** [HU-XX]
-   **Descripción:** “Como [rol], quiero [funcionalidad] para [beneficio/objetivo].”
-   **Criterios de Aceptación:** Condiciones específicas que deben cumplirse para considerar que la historia está completa.
-   **Prioridad:** Alta, Media, Baja (según la importancia para el sistema).
-   **Esfuerzo Estimado:** (en puntos o unidades de tiempo).

----------

## Historias de Usuario

### **HU-01: Subir Curriculum Vitae (CV)**

-   **Descripción:** Como candidato, quiero subir mi CV en formatos PDF, DOCX o TXT para que el sistema analice y almacene mis datos.
-   **Criterios de Aceptación:**
    1.  El sistema debe aceptar archivos en los formatos permitidos.
    2.  El sistema debe validar que el archivo contiene información relevante de un CV (basado en palabras clave).
    3.  Si el archivo no es un CV, se debe mostrar un mensaje de error y no almacenar el archivo.
    4.  Una vez aceptado, el sistema extrae los datos y los almacena en la base de datos.
-   **Prioridad:** Alta
-   **Esfuerzo Estimado:** 8 puntos

----------

### **HU-02: Validación de Datos Extraídos**

-   **Descripción:** Como candidato, quiero revisar los datos extraídos de mi CV para confirmar que sean correctos antes de guardarlos en la base de datos.
-   **Criterios de Aceptación:**
    1.  El sistema debe presentar los datos extraídos en un formulario editable.
    2.  El candidato puede modificar cualquier campo incorrecto.
    3.  El sistema solo guardará los datos si el candidato los confirma.
    4.  Los datos no confirmados deben eliminarse automáticamente después de 24 horas.
-   **Prioridad:** Alta
-   **Esfuerzo Estimado:** 5 puntos

----------

### **HU-03: Consultar Base de Datos de Candidatos**

-   **Descripción:** Como reclutador, quiero buscar candidatos en la base de datos según criterios como experiencia, localidad, y habilidades para identificar los mejores perfiles para una oferta laboral.
-   **Criterios de Aceptación:**
    1.  El sistema debe permitir búsquedas por filtros: localidad, experiencia, habilidades, y salario deseado.
    2.  Los resultados deben mostrarse ordenados por relevancia.
    3.  El sistema debe resolver empates entre candidatos usando un algoritmo de machine learning sin sesgos.
    4.  La búsqueda debe completarse en menos de 5 segundos.
-   **Prioridad:** Alta
-   **Esfuerzo Estimado:** 13 puntos

----------

### **HU-04: Generar Informe de Candidatos**

-   **Descripción:** Como reclutador, quiero generar un informe en PDF con los datos de los candidatos seleccionados para compartirlos con la empresa contratante.
-   **Criterios de Aceptación:**
    1.  El sistema debe permitir seleccionar uno o más candidatos.
    2.  El informe debe incluir información clave: nombre, experiencia, habilidades, y contacto.
    3.  El informe debe ser exportado en un formato legible y profesional (PDF).
    4.  El archivo generado debe estar disponible para descarga inmediata.
-   **Prioridad:** Media
-   **Esfuerzo Estimado:** 8 puntos

----------

### **HU-05: Registro de Reclutadores**

-   **Descripción:** Como administrador, quiero que los reclutadores se registren en la plataforma para garantizar el acceso seguro a la base de datos de candidatos.
-   **Criterios de Aceptación:**
    1.  El sistema debe requerir un formulario de registro con datos como nombre, correo, y empresa.
    2.  Los reclutadores deben ser aprobados manualmente por un administrador.
    3.  El sistema debe enviar un correo de confirmación tras la aprobación.
    4.  Los reclutadores deben usar credenciales para acceder al sistema.
-   **Prioridad:** Alta
-   **Esfuerzo Estimado:** 8 puntos

----------

### **HU-06: Publicar Ofertas de Trabajo**

-   **Descripción:** Como reclutador, quiero publicar ofertas de trabajo vinculadas a habilidades específicas para atraer a los candidatos más relevantes.
-   **Criterios de Aceptación:**
    1.  El formulario de publicación debe incluir: descripción del puesto, habilidades requeridas, experiencia deseada, tipo de jornada, y salario.
    2.  Las ofertas deben aparecer en un panel visible para los candidatos.
    3.  Los candidatos deben recibir recomendaciones automáticas si cumplen los criterios.
-   **Prioridad:** Media
-   **Esfuerzo Estimado:** 10 puntos

----------

### **HU-07: Seguridad y Privacidad de Datos**

-   **Descripción:** Como administrador, quiero garantizar que los datos de los candidatos estén protegidos para cumplir con las normativas de privacidad.
-   **Criterios de Aceptación:**
    1.  Los datos personales deben estar cifrados en la base de datos.
    2.  Solo los usuarios autorizados deben acceder a los datos.
    3.  El sistema debe cumplir con la normativa GDPR.
-   **Prioridad:** Alta
-   **Esfuerzo Estimado:** 8 puntos

----------



> Escrito por [Erika Alvares](https://www.erikaalvares.es/).
