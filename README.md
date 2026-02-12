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

# 🎨 AI Image Generator Lite

Generador de imágenes IA ultra liviano para PCs de bajos recursos.

## 🚀 Instalación Rápida

```bash
git clone https://github.com/servlet05/AI-Image-Generator-Lite.git
cd AI-Image-Generator-Lite
pip install -r requirements.txt
python examples/demo.py
```

## 📝 Uso Básico

```python
from src.generator import LiteImageGenerator
gen = LiteImageGenerator()
gen.generate("paisaje cyberpunk", "output.jpg")
```

## ⚙️ Personalización

```python
gen = LiteImageGenerator(model="tiny")
gen.generate("gato espacial", "cat.jpg", steps=20, guidance=7.5)
```
