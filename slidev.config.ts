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
  },
  
  // Vite build optimizations
  vite: {
    build: {
      // 增加chunk size限制，避免过多小文件
      chunkSizeWarningLimit: 1000,
      rollupOptions: {
        output: {
          // 手动chunk分割，提升构建效率
          manualChunks: {
            vue: ['vue'],
            slidev: ['@slidev/client'],
          }
        }
      }
    },
    optimizeDeps: {
      // 预构建依赖，加速开发和构建
      include: ['vue', '@slidev/client'],
    }
  }
})
