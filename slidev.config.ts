import { defineConfig } from '@slidev/cli'

export default defineConfig({
  // Ensure public assets are included in build
  publicDir: 'public',
  
  // Disable PDF export for faster builds
  export: {
    format: 'png',
    timeout: 30000,
    withClicks: false,
  },
  
  // Optimize for production builds
  build: {
    outDir: 'dist',
    base: './',
  }
})
