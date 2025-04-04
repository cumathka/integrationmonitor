import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path' // Path modülünü içe aktar

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'), // @ işaretini src dizinine yönlendir
    },
  },
})