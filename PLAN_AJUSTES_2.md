# Plan de Ajustes 2 - Reorganización Completa

> **Fecha**: 2026-03-15  
> **Estado**: Planificación  
> **Basado en**: Lineamientos de Adriana (audios 5-marzo)

---

## 📋 Resumen Ejecutivo

Reorganización completa de la bibliografía y la página Sobre mí:
1. **Corregir orden de libros** según cronología real
2. **Clarificar** que "Los árboles..." es un cuento, no un libro
3. **Unificar** sección de libros en Biblioteca
4. **Crear** sección Testimonios/Entrevistas en Sobre mí
5. **Agregar** podcast de Spotify

---

## 📚 Orden Correcto de Obras

| Orden | Título | Año | Tipo | Descripción |
|-------|--------|-----|------|-------------|
| 1 | Lazos Escritos | 2023 | Libro | Obra autobiográfica + contenido canalizado |
| 2 | Los árboles que se miraron al espejo | 2025 | **Cuento** | Fábula en antología "Sus huesos y otros cuentos" |
| 3 | Una Voz al paso del Eclipse | 2026 | Libro | Novela de crecimiento espiritual |

### Corrección Importante
- ❌ "Los árboles..." NO es un libro independiente
- ✅ Es un **cuento** dentro de la antología "Sus huesos y otros cuentos"
- ✅ Programa: Autor de Éxito

---

## 🎯 Fase A: Biblioteca (`libros.astro`)

### A.1 Reestructurar catálogo completo

**Nueva estructura:**

#### Libro 1: Lazos Escritos (2023)
- **Portada**: `/images/lazos-escritos.png`
- **Tipo**: Libro
- **Género**: Obra autobiográfica + contenido canalizado
- **Texto**: 
  > "Una primera inmersión en el mundo editorial. Este libro es una guía para quienes atraviesan sus propios procesos de transformación."

#### Libro 2: Sus Huesos y Otros Cuentos (2025)
- **Portada**: `/images/sus-huesos-antologia.jpg` ✅ NUEVA
- **Tipo**: Antología
- **Contiene**: Cuento "Los árboles que se miraron al espejo"
- **Género**: Fábula
- **Texto cuento**:
  > "Una fábula que explora el valor de habitar la identidad en medio de las diferencias."
- **Programa**: Autor de Éxito
- **Diploma**: `/images/sus-huesos-diploma.jpg` ✅ NUEVA

#### Libro 3: Una Voz al Paso del Eclipse (2026)
- **Portada**: `/images/portada-libro-2.png`
- **Tipo**: Libro
- **Género**: Crecimiento Espiritual
- **Texto**:
  > "Mi obra más personal. Un recorrido íntimo por situaciones que nos hicieron creer que vivíamos en la oscuridad, cuando en realidad solo necesitábamos reencontrarnos con nuestra propia luz."
- **Lanzamiento**: 11 de abril 2026 - Feria del Libro de Bogotá

### A.2 Diseño de sección "Sus Huesos"
- Layout especial que muestre:
  - Portada de la antología (principal)
  - Mención del cuento "Los árboles..."
  - Logo/diploma del programa Autor de Éxito
  - Fecha: 31 octubre 2025

**Commit sugerido**: `content: Reestructurar Biblioteca con orden correcto de obras`

---

## 🎯 Fase B: Sobre Mí (`sobre-mi.astro`)

### B.1 Quitar sección "Mi Viaje Literario" completa
- Eliminar todo el `<section id="libros">` (líneas ~177-240)
- Esta sección se mueve completamente a Biblioteca

### B.2 Crear nueva sección: Testimonios y Entrevistas

**Ubicación**: Después de la sección de biografía (reemplaza libros)

#### Estructura propuesta:

```
# Testimonios y Entrevistas

## Lo que dicen de mi trabajo
[Grid de testimonios - esperando contenido]

## Entrevistas y Medios
[Cards con entrevistas]
```

#### Entrevista 1: Podcast Spotify
- **Título**: [Nombre del podcast]
- **Fuente**: Spotify
- **Link**: https://open.spotify.com/episode/70yA6Lh3IXwmAq138Tp9ga?si=kTbAZpTPTRqN0YSXNaq9Og
- **Embed**: Usar iframe de Spotify
- **Imagen**: Icono/podcast genérico o captura

#### Entrevista 2: [Pendiente - Adriana mencionó otra entrevista]
- Esperando información

### B.3 Testimonios (Pendientes)
- Esperando que Adriana envíe los testimonios que habían mencionado
- Diseño: Tarjetas con foto, nombre, texto y estrellas

**Commit sugerido**: `content: Reemplazar libros por Testimonios y Entrevistas en Sobre mí`

---

## 🎯 Fase C: Correcciones en Index (Home)

### C.1 Sección Libro (Lazos Escritos)
Si hay mención a "Los árboles..." en el home, corregir para que sea consistente.

**Revisar**: Que el home solo promocione los LIBROS principales, no la antología.

---

## 🎯 Fase D: Imágenes Nuevas

### D.1 Imágenes copiadas ✅
```
public/images/
├── sus-huesos-antologia.jpg     (Portada antología)
└── sus-huesos-diploma.jpg       (Diploma Autor de Éxito)
```

### D.2 Optimización
- [ ] Verificar tamaño de imágenes
- [ ] Comprimir si es necesario
- [ ] Agregar alt text descriptivo

**Commit sugerido**: `assets: Agregar imágenes de antología Sus Huesos y diploma`

---

## 📋 Orden de Ejecución

### Paso 1: Imágenes y Biblioteca
1. ✅ Copiar imágenes (hecho)
2. Reestructurar `libros.astro`
3. Commit

### Paso 2: Sobre Mí
1. Quitar sección libros
2. Crear sección Testimonios/Entrevistas
3. Agregar embed de Spotify
4. Commit

### Paso 3: Revisión y ajustes
1. Revisar consistencia en todo el sitio
2. Verificar links
3. Build y test

---

## 📝 Notas de Implementación

### Spotify Embed
```html
<iframe 
  src="https://open.spotify.com/embed/episode/70yA6Lh3IXwmAq138Tp9ga" 
  width="100%" 
  height="232" 
  frameBorder="0" 
  allowfullscreen="" 
  allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
></iframe>
```

### Antología "Sus Huesos"
- Fecha del diploma: 31 octubre 2025
- Autora reconocida: Adriana Cristina Rueda Sañudo
- Obra: "Los árboles que se miraron al espejo"
- Programa: Autor de Éxito (Alexandra Castrillón Gómez)

### Estrategia de Diseño
- La antología debe mostrarse diferente a los libros
- Usar badge "Antología" vs "Libro"
- Destacar que es parte del programa Autor de Éxito
- Quizás mostrar el diploma como certificación

---

## ❓ Preguntas Pendientes para Adriana

1. **Testimonios**: ¿Nos envías los testimonios para agregar?
2. **Entrevistas**: ¿Tienes más entrevistas además del podcast?
3. **Info del podcast**: ¿Cuál es el título/nombre del episodio?
4. **Fotos**: ¿Aún nos debes fotos reales para Sobre mí y Servicios?

---

## ✅ Checklist

- [ ] Reestructurar Biblioteca (libros.astro)
- [ ] Agregar antología Sus Huesos
- [ ] Quitar sección libros de Sobre mí
- [ ] Crear sección Testimonios
- [ ] Agregar podcast Spotify
- [ ] Optimizar imágenes nuevas
- [ ] Verificar consistencia en todo el sitio
- [ ] Build exitoso
- [ ] Commit de imágenes
- [ ] Commit de cambios de contenido

---

> **Nota**: Este plan está basado en los audios del 5 de marzo. Ajustar según nuevas indicaciones.
