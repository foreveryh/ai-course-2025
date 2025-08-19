import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    chunkSizeWarningLimit: 3000,
    rollupOptions: {
      output: {
        manualChunks: {
          'slidev-theme': ['@slidev/theme-default', '@slidev/theme-seriph'],
          'vue-vendor': ['vue']
        }
      }
    }
  }
})
