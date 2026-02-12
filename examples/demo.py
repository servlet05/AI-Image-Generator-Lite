#!/usr/bin/env python3
"""
Ejemplo básico de uso del generador de imágenes
"""

import sys
from pathlib import Path

# Añadir al path
sys.path.append(str(Path(__file__).parent.parent))

from src.generator import LiteImageGenerator
from src.utils import verificar_requisitos

def main():
    print("="*50)
    print("🎨 AI Image Generator Lite - Demo")
    print("="*50)
    
    # Verificar sistema
    verificar_requisitos()
    
    # Inicializar generador
    print("\n📦 Cargando modelo...")
    gen = LiteImageGenerator(model="tiny")  # 30MB
    
    # Generar imagen
    print("\n✨ Generando imagen...")
    prompt = "un gato astronauta en el espacio, estilo cartoon"
    
    gen.generate(
        prompt=prompt,
        output="outputs/gato_espacial.jpg",
        steps=15,      # Menos pasos = más rápido
        width=256,     # Baja resolución = rápido
        height=256
    )
    
    print("\n✅ ¡Demo completada!")

if __name__ == "__main__":
    main()
