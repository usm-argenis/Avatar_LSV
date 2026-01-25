from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
from api_optimizer import LSVOptimizer

app = FastAPI(
    title="LSV Translator API",
    description="API con IA para traducción a Lengua de Señas Venezolana",
    version="2.0.0"
)

# Configurar CORS para permitir acceso desde HTML local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios exactos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar optimizador con IA
optimizer = LSVOptimizer()

# Modelos de datos
class TranslateRequest(BaseModel):
    texto: str
    avatar: Optional[str] = "Nancy"
    deletrear_desconocidas: Optional[bool] = True
    velocidad_deletreo: Optional[float] = 1.2  # Duración en segundos por letra

class AnimacionItem(BaseModel):
    nombre: str
    categoria: str
    archivo: str
    es_deletreo: bool = False
    duracion: Optional[float] = None

class TranslateResponse(BaseModel):
    texto_original: str
    texto_corregido: str
    animaciones: List[AnimacionItem]
    total_animaciones: int
    palabras_deletreadas: List[str]

@app.get("/")
async def root():
    return {
        "message": "LSV Translator API funcionando! 🚀",
        "version": "2.0.0",
        "endpoints": {
            "translate": "/api/translate",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "optimizer": "ready"}

@app.post("/api/translate")
async def translate_text(request: TranslateRequest):
    """
    Traduce texto español a secuencia de animaciones LSV
    - Deletrea palabras desconocidas usando alfabeto
    - Retorna secuencia de animaciones
    """
    try:
        # Obtener secuencia de animaciones directamente
        resultado = optimizer.translate_to_animations(
            request.texto,
            deletrear_desconocidas=request.deletrear_desconocidas,
            velocidad_deletreo=request.velocidad_deletreo
        )
        
        # Retornar respuesta en formato JSON simple
        return {
            "texto_original": request.texto,
            "texto_corregido": request.texto,
            "animaciones": resultado['animaciones'],
            "total_animaciones": resultado['total_animaciones'],
            "palabras_deletreadas": resultado['palabras_deletreadas']
        }
    
    except Exception as e:
        print(f"❌ Error en translate: {e}")
        return {
            "texto_original": request.texto,
            "texto_corregido": request.texto,
            "animaciones": [],
            "total_animaciones": 0,
            "palabras_deletreadas": [],
            "error": str(e)
        }

if __name__ == "__main__":
    print("🚀 Iniciando LSV Translator API...")
    print("📡 Servidor corriendo en http://localhost:8000")
    print("📚 Documentación en http://localhost:8000/docs")
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True  # Auto-reload en desarrollo
    )
