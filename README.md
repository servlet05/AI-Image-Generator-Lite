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

### 🚀 Instalación Rápida

```bash
# 1. Clonar
git clone https://github.com/servlet05/AI-Image-Generator-Lite.git
cd AI-Image-Generator-Lite

# 2. Instalar
pip install -r requirements.txt

# 3. ¡Generar!
python examples/demo.py


#### 🚀 Uso Básico
```bash
from src.generator import LiteImageGenerator

# Inicializar (carga automática)
gen = LiteImageGenerator()

# Generar imagen
gen.generate("paisaje cyberpunk", "output.jpg")



##### 🚀 Personalizacion
# Modelos disponibles
```bash
gen = LiteImageGenerator(model="tiny")  # 30MB, rápido
gen = LiteImageGenerator(model="small") # 80MB, mejor calidad

# Parámetros
gen.generate(
    prompt="gato espacial",
    output="cat.jpg",
    steps=20,        # Iteraciones (más = mejor calidad)
    guidance=7.5     # Creatividad
)



        


