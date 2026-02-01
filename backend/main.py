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
    corregir_ortografia: Optional[bool] = True  # Nueva opción
    velocidad_deletreo: Optional[float] = 1.2  # Duración en segundos por letra

class CorreccionItem(BaseModel):
    original: str
    corregida: str
    tipo: str
    confianza: int
    distancia: Optional[int] = None

class AnimacionItem(BaseModel):
    nombre: str
    categoria: str
    archivo: str
    es_deletreo: bool = False
    duracion: Optional[float] = None

class TranslateResponse(BaseModel):
    texto_original: str
    texto_corregido: str
    correcciones: List[CorreccionItem]
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

@app.post("/api/corregir")
async def corregir_texto(request: dict):
    """
    Corrige ortografía del texto sin traducir
    - Detecta y corrige errores de escritura
    - Normaliza verbos y palabras
    - Retorna texto corregido con lista de correcciones
    """
    try:
        texto = request.get("texto", "")
        texto_corregido, correcciones = optimizer.corregir_texto(texto)
        
        return {
            "texto_original": texto,
            "texto_corregido": texto_corregido,
            "correcciones": correcciones,
            "total_correcciones": len(correcciones)
        }
    
    except Exception as e:
        print(f"❌ Error en corregir: {e}")
        return {
            "texto_original": texto,
            "texto_corregido": texto,
            "correcciones": [],
            "total_correcciones": 0,
            "error": str(e)
        }

@app.post("/api/translate")
async def translate_text(request: TranslateRequest):
    """
    Traduce texto español a secuencia de animaciones LSV
    - Corrige errores ortográficos automáticamente
    - Deletrea palabras desconocidas usando alfabeto
    - Retorna secuencia de animaciones
    """
    try:
        # Obtener secuencia de animaciones directamente
        resultado = optimizer.translate_to_animations(
            request.texto,
            deletrear_desconocidas=request.deletrear_desconocidas,
            velocidad_deletreo=request.velocidad_deletreo,
            corregir_ortografia=request.corregir_ortografia
        )
        
        # Retornar respuesta en formato JSON simple
        return {
            "texto_original": resultado['texto_original'],
            "texto_corregido": resultado['texto_corregido'],
            "correcciones": resultado['correcciones'],
            "animaciones": resultado['animaciones'],
            "total_animaciones": resultado['total_animaciones'],
            "palabras_deletreadas": resultado['palabras_deletreadas']
        }
    
    except Exception as e:
        print(f"❌ Error en translate: {e}")
        import traceback
        traceback.print_exc()
        return {
            "texto_original": request.texto,
            "texto_corregido": request.texto,
            "correcciones": [],
            "animaciones": [],
            "total_animaciones": 0,
            "palabras_deletreadas": [],
            "error": str(e)
        }

if __name__ == "__main__":
    print("🚀 Iniciando LSV Translator API...")
    print("📡 Servidor corriendo en http://localhost:3000")
    print("📚 Documentación en http://localhost:3000/docs")
    uvicorn.run(
        "main:app",  # Import string en lugar del objeto
        host="0.0.0.0", 
        port=3000,
        reload=True  # Auto-reload en desarrollo
    )
