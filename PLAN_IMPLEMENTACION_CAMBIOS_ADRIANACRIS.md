# 📋 PLAN COMPLETO DE IMPLEMENTACIÓN
## Modificaciones Página Web - AdriCris Rueda | Vida Consciente

> **Fecha**: Abril 2026  
> **Proyecto**: adricrisrueda.com  
> **Stack**: Astro 5 + Tailwind CSS 3.4  

---

## 🎯 RESUMEN EJECUTIVO

Este plan detalla la implementación completa de las modificaciones solicitadas por Adriana para su sitio web, incluyendo cambios de contenido, fotografías, reorganización de secciones y mejoras UX/UI.

### 📁 Archivos Recibidos

**Fotografías** (5 archivos):
| Archivo | Uso | Destino |
|---------|-----|---------|
| `AdriCris Rueda bio1 .jpg.jpeg` | Foto blusa blanca (busto) | Página Sobre Mí - Hero |
| `Adri4.jpg.jpeg` | Foto blusa roja/fucsia | Página Libro - Notas de la autora |
| `AdriCris Rueda _ 4.jpg.jpeg` | Foto sentada blusa blanca | Página Servicios |
| `Utrilla_FILBo2026_publicidad_2.jpg` | Afiche oficial FilBo 2026 | Página Libro - Sección FilBo |
| `20260330_195145_0000.png` | Foto alternativa sentada | Reserva |

**Documentos** (2 archivos):
| Archivo | Uso | Ubicación |
|---------|-----|-----------|
| `30 tips de vida.pdf` | Lead magnet newsletter | `/public/downloads/30-tips-vida.pdf` |
| `UNA VOZ AL PASO DEL ECLIPSE...pdf` | Capítulo muestra | `/public/downloads/capitulo-muestra.pdf` |

---

## 🗂️ FASES DE IMPLEMENTACIÓN

---

## ✅ FASE 1: PREPARACIÓN Y OPTIMIZACIÓN DE ASSETS

### 1.1 Optimización de Imágenes

**Técnica**: Uso de skill de procesamiento de imágenes + Sharp (si disponible)

| Imagen Original | Versión Web | Versión Retina | Formato |
|-----------------|-------------|----------------|---------|
| bio1.jpg (1794×2394) | 600×800 | 1200×1600 | WebP + JPEG fallback |
| Adri4.jpg (1908×3392) | 800×1200 | 1600×2400 | WebP + JPEG fallback |
| _4.jpg (2244×3398) | 800×1200 | 1600×2400 | WebP + JPEG fallback |
| FilBo2026.jpg (4501×6001) | 1200×1600 | 2400×3200 | WebP + JPEG fallback |

**Optimizaciones aplicadas**:
- Compresión sin pérdida visible (calidad 85%)
- Conversión WebP con fallback JPEG
- Generación de versiones @2x para retina
- Metadatos GPS eliminados
- Alt text SEO-friendly

### 1.2 Configuración de Archivos PDF

```
public/downloads/
├── 30-tips-vida.pdf (Lead magnet)
├── capitulo-muestra.pdf (Muestra del libro)
└── politica-privacidad.pdf (Nuevo - crear)
```

### 1.3 Crear Página de Política de Privacidad

**Ruta**: `/privacidad` → `src/pages/privacidad.astro`

Basada en referencia: alexandracastrillon.com
Contenido:
- Responsable del tratamiento
- Datos recopilados
- Finalidad del tratamiento
- Derechos de los titulares
- Cookies y tracking
- Contacto DPO

---

## ✅ FASE 2: MODIFICACIONES GLOBALES

### 2.1 Cambio de "Pre-lanzamiento" → Disponible

**Ubicaciones a modificar**:
1. `src/pages/index.astro` (Línea 32): Badge "Nuevo Lanzamiento" → "Disponible"
2. `src/pages/index.astro` (Línea 48): Botón "PRE-ORDENAR LIBRO" → "COMPRAR LIBRO"
3. `src/pages/libro.astro` (Línea 59): Badge lanzamiento
4. `src/pages/libros.astro` (Línea 74): Badge "Nuevo"
5. `src/pages/libro.astro` (Línea 229): "Pre-Registrarse" → "Compra anticipada"

**Nota**: Amazon sigue siendo Mayo 2026, pero venta nacional ya está activa.

### 2.2 Incremento de Tamaños de Fuente Global

**Archivo**: `src/styles/global.css`

```css
/* Agregar al final del archivo */
@layer base {
  /* Aumentar tamaño base de texto */
  body {
    @apply text-base md:text-lg;
  }
  
  /* Subtítulos de sección más grandes */
  .section-subtitle {
    @apply text-sm md:text-base tracking-[0.3em];
  }
  
  /* Texto de párrafos en secciones */
  .section-body {
    @apply text-base md:text-lg leading-relaxed;
  }
}
```

---

## ✅ FASE 3: PÁGINA INICIO (`src/pages/index.astro`)

### 3.1 Aumentar Tamaño de Fuente de Textos Generales

**Cambios**:
- Línea 40: `text-lg` → `text-xl md:text-2xl`
- Línea 131-143: Párrafos bio aumentar a `text-base md:text-lg`
- Línea 193-200: Párrafos de libro aumentar

### 3.2 Cuadro Biografía - Formato "Confío y Creo en Mí"

**Ubicación**: Línea 139

**Actual**:
```html
<em class="text-gray-800 dark:text-gray-200">"Confío y Creo en Mí"</em>
```

**Nuevo** (mismo formato que "Autoras con Propósito"):
```html
<strong class="text-secondary font-display text-lg">"Confío y Creo en Mí"</strong>
```

### 3.3 Subtítulos Más Grandes

**Ubicación**: Línea 105
```html
<!-- DE -->
<span class="text-secondary font-bold tracking-[0.3em] uppercase text-xs block mb-4">La Guía</span>

<!-- A -->
<span class="text-secondary font-bold tracking-[0.3em] uppercase text-sm md:text-base block mb-4">La Guía</span>
```

### 3.4 Sección Obra Destacada - Mover a Biblioteca

**Acción**: ELIMINAR toda la sección "Book Section" (Líneas 150-238) de index.astro

**Contenido a migrar**:
- Texto completo nuevo de Lazos Escritos
- Características del libro
- Botones de compra

### 3.5 Nueva Sección Lazos Escritos en Biblioteca

**Texto completo nuevo** (para `libros.astro`):

```
Mi primera obra, Lazos Escritos (2023), presenta una guía de cinco pasos, basada en mi proceso de despertar de consciencia, partiendo desde la "noche oscura del alma", hasta lograr convertir esos momentos de vulnerabilidad en la base del propósito de vida.

La conexión espiritual se convierte en una fuente de claridad y serenidad, que invita a vivir con mayor presencia. Además, contiene cuarenta mensajes canalizados, de Jesús, María y los Ángeles.

Con este libro, mi mensaje ha llegado a lectores en diversos países, invitándolos a descubrir su propia voz interior y camino de sanación.
```

### 3.6 Foto del Libro Más Pequeña

En la nueva sección de Biblioteca:
```html
<!-- DE -->
class="w-[320px] md:w-[420px]"

<!-- A -->
class="w-[240px] md:w-[320px]"
```

### 3.7 Servicios Holísticos - Redireccionar a /servicios

**Verificar** que todos los links de servicios apunten a `/servicios`:
- Línea 267: Terapia Holística
- Línea 284: Talleres y Cursos
- Línea 301: Comunidad
- Línea 309: "VER TODO EL CATÁLOGO"

### 3.8 Sección Newsletter - Mejoras

**Ubicación**: Líneas 316-343

#### 3.8.1 Logo de Carta Más Grande
```html
<!-- DE -->
<span class="material-symbols-outlined text-6xl text-secondary mb-6 block mx-auto animate-bounce">mark_email_unread</span>

<!-- A -->
<span class="material-symbols-outlined text-7xl md:text-8xl text-secondary mb-6 block mx-auto animate-bounce">mark_email_unread</span>
```

#### 3.8.2 Campo Nombre + Correo
```html
<form class="flex flex-col gap-4 justify-center max-w-lg mx-auto">
  <input 
    type="text" 
    name="nombre"
    placeholder="Tu nombre" 
    class="w-full px-8 py-4 rounded-full text-gray-900 bg-surface-light focus:ring-2 focus:ring-secondary focus:outline-none border-none shadow-xl font-light placeholder-gray-400"
    required
  />
  <input 
    type="email" 
    name="email"
    placeholder="Tu correo electrónico" 
    class="w-full px-8 py-4 rounded-full text-gray-900 bg-surface-light focus:ring-2 focus:ring-secondary focus:outline-none border-none shadow-xl font-light placeholder-gray-400"
    required
  />
  <!-- Checkbox términos -->
  <label class="flex items-start gap-3 text-left">
    <input type="checkbox" required class="mt-1 w-5 h-5 rounded border-gray-300 text-secondary focus:ring-secondary">
    <span class="text-sm text-white/80">
      Acepto el tratamiento de mis datos personales según la 
      <a href="/privacidad" class="underline hover:text-secondary">Política de Privacidad</a>
    </span>
  </label>
  <button type="submit" class="bg-secondary text-primary font-bold px-10 py-4 rounded-full hover:bg-white transition-colors shadow-lg shadow-secondary/30">
    SUSCRIBIRME
  </button>
</form>
```

#### 3.8.3 Integración con Kinto CMS para Formularios

**Configuración propuesta**:
```javascript
// scripts/newsletter-subscription.js
// Envío a Kinto CMS o servicio de email

async function subscribeNewsletter(data) {
  const response = await fetch('/api/subscribe', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      nombre: data.nombre,
      email: data.email,
      source: 'homepage_newsletter',
      tags: ['vida-consciente', 'newsletter'],
      // Lead magnet: PDF 30 tips
      downloadUrl: '/downloads/30-tips-vida.pdf'
    })
  });
  
  if (response.ok) {
    // Redirigir a descarga del PDF
    window.open('/downloads/30-tips-vida.pdf', '_blank');
    alert('¡Gracias! Revisa tu correo para confirmar la suscripción.');
  }
}
```

**Alternativa simple**: Formspree o Google Forms con redirección a descarga.

### 3.9 Link "Mis Libros" → Biblioteca

**Ubicación**: Footer o sección final (verificar en Layout.astro)

Asegurar que el link apunte a `/libros` en lugar de `/libro`.

---

## ✅ FASE 4: PÁGINA SOBRE MÍ (`src/pages/sobre-mi.astro`)

### 4.1 Cambiar Primera Foto (Hero)

**Ubicación**: Línea 65-72

**Cambio**:
```html
<!-- DE -->
src="/images/adriana-bio.png"

<!-- A -->
src="/images/adriana-bio-blusa-blanca.webp"
alt="Adriana Cristina Rueda Sañudo — Terapeuta Holística y Autora, Bogotá Colombia"
```

### 4.2 Actualizar Entrevista Spotify

**Ubicación**: Línea 256-276

**Nuevo contenido**:
```html
<div class="flex-grow text-center md:text-left">
  <span class="text-xs text-gray-400 uppercase tracking-wider">Podcast "Viviendo en plenitud"</span>
  <h4 class="font-display text-xl text-primary dark:text-white mb-2">
    La física cuántica: ¿qué es y cómo puede ayudarnos a sanar?
  </h4>
  <p class="text-gray-500 font-light text-sm mb-4">
    Descubre cómo transformar una experiencia cercana a la muerte en propósito de vida. Una charla sobre sanación cuántica y crecimiento personal para alcanzar el autoconocimiento, la plenitud y la certeza.
  </p>
  <div class="flex flex-col sm:flex-row gap-3">
    <a href="https://open.spotify.com/episode/70yA6Lh3IXwmAq138Tp9ga" 
       target="_blank" rel="noopener noreferrer" 
       class="inline-flex items-center gap-2 text-[#1DB954] hover:text-[#1ed760] font-medium transition-colors">
      <span class="material-symbols-outlined text-base">play_circle</span>
      Escuchar en Spotify
    </a>
    <a href="https://youtu.be/_31gXvzdGZk" 
       target="_blank" rel="noopener noreferrer" 
       class="inline-flex items-center gap-2 text-[#FF0000] hover:text-[#ff3333] font-medium transition-colors">
      <span class="material-symbols-outlined text-base">play_circle</span>
      Ver en YouTube
    </a>
  </div>
</div>
```

### 4.3 Adicionar Entrevista YouTube

**Nueva entrevista después de Spotify**:

```html
<!-- YouTube Interview -->
<div class="mt-8 max-w-3xl mx-auto bg-white dark:bg-surface-dark rounded-2xl p-8 shadow-lg border border-gray-100 dark:border-gray-800">
  <div class="flex flex-col md:flex-row items-center gap-6">
    <div class="w-20 h-20 rounded-full bg-[#FF0000] flex items-center justify-center flex-shrink-0">
      <svg class="w-10 h-10 text-white" viewBox="0 0 24 24" fill="currentColor">
        <path d="M19.812 5.418c.861.23 1.538.907 1.768 1.768C21.998 8.746 22 12 22 12s0 3.255-.418 4.814a2.504 2.504 0 0 1-1.768 1.768c-1.56.419-7.814.419-7.814.419s-6.255 0-7.814-.419a2.505 2.505 0 0 1-1.768-1.768C2 15.255 2 12 2 12s0-3.255.417-4.814a2.507 2.507 0 0 1 1.768-1.768C5.744 5 11.998 5 11.998 5s6.255 0 7.814.418ZM15.194 12 10 15V9l5.194 3Z"/>
      </svg>
    </div>
    <div class="flex-grow text-center md:text-left">
      <span class="text-xs text-gray-400 uppercase tracking-wider">YouTube</span>
      <h4 class="font-display text-xl text-primary dark:text-white mb-2">
        Atravesar la incertidumbre sin huir de ti
      </h4>
      <p class="text-gray-500 font-light text-sm mb-4">
        Una conversación sobre cómo enfrentar los momentos de incertidumbre desde la consciencia y el autoconocimiento.
      </p>
      <a href="https://youtu.be/YP15Bo31ZjA" 
         target="_blank" rel="noopener noreferrer" 
         class="inline-flex items-center gap-2 text-[#FF0000] hover:text-[#ff3333] font-medium transition-colors">
        <span class="material-symbols-outlined text-base">play_circle</span>
        Ver en YouTube
      </a>
    </div>
  </div>
</div>
```

---

## ✅ FASE 5: PÁGINA BIBLIOTECA (`src/pages/libros.astro`)

### 5.1 Quitar Sección Libro Nuevo (Hero duplicado)

**Acción**: Eliminar sección "Featured Book Section" completa (Líneas 57-111)

### 5.2 Frase de Franja Verde - Mover Arriba

**La frase actual**:
> "Cada libro es un peldaño en la escalera hacia la consciencia..."

**Mantener** en el hero principal (ya está bien ubicada).

### 5.3 Sección Lazos Escritos - Información Completa

**Reemplazar** la tarjeta actual de Lazos Escritos (Líneas 140-163) con formato completo:

```html
<!-- Lazos Escritos - Versión Extendida -->
<div class="bg-white dark:bg-surface-dark rounded-3xl p-8 lg:p-12 shadow-xl hover:shadow-2xl transition-shadow duration-300 border border-gray-100 dark:border-gray-800 flex flex-col lg:flex-row gap-12 items-center">
  <!-- Imagen más pequeña -->
  <div class="w-40 md:w-48 flex-shrink-0 perspective-1000 relative">
    <div class="absolute inset-0 bg-secondary/20 blur-2xl rounded-full group-hover:bg-secondary/30 transition-colors"></div>
    <div class="aspect-[2/3] rounded shadow-lg flex items-center justify-center relative z-10 transform group-hover:rotate-y-6 transition-transform duration-500 border border-gray-200 dark:border-gray-700 overflow-hidden">
      <img src="/images/lazos-escritos.png" 
           alt="Portada Lazos Escritos — libro 2023 de Adriana Cristina Rueda Sañudo" 
           class="w-full h-full object-cover" loading="lazy" decoding="async" />
    </div>
  </div>
  
  <!-- Contenido extendido -->
  <div class="flex-grow text-center lg:text-left">
    <div class="flex items-center justify-center lg:justify-start gap-3 mb-2">
      <span class="text-secondary font-bold text-sm">2023</span>
      <span class="px-2 py-0.5 bg-secondary/10 text-secondary text-xs font-bold uppercase tracking-wider rounded">Libro</span>
    </div>
    <h3 class="font-display text-3xl text-primary dark:text-white mb-4">Lazos Escritos</h3>
    
    <!-- Texto completo nuevo -->
    <div class="prose dark:prose-invert text-gray-600 dark:text-gray-300 font-light mb-6 text-left">
      <p class="mb-4">
        Mi primera obra, <em>Lazos Escritos (2023)</em>, presenta una guía de cinco pasos, basada en mi proceso de despertar de consciencia, partiendo desde la "noche oscura del alma", hasta lograr convertir esos momentos de vulnerabilidad en la base del propósito de vida.
      </p>
      <p class="mb-4">
        La conexión espiritual se convierte en una fuente de claridad y serenidad, que invita a vivir con mayor presencia. Además, contiene cuarenta mensajes canalizados, de Jesús, María y los Ángeles.
      </p>
      <p>
        Con este libro, mi mensaje ha llegado a lectores en diversos países, invitándolos a descubrir su propia voz interior y camino de sanación.
      </p>
    </div>
    
    <!-- Features -->
    <div class="space-y-3 mb-6">
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-secondary">auto_awesome</span>
        <span class="text-sm text-gray-600 dark:text-gray-300">40 mensajes canalizados</span>
      </div>
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-secondary">menu_book</span>
        <span class="text-sm text-gray-600 dark:text-gray-300">Guía de 5 pasos de transformación</span>
      </div>
    </div>
    
    <!-- Botones -->
    <div class="flex flex-col sm:flex-row gap-4">
      <a href="https://www.amazon.com/dp/B0CK3ZWGJN" target="_blank" rel="noopener noreferrer" 
         class="gold-gradient text-primary px-6 py-3 rounded-full font-bold text-sm shadow-md hover:shadow-lg transition-all inline-flex items-center justify-center gap-2">
        COMPRAR EN AMAZON
        <span class="material-symbols-outlined text-base">shopping_bag</span>
      </a>
      <a href="https://wa.me/573132979675?text=Hola%2C%20me%20interesa%20comprar%20el%20libro%20Lazos%20Escritos" 
         target="_blank" rel="noopener noreferrer"
         class="bg-green-500 hover:bg-green-600 text-white px-6 py-3 rounded-full font-bold text-sm transition-all inline-flex items-center justify-center gap-2">
        COMPRAR POR WHATSAPP
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967..."/></svg>
      </a>
    </div>
  </div>
</div>
```

### 5.4 Sección "Los árboles que se miraron al espejo"

**Mantener** la tarjeta actual de "Sus Huesos y Otros Cuentos" pero:
- **Agrandar imagen del diploma** (Línea 185)
```html
class="w-24 h-16 object-cover rounded"  <!-- DE -->
class="w-32 h-20 object-cover rounded"  <!-- A -->
```

### 5.5 Libro Nuevo - Conservar Formato

**Mantener** tarjeta de "Una Voz al Paso del Eclipse" (Líneas 191-215) con:
- Botón "PRE-ORDENAR" → "VER LIBRO"
- Link a `/libro`

---

## ✅ FASE 6: PÁGINA LIBRO (`src/pages/libro.astro`)

### 6.1 Lanzamiento - Actualizar Fechas

**Ubicación**: Línea 59

**Cambio**:
```html
<!-- DE -->
<span class="text-primary dark:text-secondary text-xs font-bold tracking-[0.2em] uppercase">Lanzamiento: 11 de Abril 2026</span>

<!-- A -->
<span class="text-primary dark:text-secondary text-xs font-bold tracking-[0.2em] uppercase">Lanzamiento Presencial: Feria del Libro de Bogotá</span>
```

### 6.2 Nueva Sinopsis

**Reemplazar** sección sinopsis completa (Líneas 99-131):

```html
<section class="py-24 md:py-32 bg-white dark:bg-surface-dark relative overflow-hidden" id="sinopsis">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="flex flex-col lg:flex-row gap-16 lg:gap-24">
      <div class="lg:w-1/2 space-y-8">
        <span class="text-secondary font-bold tracking-[0.3em] uppercase text-xs block mb-2">Sinopsis</span>
        <h2 class="font-display text-4xl md:text-5xl text-primary dark:text-white leading-tight">
          Una Voz al Paso <span class="italic text-accent">del Eclipse</span>
        </h2>
        <div class="prose dark:prose-invert text-gray-600 dark:text-gray-300 font-light text-lg leading-relaxed space-y-6">
          <p>
            Natalia, una mujer de cincuenta años que hace tiempo dejó atrás la profesión que la desgastaba, vive sola, en una calma que a veces confunde con plenitud. Durante años ha aprendido a acomodarse a lo que otros esperan de ella, apagando, casi sin notarlo, la parte más luminosa y soñadora de sí misma.
          </p>
          <p>
            Sin embargo, cuando las situaciones adversas de la vida empiezan a confrontarla, comprende que lleva tiempo sosteniendo una paz construida a costa de sí misma.
          </p>
          <p>
            Movida por una incomodidad que ya no puede ignorar, inicia un reencuentro íntimo con la vitalidad que un día tuvo y que abandonó para sobrevivir. En ese proceso, descubre que su mayor obstáculo no es el mundo exterior, sino las lealtades invisibles que la atan a una versión de sí misma que ya no la representa.
          </p>
          <p class="text-accent font-medium italic">
            Una voz al paso del eclipse es una historia que invita a detenerse, mirarse con honestidad y dejar la puerta abierta hacia una vida más auténtica.
          </p>
        </div>
      </div>
      
      <!-- Frase destacada -->
      <div class="lg:w-1/2 flex flex-col justify-center">
        <div class="relative p-10 md:p-14 bg-background-light dark:bg-background-dark rounded-tr-[4rem] rounded-bl-[4rem] shadow-xl border border-secondary/10">
          <span class="material-symbols-outlined absolute top-8 left-8 text-6xl text-secondary/20">format_quote</span>
          <blockquote class="relative z-10 text-center">
            <p class="font-display text-2xl md:text-3xl italic text-primary dark:text-white leading-relaxed mb-6">
              "Mirándome a través de los ojos de Natalia, comprendí que, al recuperar mi verdadera voz, volví a sonreír con la mirada"
            </p>
            <footer class="text-secondary font-display text-lg">— AdriCris Rueda</footer>
          </blockquote>
        </div>
      </div>
    </div>
  </div>
</section>
```

### 6.3 Sección Notas de la Autora - Cambiar Foto

**Ubicación**: Línea 181-187

```html
<!-- DE -->
src="/images/adriana-bio.png"

<!-- A -->
src="/images/adriana-notas-autora.webp"
alt="Adriana Cristina Rueda Sañudo — Notas de la autora de Una Voz al paso del Eclipse"
```

### 6.4 Sección Feria del Libro de Bogotá 2026

**Reemplazar** sección "Comprar" (Líneas 217-247) con nueva sección FilBo:

```html
<!-- Feria del Libro Section -->
<section class="py-24 bg-surface-light dark:bg-surface-dark relative" id="feria">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="text-center mb-12">
      <span class="material-symbols-outlined text-5xl text-accent mb-6 animate-pulse">menu_book</span>
      <h2 class="font-display text-4xl md:text-5xl text-primary dark:text-white mb-6">
        Feria del Libro de Bogotá 2026
      </h2>
      <p class="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto font-light">
        Te espero en la Feria Internacional del Libro de Bogotá para compartir juntas este momento especial.
      </p>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-16">
      <!-- Imagen oficial FilBo -->
      <div class="relative">
        <div class="relative rounded-2xl overflow-hidden shadow-2xl">
          <img src="/images/filbo-2026-oficial.webp" 
               alt="Afiche oficial Feria del Libro de Bogotá 2026 - Adriana Cristina Rueda"
               class="w-full h-auto"
               loading="lazy" decoding="async" />
        </div>
      </div>
      
      <!-- Calendario -->
      <div class="space-y-6">
        <h3 class="font-display text-2xl text-primary dark:text-white mb-4">Calendario de Presentaciones</h3>
        
        <div class="space-y-4">
          <div class="bg-white dark:bg-background-dark p-6 rounded-2xl shadow-lg border-l-4 border-secondary">
            <div class="flex items-start gap-4">
              <div class="bg-secondary/20 p-3 rounded-xl">
                <span class="material-symbols-outlined text-secondary">event</span>
              </div>
              <div>
                <p class="font-bold text-primary dark:text-white">Miércoles 22 de abril</p>
                <p class="text-gray-600 dark:text-gray-300 text-sm">Conversatorio y firma de libros</p>
                <p class="text-accent text-sm font-medium">Gran Salón A</p>
              </div>
            </div>
          </div>
          
          <div class="bg-white dark:bg-background-dark p-6 rounded-2xl shadow-lg border-l-4 border-accent">
            <div class="flex items-start gap-4">
              <div class="bg-accent/20 p-3 rounded-xl">
                <span class="material-symbols-outlined text-accent">event</span>
              </div>
              <div>
                <p class="font-bold text-primary dark:text-white">Jueves 23, sábado 25 de abril y viernes 1° de mayo</p>
                <p class="text-gray-600 dark:text-gray-300 text-sm">Presentaciones y firma de libros</p>
                <p class="text-accent text-sm font-medium">Stand Editorial Utrilla (Área Internacional - Pabellón 17 - Stand 1919)</p>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Lanzamiento Amazon -->
        <div class="bg-primary/5 dark:bg-primary/10 p-6 rounded-2xl border border-primary/20">
          <p class="text-sm text-primary dark:text-accent font-medium mb-2">Lanzamiento Amazon (Internacional)</p>
          <p class="text-gray-600 dark:text-gray-300">Mayo de 2026</p>
        </div>
      </div>
    </div>
    
    <!-- CTA Compra anticipada -->
    <div class="bg-white dark:bg-background-dark rounded-3xl p-8 md:p-12 shadow-xl border border-secondary/20 text-center">
      <span class="material-symbols-outlined text-5xl text-secondary mb-4">local_shipping</span>
      <h3 class="font-display text-3xl text-primary dark:text-white mb-4">Compra Anticipada</h3>
      <p class="text-gray-600 dark:text-gray-300 mb-6 max-w-xl mx-auto">
        ¡Ya tengo stock disponible! Realiza tu compra desde ya y te envío tu ejemplar personalizado. Envíos a todo Colombia.
      </p>
      <a href="https://wa.me/573132979675?text=Hola%20Adri!%20me%20gustaría%20comprar%20tu%20libro%20:)%20" 
         target="_blank" rel="noopener noreferrer"
         class="gold-gradient hover:opacity-90 text-primary px-10 py-4 rounded-full font-display font-bold text-lg shadow-xl hover:shadow-2xl transition-all transform hover:-translate-y-1 inline-flex items-center gap-3">
        <span class="material-symbols-outlined">chat</span>
        COMPRAR POR WHATSAPP
      </a>
    </div>
  </div>
</section>
```

### 6.5 Quitar Sección de Notificaciones

**Eliminar** la sección de notificaciones (la opción de pre-registro) o simplificarla.

---

## ✅ FASE 7: PÁGINA SERVICIOS (`src/pages/servicios.astro`)

### 7.1 Cambiar Foto Hero

**Ubicación**: Línea 83-90

```html
<!-- DE -->
src="/images/adriana-servicios.png"

<!-- A -->
src="/images/adriana-servicios-blusa-blanca.webp"
alt="Adriana Cristina Rueda Sañudo en sesión de terapia holística — Bogotá Colombia"
```

### 7.2 Ocultar Sección Acompañamiento Grupal

**Opción A - Eliminar** (Líneas 209-247)

**Opción B - Comentar/ocultar con CSS**:
```html
<section class="hidden" id="comunidad">
  <!-- Contenido existente -->
</section>
```

**Recomendación**: Opción A (eliminar completamente y mantener en git history).

---

## ✅ FASE 8: TESTING, SEO Y DEPLOY

### 8.1 Checklist de Testing

- [ ] Build exitoso (`npm run build`)
- [ ] No errores de TypeScript
- [ ] Dark mode funciona en todas las páginas
- [ ] Links de WhatsApp funcionan con mensaje correcto
- [ ] Imágenes tienen alt text descriptivo
- [ ] SEOHead incluido en todas las páginas
- [ ] Schema.org válido (test en Google Rich Results)
- [ ] Formulario de newsletter funciona
- [ ] Descarga de PDF funciona
- [ ] Página de privacidad accesible
- [ ] Responsive en mobile, tablet y desktop

### 8.2 SEO Checklist

- [ ] Meta títulos actualizados
- [ ] Meta descripciones 150-160 caracteres
- [ ] Open Graph images correctas
- [ ] Schema.org Book actualizado
- [ ] Schema.org Event para FilBo
- [ ] Breadcrumbs en todas las páginas
- [ ] Sitemap actualizado

### 8.3 Performance Checklist

- [ ] Imágenes WebP con fallback
- [ ] Lazy loading en imágenes debajo del fold
- [ ] Fuentes preloaded
- [ ] Scripts diferidos

### 8.4 Deploy

```bash
npm run build
npm run deploy:static
```

---

## 📊 TIMELINE ESTIMADO

| Fase | Tiempo Estimado |
|------|-----------------|
| Fase 1: Preparación Assets | 2 horas |
| Fase 2: Modificaciones Globales | 1 hora |
| Fase 3: Página Inicio | 3 horas |
| Fase 4: Página Sobre Mí | 2 horas |
| Fase 5: Página Biblioteca | 2 horas |
| Fase 6: Página Libro | 3 horas |
| Fase 7: Página Servicios | 1 hora |
| Fase 8: Testing y Deploy | 2 horas |
| **TOTAL** | **~16 horas** |

---

## 🔧 NOTAS TÉCNICAS ADICIONALES

### Integración Kinto CMS

Si se usa Kinto CMS para el formulario de newsletter:

```javascript
// src/pages/api/subscribe.ts
export const POST: APIRoute = async ({ request }) => {
  const data = await request.json();
  
  // Enviar a Kinto CMS
  const response = await fetch('https://kinto.adricrisrueda.com/v1/buckets/newsletter/collections/subscribers/records', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + import.meta.env.KINTO_API_KEY
    },
    body: JSON.stringify({
      data: {
        nombre: data.nombre,
        email: data.email,
        source: data.source,
        fecha: new Date().toISOString(),
        tags: data.tags
      }
    })
  });
  
  return new Response(JSON.stringify({ success: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
```

### Variables de Entorno

```bash
# .env
KINTO_API_KEY=tu_api_key_aqui
PUBLIC_SITE_URL=https://adricrisrueda.com
```

---

## ✅ RESUMEN DE CAMBIOS POR PÁGINA

| Página | Cambios Principales |
|--------|---------------------|
| **Inicio** | Fuente aumentada, bio reformateada, Lazos Escritos movido a Biblioteca, newsletter mejorado con nombre + términos + lead magnet |
| **Sobre Mí** | Nueva foto hero, entrevista Spotify actualizada, nueva entrevista YouTube añadida |
| **Biblioteca** | Eliminado hero duplicado, Lazos Escritos con info completa, diploma más grande |
| **Libro** | Sinopsis actualizada, frase destacada nueva, foto notas de autora cambiada, sección FilBo con calendario, compra anticipada |
| **Servicios** | Nueva foto, sección comunidad oculta |
| **Nueva** | Página de Política de Privacidad |

---

*Plan creado el 9 de abril de 2026 para Adriana Cristina Rueda Sañudo | Vida Consciente*
