# KIMI.md - Contexto para Kimi Code CLI

> **Proyecto**: AdriCris Rueda | Vida Consciente  
> **Dominio**: https://adricrisrueda.com  
> **Última actualización**: 2026-03-15

---

## 📋 Información General

Este es el sitio web oficial de **Adriana Cristina Rueda Sañudo**, terapeuta holística, autora y guía espiritual con sede en Bogotá, Colombia.

### Identidad de la Marca
- **Nombre comercial**: AdriCris Rueda | Vida Consciente
- **Slogan**: *"Una Voz al paso del Eclipse"*
- **Ubicación**: Bogotá, Colombia
- **Email**: adriana@adricrisrueda.com
- **WhatsApp**: +57 313 297 9675

---

## 🏗️ Stack Tecnológico

| Tecnología | Versión | Uso |
|------------|---------|-----|
| Astro | 5.0 | Framework SSG |
| Tailwind CSS | 3.4 | Estilos utility-first |
| PostCSS | 8.4 | Procesamiento CSS |
| TypeScript | - | Tipado estricto |
| Google Fonts | - | Tenor Sans, Montserrat |
| Material Symbols | - | Iconografía |

### Estructura de Carpetas
```
/
├── src/
│   ├── components/seo/     # SEOHead.astro, SchemaOrg.astro
│   ├── layouts/            # Layout.astro (principal)
│   ├── pages/              # index, sobre-mi, libro, libros, servicios
│   └── styles/             # global.css
├── public/images/          # Imágenes del sitio
├── scripts/                # deploy-static.js
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

---

## 🎨 Sistema de Diseño

### Paleta de Colores (Tailwind)
```javascript
colors: {
  primary: "#0F5257",        // Verde oscuro profundo
  secondary: "#E3B64C",      // Dorado
  accent: "#4F8F8B",         // Verde menta
  "background-light": "#EDEBE8",
  "background-dark": "#0D1B1E",
  "surface-light": "#F7F5F2",
  "surface-dark": "#16262B",
}
```

### Tipografía
- **Display**: `'Tenor Sans', sans-serif` - Títulos
- **Body**: `'Montserrat', sans-serif` - Texto general

### Clases CSS Personalizadas
```css
.text-gradient      /* Gradiente de primary a accent */
.gold-gradient      /* Gradiente dorado 135deg */
.gold-glow          /* Sombra dorada glow */
.organic-border     /* Border-radius orgánico 40% 60%... */
```

### Animaciones
- `animate-blob` - Formas orgánicas morphing
- `animate-float` - Flotación suave Y
- `animate-glow` - Pulso de sombra dorada

---

## 📄 Páginas y Rutas

| Ruta | Archivo | Descripción |
|------|---------|-------------|
| `/` | `index.astro` | Hero libro + bio + servicios + newsletter |
| `/sobre-mi` | `sobre-mi.astro` | Historia completa, transición profesional |
| `/libro` | `libro.astro` | "Una Voz al paso del Eclipse" - pre-registro |
| `/libros` | `libros.astro` | Biblioteca completa (catálogo) |
| `/servicios` | `servicios.astro` | Terapias, talleres, comunidad, FAQ |

### Navegación (Nav)
```
INICIO → SOBRE MÍ → BIBLIOTECA → LIBRO [Nuevo] → SERVICIOS → AGENDAR CONSULTA
```

---

## 👤 Perfil Profesional

### Adriana Cristina Rueda Sañudo
- **Título**: Terapeuta Holística, Autora y Guía Espiritual
- **Background**: Arquitecta y Profesional en Tecnologías de Información
- **Especialidades**: Reiki Usui, Pinealista, Canalizadora

### Creaciones
1. **Método Swami Om Hari** - Auto-sanación emocional canalizada
2. **Comunidad "Confío y Creo en Mí"** - Espacio de apoyo espiritual

### Libros
| Libro | Año | Género | Estado |
|-------|-----|--------|--------|
| Lazos Escritos | 2023 | Antología | Publicado |
| Una Voz al paso del Eclipse | 2026 | Crecimiento Espiritual | Pre-lanzamiento |

---

## 💆 Servicios

### 1. Terapia de Sanación Intuitiva
- Reiki Usui
- Cristaloterapia
- Activación de glándula pineal
- Mensajes canalizados

### 2. Talleres y Cursos
- Método Swami Om Hari
- Activación Pineal
- Escritura Terapéutica

### 3. Comunidad
- Acompañamiento grupal
- Meditaciones en vivo
- Círculos de palabra

---

## 🔍 SEO & AEO (AI Citation Optimization)

### Schema.org Implementados
- `Person` - Perfil de Adriana
- `Organization` / `WebSite` - Marca y sitio
- `LocalBusiness` - Ubicación Bogotá
- `Book` - Para cada libro
- `Service` - Terapias ofrecidas
- `FAQPage` - Preguntas frecuentes
- `BreadcrumbList` - Migas de pan
- `AboutPage` - Página sobre mí

### AI Crawlers Permitidos (robots.txt)
- GPTBot, ChatGPT-User
- Google-Extended
- PerplexityBot, ClaudeBot
- Applebot-Extended, Amazonbot

### Meta Tags Especiales
```html
<meta name="citation_title" ... />
<meta name="citation_author" content="Adriana Cristina Rueda Sañudo" />
<meta name="citation_language" content="es" />
<meta name="ai-purpose" content="informational" />
```

---

## 📞 Puntos de Contacto

### Enlaces Directos
- **WhatsApp**: `https://wa.me/573132979675`
- **Email**: `mailto:adriana@adricrisrueda.com`
- **Instagram**: https://www.instagram.com/adricrisrueda/
- **Facebook**: https://www.facebook.com/adricrisespiritual/
- **YouTube**: https://www.youtube.com/@adricrisespiritual
- **LinkedIn**: https://co.linkedin.com/in/adriana-cristina-rueda

### Botones CTA Principales
1. "AGENDAR CONSULTA" → WhatsApp
2. "PRE-ORDENAR LIBRO" → /libro
3. "COMPRAR EN AMAZON" → Amazon (Lazos Escritos)

---

## 🚀 Deployment

### Comandos Disponibles
```bash
npm run dev          # localhost:4321
npm run build        # Genera /dist
npm run preview      # Previsualiza build
npm run deploy:static # Deploy a repo estático
```

### Proceso de Deploy
El script `scripts/deploy-static.js`:
1. Clona `adricrisrueda-static.git`
2. Copia `/dist` al repo temporal
3. Commitea cambios
4. Hace push al repo estático

---

## 📝 Convenciones de Código

### Astro Components
- Usar `interface Props` para tipado
- SEO via `SEOHead` y `SchemaOrg` components
- Imágenes: `loading="lazy"` por defecto, `eager` para hero

### Tailwind
- Mobile-first approach
- Dark mode: `dark:` prefix
- Colores: usar tokens del tema (primary, secondary, accent)

### Imágenes
```astro
<img
  src="/images/nombre.png"
  alt="Descripción SEO-friendly — ubicación"
  loading="lazy|eager"
  fetchpriority="high" (solo hero)
  decoding="async|sync"
/>
```

---

## ⚠️ Notas Importantes

1. **Dark Mode**: Implementado con `darkMode: "class"` en Tailwind. El toggle usa JavaScript vanilla para alternar clase `dark` en `<html>`.

2. **Fecha de Lanzamiento**: El libro "Una Voz al paso del Eclipse" se lanza el **11 de abril de 2026** en la Feria del Libro de Bogotá.

3. **Google Analytics**: ID `G-J08BEBZW01` está activo en todas las páginas.

4. **WhatsApp**: Es el canal de conversión principal. Botón flotante siempre visible.

5. **Sitemap**: Generado automáticamente por `@astrojs/sitemap`.

---

## 🔄 Historial de Cambios Recientes

- **2026-03-15**: Documentación inicial creada

---

> Para cualquier duda sobre el proyecto, referirse a:
> - README.md (información general)
> - Este archivo (contexto técnico detallado)
> - Código fuente en `/src`
