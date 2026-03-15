from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon(size, output_path):
    # Crear imagen con fondo transparente
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Radio de esquinas redondeadas (proporcional al tamaño)
    radius = int(size * 0.2)
    
    # Colores
    bg_color_start = (15, 82, 87)    # #0F5257
    bg_color_end = (13, 27, 30)       # #0D1B1E
    gold_color = (227, 182, 76)       # #E3B64C
    
    # Dibujar fondo con gradiente simulado
    for y in range(size):
        ratio = y / size
        r = int(bg_color_start[0] * (1 - ratio) + bg_color_end[0] * ratio)
        g = int(bg_color_start[1] * (1 - ratio) + bg_color_end[1] * ratio)
        b = int(bg_color_start[2] * (1 - ratio) + bg_color_end[2] * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    
    # Dibujar borde dorado
    border_width = max(1, int(size * 0.02))
    draw.rounded_rectangle(
        [(border_width//2, border_width//2), (size - border_width//2, size - border_width//2)],
        radius=radius,
        outline=gold_color,
        width=border_width
    )
    
    # Dibujar la letra "A"
    font_size = int(size * 0.5)
    font = None
    
    # Intentar diferentes fuentes del sistema
    font_paths = [
        "C:\\Windows\\Fonts\\georgia.ttf",
        "C:\\Windows\\Fonts\\times.ttf",
        "C:\\Windows\\Fonts\\cambria.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
        "/System/Library/Fonts/Georgia.ttf",
    ]
    
    for font_path in font_paths:
        try:
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, font_size)
                break
        except:
            continue
    
    if font is None:
        font = ImageFont.load_default()
    
    # Calcular posición centrada del texto
    text = "A"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - int(size * 0.05)  # Ajuste visual
    
    # Dibujar la "A" en dorado
    draw.text((x, y), text, fill=gold_color, font=font)
    
    # Guardar
    img.save(output_path, 'PNG')
    print(f"Creado: {output_path} ({size}x{size})")

if __name__ == "__main__":
    # Crear los diferentes tamaños
    create_favicon(16, 'public/favicon-16x16.png')
    create_favicon(32, 'public/favicon-32x32.png')
    create_favicon(180, 'public/apple-touch-icon.png')
    create_favicon(144, 'public/mstile-144x144.png')
    
    print("¡Favicons creados exitosamente!")
