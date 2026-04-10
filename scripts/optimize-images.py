from PIL import Image
import os

# Configuración
source_dir = r'c:\Users\camilo\Documents\ADRIANA CRISTINA RUEDA\CAMBIOS 2\FOTOS'
dest_dir = 'public/images'

# Definir las imágenes y sus configuraciones
images_config = [
    {
        'src': 'AdriCris Rueda bio1 .jpg.jpeg',
        'dest': 'adriana-bio-blusa-blanca.webp',
        'width': 800,
        'quality': 85
    },
    {
        'src': 'Adri4.jpg.jpeg',
        'dest': 'adriana-notas-autora.webp',
        'width': 800,
        'quality': 85
    },
    {
        'src': 'AdriCris Rueda _ 4.jpg.jpeg',
        'dest': 'adriana-servicios-nueva.webp',
        'width': 800,
        'quality': 85
    },
    {
        'src': 'Utrilla_FILBo2026_publicidad_2_Adriana Cristina Rueda.jpg.jpeg',
        'dest': 'filbo-2026-oficial.webp',
        'width': 1200,
        'quality': 85
    },
    {
        'src': '20260330_195145_0000.png',
        'dest': 'adriana-alternativa.webp',
        'width': 800,
        'quality': 85
    }
]

for config in images_config:
    try:
        src_path = os.path.join(source_dir, config['src'])
        dest_path = os.path.join(dest_dir, config['dest'])
        
        if os.path.exists(src_path):
            img = Image.open(src_path)
            
            # Convertir a RGB si es necesario
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Calcular nueva altura manteniendo proporción
            ratio = config['width'] / img.width
            height = int(img.height * ratio)
            
            # Redimensionar
            img_resized = img.resize((config['width'], height), Image.LANCZOS)
            
            # Guardar como WebP
            img_resized.save(dest_path, 'WEBP', quality=config['quality'], method=6)
            
            print(f'OK: {config["src"]} -> {config["dest"]} ({img_resized.width}x{img_resized.height})')
        else:
            print(f'NOT FOUND: {config["src"]}')
    except Exception as e:
        print(f'ERROR: {config["src"]}: {e}')

print('\nOptimizacion completada!')
