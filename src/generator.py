
---

## **2. `src/generator.py`**
```python
"""
Generador de imágenes IA ultra liviano.
Optimizado para CPU y bajos recursos.
"""

import os
import time
from pathlib import Path
from typing import Optional, Union
import numpy as np
from PIL import Image

class LiteImageGenerator:
    """Generador de imágenes optimizado para recursos bajos"""
    
    def __init__(self, model: str = "tiny", device: str = "cpu"):
        """
        Args:
            model: "tiny" (30MB) o "small" (80MB)
            device: "cpu" siempre (GPU deshabilitada intencionalmente)
        """
        self.model_name = model
        self.device = device
        self.pipeline = None
        self._cargar_modelo()
    
    def _cargar_modelo(self):
        """Carga el modelo optimizado OpenVINO"""
        try:
            from optimum.intel.openvino import OVStableDiffusionPipeline
            
            modelos = {
                "tiny": "OpenVINO/TinySD",
                "small": "OpenVINO/Dreamshaper-8-LCM"
            }
            
            print(f"🔄 Cargando modelo {self.model_name}...")
            start = time.time()
            
            self.pipeline = OVStableDiffusionPipeline.from_pretrained(
                modelos[self.model_name],
                device="CPU"
            )
            
            print(f"✅ Modelo cargado en {time.time()-start:.1f}s")
            
        except ImportError:
            print("❌ Error: Instala optimum-intel")
            print("pip install optimum-intel[openvino]")
            raise
    
    def generate(
        self,
        prompt: str,
        output: Union[str, Path],
        negative_prompt: str = "borroso, baja calidad, distorsionado",
        steps: int = 20,
        guidance: float = 7.5,
        width: int = 384,
        height: int = 384
    ) -> str:
        """
        Genera una imagen desde texto
        
        Args:
            prompt: Descripción de la imagen
            output: Ruta de salida
            negative_prompt: Qué evitar
            steps: Pasos de inferencia (más = mejor calidad)
            guidance: Creatividad (1-15)
            width/height: Resolución (múltiplos de 64)
            
        Returns:
            Ruta del archivo generado
        """
        if not self.pipeline:
            raise RuntimeError("Modelo no cargado")
        
        print(f"🎨 Generando: '{prompt}'")
        start = time.time()
        
        # Generar imagen
        image = self.pipeline(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=steps,
            guidance_scale=guidance,
            width=width,
            height=height
        ).images[0]
        
        # Guardar
        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path)
        
        print(f"✅ Guardado en {output_path}")
        print(f"⏱️  Tiempo: {time.time()-start:.1f}s")
        
        return str(output_path)
    
    def generate_batch(
        self,
        prompts: list,
        output_dir: Union[str, Path] = "outputs"
    ) -> list:
        """Genera múltiples imágenes"""
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
        
        resultados = []
        for i, prompt in enumerate(prompts):
            out = output_dir / f"img_{i}_{int(time.time())}.jpg"
            ruta = self.generate(prompt, out)
            resultados.append(ruta)
        
        return resultados
