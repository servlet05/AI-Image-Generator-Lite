"""Utilidades para el generador de imágenes"""

import os
import json
from pathlib import Path
from datetime import datetime

def verificar_requisitos():
    """Verifica que se cumplan los requisitos mínimos"""
    import psutil
    
    ram = psutil.virtual_memory()
    cpu = psutil.cpu_count()
    
    print(f"💾 RAM: {ram.total / 1024**3:.1f}GB")
    print(f"🧠 CPU: {cpu} núcleos")
    
    if ram.total < 1024**3:  # 1GB
        print("⚠️  RAM baja: mínimo 1GB recomendado")
    
    if cpu < 2:
        print("⚠️  CPU baja: mínimo 2 núcleos recomendado")
    
    return True

def guardar_metadata(prompt, archivo, params):
    """Guarda metadatos de la generación"""
    metadata = {
        "prompt": prompt,
        "archivo": str(archivo),
        "fecha": datetime.now().isoformat(),
        "parametros": params
    }
    
    meta_path = Path(archivo).with_suffix('.json')
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    return meta_path
