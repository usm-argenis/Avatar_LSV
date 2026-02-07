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
    glosa_lsv: str  # Nueva: glosa LSV en MAYÚSCULAS
    correcciones: List[CorreccionItem]
    animaciones: List[AnimacionItem]
    total_animaciones: int
    palabras_deletreadas: List[str]
    observaciones_linguisticas: List[str]  # Nueva: observaciones sobre la traducción
    alternativas: List[str]  # Nueva: alternativas válidas

@app.get("/")
async def root():
    return {
        "message": "LSV Translator API funcionando! 🚀",
        "version": "2.0.0",
        "endpoints": {
            "translate": "/api/translate",
            "optimizar": "/api/optimizar",
            "corregir": "/api/corregir",
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
    
    🎯 SISTEMA EXPERTO EN LSV basado en patrones lingüísticos reales:
    - Corrige errores ortográficos automáticamente
    - Aplica orden gramatical LSV: CONTEXTO → TIEMPO → LUGAR → SUJETO → ACCIÓN → NEGACIÓN
    - Reformula conceptos abstractos usando señas existentes
    - Deletrea palabras desconocidas usando alfabeto
    - Retorna glosa LSV, animaciones, observaciones lingüísticas y alternativas
    
    Ejemplos del sistema:
    - "Bienvenidos a la defensa" → BIENVENIR DEFENSA
    - "Nuestro objetivo es crear un sistema" → OBJETIVO NOSOTROS SISTEMA CREAR
    - "No existe" → EXISTIR NO
    - "Es muy importante" → IMPORTANTE MUCHO
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
            "glosa_lsv": resultado.get('glosa_lsv', ''),
            "correcciones": resultado['correcciones'],
            "animaciones": resultado['animaciones'],
            "total_animaciones": resultado['total_animaciones'],
            "palabras_deletreadas": resultado['palabras_deletreadas'],
            "observaciones_linguisticas": resultado.get('observaciones_linguisticas', []),
            "alternativas": resultado.get('alternativas', [])
        }
    
    except Exception as e:
        print(f"❌ Error en translate: {e}")
        import traceback
        traceback.print_exc()
        return {
            "texto_original": request.texto,
            "texto_corregido": request.texto,
            "glosa_lsv": "",
            "correcciones": [],
            "animaciones": [],
            "total_animaciones": 0,
            "palabras_deletreadas": [],
            "observaciones_linguisticas": [],
            "alternativas": [],
            "error": str(e)
        }

@app.post("/api/optimizar")
async def optimizar_texto(request: dict):
    """
    Optimiza texto para LSV (endpoint para app móvil)
    - Corrige ortografía
    - Traduce a LSV
    - Retorna información de cobertura y sugerencias
    """
    try:
        texto = request.get("texto", "")
        
        # Obtener traducción completa
        resultado = optimizer.translate_to_animations(
            texto,
            deletrear_desconocidas=True,
            velocidad_deletreo=1.2,
            corregir_ortografia=True
        )
        
        # Calcular palabras disponibles y faltantes
        palabras_input = texto.lower().split()
        palabras_lsv = [anim['nombre'] for anim in resultado['animaciones'] if not anim.get('es_deletreo', False)]
        palabras_disponibles = [p for p in palabras_lsv if p not in resultado['palabras_deletreadas']]
        
        # Calcular porcentaje de cobertura (palabras que NO se deletrearon)
        total_palabras = len([p for p in palabras_input if p not in optimizer.palabras_omitidas])
        palabras_sin_deletrear = len(palabras_disponibles)
        porcentaje_cobertura = (palabras_sin_deletrear / total_palabras * 100) if total_palabras > 0 else 100
        
        # Generar texto LSV (glosas en orden)
        texto_lsv = resultado.get('glosa_lsv', '')
        if not texto_lsv:
            texto_lsv = ' '.join([anim['nombre'].upper() for anim in resultado['animaciones']])
        
        return {
            "texto_original": resultado['texto_original'],
            "texto_corregido": resultado['texto_corregido'],
            "texto_lsv": texto_lsv,
            "palabras_lsv": palabras_lsv,
            "palabras_disponibles": palabras_disponibles,
            "palabras_faltantes": resultado['palabras_deletreadas'],
            "porcentaje_cobertura": porcentaje_cobertura,
            "sugerencias": {},
            "correcciones": resultado['correcciones'],
            "animaciones": resultado['animaciones'],
            "total_animaciones": resultado['total_animaciones'],
            "observaciones_linguisticas": resultado.get('observaciones_linguisticas', []),
            "alternativas": resultado.get('alternativas', [])
        }
    
    except Exception as e:
        print(f"❌ Error en optimizar: {e}")
        import traceback
        traceback.print_exc()
        return {
            "texto_original": texto,
            "texto_corregido": texto,
            "texto_lsv": "",
            "palabras_lsv": [],
            "palabras_disponibles": [],
            "palabras_faltantes": [],
            "porcentaje_cobertura": 0,
            "sugerencias": {},
            "error": str(e)
        }


if __name__ == "__main__":
    print("🚀 Iniciando LSV Translator API...")
    print("📡 Servidor corriendo en http://localhost:5000")
    print("📚 Documentación en http://localhost:5000/docs")
    uvicorn.run(
        "main:app",  # Import string en lugar del objeto
        host="0.0.0.0", 
        port=5000,
        reload=True  # Auto-reload en desarrollo
    )
