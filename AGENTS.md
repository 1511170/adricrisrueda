# AGENTS.md - Guía para Agentes de Código

> **Proyecto**: AdriCris Rueda | Vida Consciente  
> **Framework**: Astro + Tailwind CSS  
> **Tipo**: Sitio estático de terapeuta holística y autora

---

## 🚀 Inicio Rápido

```bash
# Instalar dependencias
npm install

# Desarrollo
npm run dev          # http://localhost:4321

# Build
npm run build        # Output en ./dist

# Deploy
npm run deploy:static # Deploy automático
```

---

## 📁 Estructura del Proyecto

```
src/
├── components/
│   └── seo/
│       ├── SEOHead.astro      # Meta tags, Open Graph, AEO
│       └── SchemaOrg.astro    # JSON-LD structured data
├── layouts/
│   └── Layout.astro           # Layout principal (nav, footer)
├── pages/
│   ├── index.astro            # Home (hero libro + bio)
│   ├── sobre-mi.astro         # Biografía completa
│   ├── libro.astro            # "Una Voz al paso del Eclipse"
│   ├── libros.astro           # Biblioteca/catálogo
│   └── servicios.astro        # Terapias y talleres
└── styles/
    └── global.css             # Tailwind + custom styles

public/
├── images/                    # Fotos, portadas, logos
├── favicon.svg
└── robots.txt
```

---

## 🎨 Sistema de Diseño

### Colores (Tailwind Config)
```javascript
primary:    "#0F5257"   // Verde oscuro
secondary:  "#E3B64C"   // Dorado
accent:     "#4F8F8B"   // Verde menta
```

### Modo Oscuro
- Clase manual: `dark` en `<html>`
- Toggle en navbar y mobile menu
- Persistencia en localStorage (implementado en Layout.astro)

### Tipografía
- **Títulos**: `font-display` (Tenor Sans)
- **Cuerpo**: `font-body` (Montserrat)

---

## 🧩 Componentes Clave

### Layout Principal
```astro
---
import Layout from '../layouts/Layout.astro';
---
<Layout
  title="Título de página"
  description="Meta descripción"
  image="/images/imagen.png"
  keywords={['palabra1', 'palabra2']}
>
  <!-- Contenido -->
</Layout>
```

### SEO & Schema.org
```astro
import SchemaOrg from '../components/seo/SchemaOrg.astro';

<!-- En Layout con slot="head" -->
<SchemaOrg slot="head" type={['Book']} data={{...}} />
<SchemaOrg slot="head" type={['BreadcrumbList']} breadcrumbs={[...]} />
```

---

## ⚠️ Reglas Importantes

### 1. SEO es Crítico
- **SIEMPRE** incluir SEOHead y SchemaOrg en páginas nuevas
- Meta descripción entre 150-160 caracteres
- Alt text descriptivo en imágenes (incluir ubicación: Bogotá, Colombia)

### 2. Colores
- Usar tokens del tema: `primary`, `secondary`, `accent`
- NO hardcodear hex codes en componentes
- Dark mode: usar `dark:` prefix

### 3. Imágenes
```astro
<!-- Hero -->
<img loading="eager" fetchpriority="high" decoding="sync" />

<!-- Resto -->
<img loading="lazy" decoding="async" />
```

### 4. WhatsApp
- Botón flotante siempre presente (Layout.astro)
- Links usar formato: `https://wa.me/573132979675?text=...`

### 5. Fecha de Lanzamiento
- Libro "Una Voz al paso del Eclipse" → **11 abril 2026**
- NO cambiar esta fecha sin confirmación

---

## 📝 Convenciones de Código

### Astro
- Props tipadas con interface
- Slots para contenido head
- Componentes en PascalCase

### CSS/Tailwind
- Mobile-first
- Clases organizadas: layout → spacing → colors → effects
- Custom classes en `global.css` con `@layer components`

### URLs
- Internas: relativa `/ruta`
- Externas: absoluta con `target="_blank" rel="noopener noreferrer"`

---

## 🔍 Checklist antes de Commit

- [ ] Build exitoso (`npm run build`)
- [ ] No errores de TypeScript
- [ ] Dark mode funciona
- [ ] Links de WhatsApp funcionan
- [ ] Imágenes tienen alt text
- [ ] SEOHead incluido
- [ ] Schema.org válido (test en Google Rich Results)

---

## 🐛 Troubleshooting

### Build falla
```bash
# Limpiar caché
rm -rf dist node_modules .astro
npm install
npm run build
```

### Tailwind no aplica cambios
- Verificar `content` en `tailwind.config.mjs`
- Reiniciar servidor dev

### Imágenes no cargan
- Verificar ruta: `/images/nombre.png`
- Confirmar archivo en `public/images/`

---

## 📞 Contactos del Proyecto

- **Cliente**: Adriana Cristina Rueda Sañudo
- **Email**: adriana@adricrisrueda.com
- **WhatsApp**: +57 313 297 9675

---

## 📚 Recursos

- [README.md](./README.md) - Documentación general
- [KIMI.md](./KIMI.md) - Contexto técnico detallado
- [memory.md](./memory.md) - Memoria del proyecto

---

> **Nota**: Este es un proyecto de marca personal. Mantener consistencia visual y tono espiritual/cálido en todas las modificaciones.
