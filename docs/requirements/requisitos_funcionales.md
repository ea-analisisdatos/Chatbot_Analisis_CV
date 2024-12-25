# Requisitos Funcionales del Proyecto: Chatbot de Análisis de Currículums

## Introducción
Este documento detalla los requisitos funcionales del sistema "Chatbot de Análisis de Currículums". Para cada funcionalidad, se especifican los actores involucrados, una breve descripción y los atributos necesarios con sus características.

---

## Requisitos Funcionales

### **RF-01: Registro de Candidatos**
- **Actor(es) Relacionado(s):** Candidato.
- **Descripción:** Permitir que los candidatos se registren en la plataforma proporcionando sus datos personales básicos.
- **Atributos Relevantes:**

| Atributo        | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|-----------------|----------|------------------------------------------------|-------------|---------------------|
| id_candidato    | Entero   | Identificador único del candidato              | Sí          | N/A                 |
| nombre          | Texto    | Nombre completo del candidato                  | Sí          | N/A                 |
| email           | Email    | Dirección de correo electrónico del candidato | Sí          | N/A                 |
| contraseña      | Texto    | Contraseña para acceder al sistema             | Sí          | N/A                 |
| fecha_registro  | Fecha    | Fecha de registro en la plataforma             | Sí          | N/A                 |

---

### **RF-02: Subir Curriculum Vitae (CV)**
- **Actor(es) Relacionado(s):** Candidato.
- **Descripción:** Permitir al candidato subir su CV en formatos soportados (PDF, DOCX, TXT).
- **Atributos Relevantes:**

| Atributo        | Tipo        | Descripción                                   | Obligatorio | Valores Permitidos |
|-----------------|-------------|-----------------------------------------------|-------------|---------------------|
| archivo_cv      | Archivo     | CV en formato PDF, DOCX o TXT                | Sí          | .pdf, .docx, .txt   |
| id_candidato    | Entero      | Identificador único del candidato            | Sí          | N/A                 |
| fecha_subida    | Fecha       | Fecha en que el CV fue subido                | Sí          | N/A                 |

---

### **RF-03: Validación de Datos Extraídos**
- **Actor(es) Relacionado(s):** Candidato.
- **Descripción:** Permitir al candidato revisar, editar y confirmar los datos extraídos de su CV.
- **Atributos Relevantes:**

| Atributo               | Tipo      | Descripción                                     | Obligatorio | Valores Permitidos |
|------------------------|-----------|-------------------------------------------------|-------------|---------------------|
| id_candidato           | Entero    | Identificador único del candidato              | Sí          | N/A                 |
| datos_extraidos        | JSON      | Datos extraídos automáticamente del CV         | Sí          | N/A                 |
| confirmacion_candidato | Booleano  | Estado de confirmación de los datos            | Sí          | true, false         |
| fecha_confirmacion     | Fecha     | Fecha en que se confirmó el CV                 | No          | N/A                 |

---

### **RF-04: Consultar Base de Datos de Candidatos**
- **Actor(es) Relacionado(s):** Reclutador.
- **Descripción:** Permitir al reclutador buscar candidatos según criterios específicos.
- **Atributos Relevantes:**

| Atributo           | Tipo       | Descripción                                     | Obligatorio | Valores Permitidos |
|--------------------|------------|-------------------------------------------------|-------------|---------------------|
| criterios_busqueda | JSON       | Parámetros de búsqueda (ej. experiencia, habilidades) | Sí      | N/A                 |
| resultados         | Lista      | Lista de candidatos que cumplen los criterios  | Sí          | N/A                 |
| id_reclutador      | Entero     | Identificador único del reclutador             | Sí          | N/A                 |

---

### **RF-05: Generar Informe de Candidatos**
- **Actor(es) Relacionado(s):** Reclutador.
- **Descripción:** Permitir al reclutador generar un informe en PDF con los datos de los candidatos seleccionados.
- **Atributos Relevantes:**

| Atributo         | Tipo      | Descripción                                 | Obligatorio | Valores Permitidos |
|------------------|-----------|---------------------------------------------|-------------|---------------------|
| id_reclutador    | Entero    | Identificador único del reclutador          | Sí          | N/A                 |
| candidatos       | Lista     | Lista de IDs de candidatos seleccionados    | Sí          | N/A                 |
| informe_pdf      | Archivo   | Informe generado en formato PDF             | Sí          | .pdf                |
| fecha_generacion | Fecha     | Fecha en que se generó el informe           | Sí          | N/A                 |

---

### **RF-06: Registro de Reclutadores**
- **Actor(es) Relacionado(s):** Administrador.
- **Descripción:** Permitir el registro y validación de reclutadores en la plataforma.
- **Atributos Relevantes:**

| Atributo        | Tipo     | Descripción                                  | Obligatorio | Valores Permitidos |
|-----------------|----------|----------------------------------------------|-------------|---------------------|
| id_reclutador   | Entero   | Identificador único del reclutador           | Sí          | N/A                 |
| nombre_empresa  | Texto    | Nombre de la empresa asociada al reclutador  | Sí          | N/A                 |
| estado_validado | Booleano | Estado de validación del reclutador          | Sí          | true, false         |

---

### **RF-07: Publicar Ofertas de Trabajo**
- **Actor(es) Relacionado(s):** Reclutador.
- **Descripción:** Permitir al reclutador publicar ofertas de trabajo vinculadas a habilidades específicas.
- **Atributos Relevantes:**

| Atributo           | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|--------------------|----------|------------------------------------------------|-------------|---------------------|
| id_oferta          | Entero   | Identificador único de la oferta              | Sí          | N/A                 |
| habilidades        | Lista    | Lista de habilidades requeridas               | Sí          | N/A                 |
| descripcion_puesto | Texto    | Descripción del puesto de trabajo             | Sí          | N/A                 |
| fecha_publicacion  | Fecha    | Fecha en que se publicó la oferta             | Sí          | N/A                 |

---

### **RF-08: Inscripción a Ofertas de Trabajo**
- **Actor(es) Relacionado(s):** Candidato.
- **Descripción:** Permitir al candidato inscribirse a ofertas de trabajo disponibles.
- **Atributos Relevantes:**

| Atributo           | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|--------------------|----------|------------------------------------------------|-------------|---------------------|
| id_inscripcion     | Entero   | Identificador único de la inscripción         | Sí          | N/A                 |
| id_candidato       | Entero   | Identificador único del candidato             | Sí          | N/A                 |
| id_oferta          | Entero   | Identificador único de la oferta              | Sí          | N/A                 |
| fecha_inscripcion  | Fecha    | Fecha en que se realizó la inscripción        | Sí          | N/A                 |

---

### **RF-09: Consultar Inscripciones Realizadas**
- **Actor(es) Relacionado(s):** Candidato.
- **Descripción:** Permitir al candidato consultar las ofertas a las que se ha inscrito.
- **Atributos Relevantes:**

| Atributo           | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|--------------------|----------|------------------------------------------------|-------------|---------------------|
| id_candidato       | Entero   | Identificador único del candidato             | Sí          | N/A                 |
| inscripciones      | Lista    | Lista de inscripciones realizadas             | Sí          | N/A                 |

---

### **RF-10: Recepción Automática de CVs por Correo Electrónico**
- **Actor(es) Relacionado(s):** Administrador.
- **Descripción:** Permitir recibir CVs enviados por correo electrónico y clasificarlos según su contenido.
- **Atributos Relevantes:**

| Atributo           | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|--------------------|----------|------------------------------------------------|-------------|---------------------|
| correo_remitente   | Email    | Dirección de correo del remitente             | Sí          | N/A                 |
| archivo_cv         | Archivo  | CV adjunto recibido por correo                | Sí          | .pdf, .docx, .txt   |
| fecha_recepcion    | Fecha    | Fecha en que se recibió el CV                 | Sí          | N/A                 |
| estado_validacion  | Booleano | Indica si el CV ha sido validado              | Sí          | true, false         |

---

### **RF-11: Generar Lista de Candidatos para una Oferta**
- **Actor(es) Relacionado(s):** Reclutador.
- **Descripción:** Generar una lista de los mejores candidatos inscritos en una oferta según los criterios de la misma.
- **Atributos Relevantes:**

| Atributo           | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|--------------------|----------|------------------------------------------------|-------------|---------------------|
| id_oferta          | Entero   | Identificador único de la oferta              | Sí          | N/A                 |
| candidatos_filtrados | Lista  | Lista de candidatos que cumplen los criterios | Sí          | N/A                 |
| algoritmo_matching | Texto    | Algoritmo utilizado para el matching          | Sí          | N/A                 |
| fecha_generacion   | Fecha    | Fecha en que se generó la lista               | Sí          | N/A                 |

---

### **RF-12: Métricas por Reclutador**
- **Actor(es) Relacionado(s):** Administrador.
- **Descripción:** Generar reportes sobre las métricas de gestión de candidatos por reclutadores.
- **Atributos Relevantes:**

| Atributo           | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|--------------------|----------|------------------------------------------------|-------------|---------------------|
| id_reclutador      | Entero   | Identificador único del reclutador            | Sí          | N/A                 |
| total_candidatos   | Entero   | Número total de candidatos gestionados        | Sí          | N/A                 |
| total_ofertas      | Entero   | Número total de ofertas gestionadas           | Sí          | N/A                 |
| fecha_reporte      | Fecha    | Fecha en que se generó el reporte             | Sí          | N/A                 |

---

### **RF-13: Chatbot Interactivo**
- **Actor(es) Relacionado(s):** Candidato, Reclutador.
- **Descripción:** Responder preguntas frecuentes y guiar a los usuarios en las acciones disponibles dentro del sistema.
- **Atributos Relevantes:**

| Atributo        | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|-----------------|----------|------------------------------------------------|-------------|---------------------|
| consulta        | Texto    | Pregunta realizada por el usuario             | Sí          | N/A                 |
| respuesta       | Texto    | Respuesta proporcionada por el sistema        | Sí          | N/A                 |

---

### **RF-14: Gestión de Habilidades**
- **Actor(es) Relacionado(s):** Administrador, Reclutador.
- **Descripción:** Mantener una base de datos de habilidades utilizadas tanto por candidatos como por ofertas.
- **Atributos Relevantes:**

| Atributo        | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|-----------------|----------|------------------------------------------------|-------------|---------------------|
| id_habilidad    | Entero   | Identificador único de la habilidad           | Sí          | N/A                 |
| nombre_habilidad| Texto    | Nombre de la habilidad                        | Sí          | N/A                 |

---

### **RF-15: Análisis de Sesgos**
- **Actor(es) Relacionado(s):** Administrador.
- **Descripción:** Detectar posibles sesgos en los procesos de selección y generar reportes.
- **Atributos Relevantes:**

| Atributo        | Tipo     | Descripción                                    | Obligatorio | Valores Permitidos |
|-----------------|----------|------------------------------------------------|-------------|---------------------|
| sesgos_detectados | JSON   | Detalles de sesgos detectados                 | Sí          | N/A                 |
| fecha_reporte   | Fecha    | Fecha en que se generó el análisis            | Sí          | N/A                 |

```
