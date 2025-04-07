import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { createHtmlPlugin } from 'vite-plugin-html'
import vueDevTools from 'vite-plugin-vue-devtools'
import path from 'path'

export default defineConfig({
  base: '/integrationmonitor/', // ✅ GitHub Pages için gerekli base ayarı
  plugins: [
    vue(),
    vueDevTools(), // Vue DevTools eklentisini aktif et
    createHtmlPlugin({}) // HTML yapılandırması
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // @ alias'ını src dizinine yönlendir
    },
  },
  server: {
    port: 5173, // Özel bir port belirleyebilirsin (isteğe bağlı)
    open: true, // Sunucu başlatıldığında otomatik olarak tarayıcıda aç
  }
})
