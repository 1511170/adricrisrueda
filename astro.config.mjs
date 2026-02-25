import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  site: 'https://adricrisrueda.com',
  
  integrations: [
    tailwind({
      configFile: './tailwind.config.mjs',
      applyBaseStyles: false
    })
  ],
  
  build: {
    format: 'directory',
    compressHTML: true
  },
  
  vite: {
    resolve: {
      alias: {
        '@components': '/src/components',
        '@layouts': '/src/layouts',
        '@styles': '/src/styles',
        '@config': '/config'
      }
    }
  }
});
