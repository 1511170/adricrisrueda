# Plan de Ajustes - AdriCris Rueda

> **Fecha**: 2026-03-15  
> **Estado**: Fase 1 COMPLETADA | Fases 2-3 PENDIENTES  
> **Dependencias pendientes**: Fotos reales (Sobre mí, Servicios)

---

## 📋 Resumen de Cambios

| Sección | Archivo | Cambios | Prioridad |
|---------|---------|---------|-----------|
| Inicio | `index.astro` | 2 ajustes | Alta |
| Sobre mí | `sobre-mi.astro` | 8+ ajustes | Alta |
| Libro | `libro.astro` | 4 ajustes | Alta |
| Servicios | `servicios.astro` | 4 ajustes | Media |

---

## ✅ Fase 1: COMPLETADA (2026-03-15)

> **Resumen**: Todos los ajustes de contenido sin dependencias de imágenes han sido implementados exitosamente. Se realizaron 4 commits con cambios en 4 archivos.

### Commits realizados en Fase 1:
| Commit | Descripción |
|--------|-------------|
| `7705b59` | Actualizar biografía y descripción de talleres en inicio |
| `094ff37` | Actualizar página Sobre mí - texto, redes y perfil |
| `5c14640` | Actualizar página Libro - citas, temáticas y nota de autora |
| `8a8bf9e` | Actualizar página Servicios - terapias y talleres |

### 1.1 Inicio (`src/pages/index.astro`) ✅

- [x] **Biografía**: Reemplazar texto actual por:
  ```
  Terapeuta holística, coach espiritual y escritora.
  Acompaño procesos de autoconocimiento y crecimiento interior a través de terapias, talleres y cursos.
  Dirijo las mentorías de escritura "Autoras con Propósito" y la comunidad espiritual "Confío y Creo en Mí", espacios dedicados al desarrollo personal y la vida consciente.
  ```

- [x] **Talleres y cursos**: Reemplazar descripción en tarjeta correspondiente:
  ```
  Formación en crecimiento espiritual, canalización, escritura creativa y terapéutica, y herramientas prácticas para la vida consciente.
  ```

**Commit realizado**: `7705b59` - content: Actualizar biografía y descripción de talleres en inicio

---

### 1.2 Sobre mí (`src/pages/sobre-mi.astro`) ✅

- [x] **Frase flotante**: Cambiar de "Mi voz es el puente." a "Tu voz es el puente"

- [x] **Links a redes sociales**: Actualizar en hero y en sección de contacto:
  - YouTube: `@adricrisrueda` (cambiar de `@adricrisespiritual`)
  - Facebook: `adricrisrueda` (cambiar de `adricrisespiritual`)
  - Instagram: `adricrisrueda` (ya está correcto)
  - ~~LinkedIn~~: Eliminar
  - ~~TikTok~~: No agregar

- [x] **Sección "Mi camino"**: Reemplazar texto completo:
  ```
  Durante varios años mi vida estuvo dedicada a la arquitectura, los planos y las estructuras concretas. Como arquitecta y profesional en Tecnologías de Información, me movía en un mundo donde el orden, la lógica y la precisión eran fundamentales. Con el tiempo empecé a sentir un interés cada vez más profundo por el mundo interior y por las preguntas que surgen cuando una persona busca comprenderse a sí misma más allá de lo visible. Ese proceso me llevó a explorar distintos caminos de crecimiento personal y espiritual, y poco a poco fui integrando estas experiencias en mi vida y en mi forma de acompañar a otros. Hoy, como terapeuta holística y coach espiritual, facilito espacios de reflexión y acompañamiento a través de terapias, talleres y procesos de crecimiento personal. En mi trabajo integro prácticas de sanación energética, intuición y escritura como caminos de conexión interior y transformación personal.
  ```

- [x] **Íconos de perfil**: 
  - Cambiar "Arquitecta" por "Mujer real" (texto del ícono)
  - Cambiar "Guía Espiritual" por "Coach Espiritual"
  - Evaluar cuál queda mejor visualmente

- [x] **Quitar texto "Arquitecta de sueños"**: Eliminar overlay de la imagen lateral

- [x] **Sección "Continuemos la conversación":
  - Cambiar "tu propia arquitectura interior" por "tu voz interior"
  - Actualizar links a redes (mismos que en hero)

**Commit realizado**: `094ff37` - content: Actualizar página Sobre mí - texto, redes y perfil

---

### 1.3 Libro (`src/pages/libro.astro`) ✅

- [x] **Sección de cita (blockquote)**:
  - Quitar el `format_quote` de abajo (solo mantener el de arriba)
  - Reemplazar frase por:
    ```
    "La voz no aparece cuando termina el eclipse, sino cuando entendemos que la luz nunca se fue."
    ```
  - O alternativa (si prefiere): 
    ```
    "Por primera vez entendí que toda mi vida había intentado mirar hacia afuera para encontrar respuestas que solo estaban dentro."
    ```

- [x] **Temáticas centrales**:
  - Cambiar "una misma" por "uno mismo"
  - Reemplacer ítem "Renacimiento" por:
    ```
    Elecciones conscientes: Habitar la certeza de que la vida no es un viaje lineal, sino una serie de decisiones que nos acercan a nuestra identidad y autenticidad.
    ```

- [x] **Sección "La esencia terapéutica"**: Reemplazar texto completo:
  ```
  "Escribir Una Voz al Paso del Eclipse no fue solo un ejercicio literario, sino un acto de confrontación. En la historia de Natalia quise plasmar procesos que veo a diario en mi consulta y que también he vivido en mi propia piel.

  El eclipse es una metáfora central en esta historia. Hay momentos en la vida en los que ciertas experiencias proyectan una sombra que parece ocultar nuestra luz. Pero, como ocurre con el sol durante un eclipse, la luz no desaparece: sigue allí.

  Este libro es una invitación a recordarlo. A reconocer que esas sombras no borran nuestra identidad, y que atravesarlas puede convertirse en el momento en que volvemos a escuchar con claridad nuestra propia voz."
  ```

**Commit realizado**: `5c14640` - content: Actualizar página Libro - citas, temáticas y nota de autora

---

### 1.4 Servicios (`src/pages/servicios.astro`) ✅

- [x] **Quitar "Activación pineal"** de la descripción de Terapia

- [x] **Íconos de servicios**:
  - Cambiar "Reiki Usui" → "Reiki Intuitivo"
  - Cambiar "Glándula Pineal" → "Conversaciones canalizadas"

- [x] **Talleres**: Reemplazar tarjeta "Activación Pineal" por:
  - **Título**: Respiración consciente
  - **Descripción**: Prácticas diarias para cultivar tranquilidad, enfoque y presencia.
  - **Ícono**: Usar apropiado (ej. `air` o `self_improvement`)

**Commit realizado**: `8a8bf9e` - content: Actualizar página Servicios - terapias y talleres

---

## 🖼️ Fase 2: Cambios que dependen de imágenes nuevas

### 2.1 Sobre mí
- [ ] **Cambiar fotos por reales** (pendiente recepción)
  - Hero: Imagen principal
  - Sección biografía: Imagen lateral
  - [ ] Optimizar imágenes (formato WebP si es posible)
  - [ ] Agregar alt text descriptivo

### 2.2 Servicios
- [ ] **Cambiar foto de terapia** (pendiente recepción)
  - [ ] Optimizar imagen
  - [ ] Actualizar alt text

**Commit sugerido**: `assets: Actualizar fotos a imágenes reales en Sobre mí y Servicios`

---

## 📚 Fase 3: Reorganización de Biblioteca

### 3.1 Página Libros (`src/pages/libros.astro`)
- [ ] Evaluar si unificar contenido con "Sobre mí" o mantener separado
- [ ] Si se unifica: Agregar "Los árboles que se miraron al espejo (2025)"
- [ ] Agregar portada de antología "Sus huesos y otros cuentos"

### 3.2 Ajustes en Bibliografía (Sobre mí → Libros)
- [ ] **Lazos Escritos**:
  - Cambiar "Antología" → "Obra autobiográfica + contenido canalizado"
  - Quitar texto actual (incorrecto)
  - Nuevo texto: "Este libro es una guía para quienes atraviesan sus propios procesos de transformación."

- [ ] **Agregar nuevo libro**: "Los árboles que se miraron al espejo (2025)"
  - Descripción: "Una fábula que explora el valor de habitar la identidad en medio de las diferencias. Incluido en la antología Sus huesos y otros cuentos, del programa Autor de Éxito."
  - Portada: Pendiente

- [ ] **Una voz al paso del eclipse**: Actualizar descripción:
  ```
  "Mi obra más personal. Un recorrido íntimo por situaciones que nos hicieron creer que vivíamos en la oscuridad, cuando en realidad solo necesitábamos reencontrarnos con nuestra propia luz."
  ```

**Commit sugerido**: `content: Reorganizar bibliografía - agregar libro 2025 y corregir Lazos Escritos`

---

## 📋 Orden de Ejecución Recomendado

### Hoy (sin bloqueos):
1. Fase 1.1 - Inicio
2. Fase 1.2 - Sobre mí (sin fotos)
3. Fase 1.3 - Libro
4. Fase 1.4 - Servicios (sin fotos)
5. Fase 3 - Biblioteca

### Cuando lleguen las fotos:
6. Fase 2.1 - Fotos Sobre mí
7. Fase 2.2 - Foto Servicios

---

## 📝 Notas de Implementación

### Cambio de "Guía Espiritual" → "Coach Espiritual"
- Evaluar visualmente cuál queda mejor en el diseño
- "Coach" puede sonar más moderno/profesional
- "Guía" puede sonar más místico/espiritual
- **Decisión**: El usuario prefiere "Coach" para no sonar como "gurú"

### Redes Sociales
- YouTube: `@adricrisrueda` (antes `@adricrisespiritual`)
- Facebook: `adricrisrueda` (antes `adricrisespiritual`)
- Instagram: `adricrisrueda` (sin cambios)

### Libro nuevo 2025
- Título: "Los árboles que se miraron al espejo"
- Tipo: Fábula en antología
- Antología: "Sus huesos y otros cuentos"
- Programa: Autor de Éxito

---

## ✅ Checklist Final

Antes de marcar como completado:
- [ ] Todas las Fases 1 ejecutadas y commiteadas
- [ ] Fotos recibidas y optimizadas
- [ ] Fases 2 ejecutadas
- [ ] Build exitoso (`npm run build`)
- [ ] Revisión visual en desktop y mobile
- [ ] Links de redes verificados
- [ ] Ortografía revisada

---

> **Última actualización**: 2026-03-15  
> **Próxima revisión**: Al recibir fotos
