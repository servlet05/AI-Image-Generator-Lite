# 🎨 AI Image Generator Lite

Generador de imágenes IA **ultra liviano** para PCs de bajos recursos.  
Funciona en CPU sin GPU, ideal para equipos viejos o sin tarjeta gráfica.



## ✨ Características

- ✅ **Funciona en CPU** - Sin GPU requerida
- ✅ **Solo 30MB** - Modelo TinySD optimizado
- ✅ **RAM mínima** - ~500MB de uso
- ✅ **Sin dependencias pesadas** - OpenVINO + Diffusers
- ✅ **Multi-plataforma** - Windows, Linux, Mac
- ✅ **API simple** - 3 líneas de código

# 🎨 AI Image Generator Lite

Generador de imágenes IA **ultra liviano** para PCs de bajos recursos.
Funciona en CPU sin GPU, ideal para equipos viejos o sin tarjeta gráfica.

---

## 🚀 Instalación Rápida

```bash
# 1. Clonar
git clone https://github.com/servlet05/AI-Image-Generator-Lite.git
cd AI-Image-Generator-Lite

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar demo
python examples/demo.py

📝 Uso Básico
python

from src.generator import LiteImageGenerator

# Inicializar (carga automática)
gen = LiteImageGenerator()

# Generar imagen
gen.generate("paisaje cyberpunk", "output.jpg")

⚙️ Personalización
python

# Modelos disponibles
gen = LiteImageGenerator(model="tiny")   # 30MB, más rápido
gen = LiteImageGenerator(model="small")  # 80MB, mejor calidad

# Parámetros avanzados
gen.generate(
    prompt="gato espacial",
    output="cat.jpg",
    steps=20,        # Iteraciones (más = mejor calidad)
    guidance=7.5     # Creatividad (1-15)
)

💻 Requisitos Mínimos
Componente	Mínimo	Recomendado
RAM	1GB	4GB
CPU	2 núcleos	4 núcleos
Disco	100MB	500MB
SO	Windows 7+	Linux/Windows 10+
⚡ Rendimiento (CPU 4 núcleos)
Resolución	Tiempo aproximado
256×256	~30 segundos
384×384	~60 segundos
512×512	~120 segundos
📦 Dependencias
txt

optimum-intel[openvino]>=1.14.0
diffusers>=0.24.0
transformers>=4.35.0
pillow>=10.0.0
torch>=2.0.0
psutil>=5.9.0

📄 Licencia

MIT © servlet05
⭐ ¿Te sirvió?

¡Dale estrella al repo! ⭐
        


