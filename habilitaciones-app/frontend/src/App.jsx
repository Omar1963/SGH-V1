import { useState } from 'react'

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center justify-center p-4">
      <header className="text-center mb-8">
        <h1 className="text-5xl font-bold text-blue-500 mb-4 tracking-tight">
          SGH-V1
        </h1>
        <p className="text-xl text-gray-400">
          Sistema Integral de Habilitaciones
        </p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl w-full">
        <div className="bg-gray-800 p-6 rounded-2xl border border-gray-700 hover:border-blue-500 transition-all shadow-xl">
          <h2 className="text-2xl font-semibold mb-3 flex items-center gap-2">
            <span className="p-2 bg-blue-500/20 rounded-lg text-blue-400">🚀</span>
            Frontend
          </h2>
          <p className="text-gray-400 mb-4">
            React + Vite + Tailwind CSS + Bootstrap 5 inicializados correctamente.
          </p>
          <button className="btn btn-primary w-full py-2 rounded-xl font-bold shadow-lg shadow-blue-500/30">
            Explorar Componentes
          </button>
        </div>

        <div className="bg-gray-800 p-6 rounded-2xl border border-gray-700 hover:border-green-500 transition-all shadow-xl">
          <h2 className="text-2xl font-semibold mb-3 flex items-center gap-2">
            <span className="p-2 bg-green-500/20 rounded-lg text-green-400">⚙️</span>
            Backend
          </h2>
          <p className="text-gray-400 mb-4">
            FastAPI skeletal listo con soporte para PostgreSQL y Docker.
          </p>
          <button className="btn btn-success w-full py-2 rounded-xl font-bold shadow-lg shadow-green-500/30">
            Ver API Docs
          </button>
        </div>
      </div>

      <footer className="mt-12 text-gray-500 text-sm">
        SGH-V1 v1.0.0 &copy; 2026 - Estructura Profesional Aprobada
      </footer>
    </div>
  )
}

export default App
