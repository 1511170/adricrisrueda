/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: [
    './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}',
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0F5257", 
        secondary: "#E3B64C", 
        accent: "#4F8F8B", 
        "background-light": "#EDEBE8", 
        "background-dark": "#0D1B1E",
        "surface-light": "#F7F5F2",
        "surface-dark": "#16262B",
      },
      fontFamily: {
        display: ["'Tenor Sans'", "sans-serif"],
        body: ["'Montserrat'", "sans-serif"],
      },
      borderRadius: {
        DEFAULT: "0.5rem",
        "xl": "1rem",
        "2xl": "1.5rem",
        "3xl": "2rem",
        "blob": "40% 60% 70% 30% / 40% 50% 60% 50%"
      },
      animation: {
        'blob': 'blob 10s infinite',
        'float': 'float 6s ease-in-out infinite',
        'glow': 'glow 3s ease-in-out infinite alternate',
      },
      keyframes: {
        blob: {
          '0%': { borderRadius: '60% 40% 30% 70% / 60% 30% 70% 40%' },
          '50%': { borderRadius: '30% 60% 70% 40% / 50% 60% 30% 60%' },
          '100%': { borderRadius: '60% 40% 30% 70% / 60% 30% 70% 40%' }
        },
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        glow: {
          'from': { boxShadow: '0 0 20px -10px rgba(227, 182, 76, 0.3)' },
          'to': { boxShadow: '0 0 40px 10px rgba(227, 182, 76, 0.4)' }
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
