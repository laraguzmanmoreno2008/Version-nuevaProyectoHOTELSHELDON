import flet as ft

def sobre_nosotros(page):
    # Colores del tema ultra moderno
    COLOR_PRIMARIO = "#625956"  # Slate 900
    COLOR_SECUNDARIO = "#475569"  # Slate 600
    COLOR_ACENTO = "#d89c6c"  # Blue 500
    COLOR_FONDO = "#ede8e4"  # Slate 50
    COLOR_TEXTO = "#152540"  # Slate 950
    COLOR_CARD = "#edebeb"

    return ft.Container(
        content=ft.Column(
            [
                # Encabezado ultra moderno
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Text(
                                "SOBRE NOSOTROS",
                                size=12,
                                weight="w600",
                                color=COLOR_ACENTO,
                            
                            ),
                            bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                            padding=ft.padding.symmetric(horizontal=16, vertical=6),
                            border_radius=50,
                        ),
                        ft.Text(
                            "Conoce nuestra historia",
                            size=40,
                            weight="w700",
                            color=COLOR_PRIMARIO,
                        ),
                        ft.Text(
                            "Más de una década de excelencia en hospitalidad",
                            size=16,
                            color=COLOR_SECUNDARIO,
                        ),
                    ], 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=12),
                    padding=ft.padding.only(bottom=48, top=24),
                ),
                
                # Contenido principal
                ft.Row(
                    [
                        # Columna izquierda - Texto
                        ft.Container(
                            content=ft.Column([
                                ft.Container(
                                    content=ft.Column([
                                        # Bienvenida
                                        ft.Row([
                                            ft.Container(
                                                content=ft.Icon(
                                                    ft.Icons.APARTMENT,
                                                    size=32,
                                                    color=COLOR_CARD
                                                ),
                                                bgcolor=COLOR_ACENTO,
                                                border_radius=12,
                                                padding=12,
                                            ),
                                            ft.Text(
                                                "Hotel Sheldon",
                                                size=28,
                                                weight="w700",
                                                color=COLOR_PRIMARIO,
                                            ),
                                        ], spacing=16),
                                        
                                        ft.Container(height=8),
                                        
                                        ft.Text(
                                            "Localizado en Unquillo, nuestro hotel ofrece 100 habitaciones "
                                            "diseñadas meticulosamente para todo tipo de viajeros. "
                                            "Cada espacio ha sido creado pensando en su comodidad y bienestar.",
                                            size=15,
                                            color=COLOR_TEXTO,
                                            text_align=ft.TextAlign.JUSTIFY,
                                        ),
                                        
                                        ft.Container(height=24),
                                        
                                        # Servicios con iconos modernos
                                        ft.Text(
                                            "Servicios Destacados",
                                            size=20,
                                            weight="w700",
                                            color=COLOR_PRIMARIO,
                                        ),
                                        
                                        ft.Container(height=8),
                                        
                                        ft.Column([
                                            ft.Container(
                                                content=ft.Row([
                                                    ft.Container(
                                                        content=ft.Icon(ft.Icons.KING_BED, size=20, color=COLOR_ACENTO),
                                                        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                                                        border_radius=8,
                                                        padding=8,
                                                    ),
                                                    ft.Text("Suites de lujo con vistas panorámicas", size=15, color=COLOR_TEXTO),
                                                ], spacing=12),
                                                padding=12,
                                                bgcolor=ft.Colors.with_opacity(0.03, COLOR_TEXTO),
                                                border_radius=12,
                                            ),
                                            ft.Container(
                                                content=ft.Row([
                                                    ft.Container(
                                                        content=ft.Icon(ft.Icons.FAMILY_RESTROOM, size=20, color=COLOR_ACENTO),
                                                        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                                                        border_radius=8,
                                                        padding=8,
                                                    ),
                                                    ft.Text("Espacios familiares amplios y confortables", size=15, color=COLOR_TEXTO),
                                                ], spacing=12),
                                                padding=12,
                                                bgcolor=ft.Colors.with_opacity(0.03, COLOR_TEXTO),
                                                border_radius=12,
                                            ),
                                            ft.Container(
                                                content=ft.Row([
                                                    ft.Container(
                                                        content=ft.Icon(ft.Icons.SPA, size=20, color=COLOR_ACENTO),
                                                        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                                                        border_radius=8,
                                                        padding=8,
                                                    ),
                                                    ft.Text("Spa exclusivo y centro de bienestar", size=15, color=COLOR_TEXTO),
                                                ], spacing=12),
                                                padding=12,
                                                bgcolor=ft.Colors.with_opacity(0.03, COLOR_TEXTO),
                                                border_radius=12,
                                            ),
                                            ft.Container(
                                                content=ft.Row([
                                                    ft.Container(
                                                        content=ft.Icon(ft.Icons.SUPPORT_AGENT, size=20, color=COLOR_ACENTO),
                                                        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                                                        border_radius=8,
                                                        padding=8,
                                                    ),
                                                    ft.Text("Atención personalizada 24/7", size=15, color=COLOR_TEXTO),
                                                ], spacing=12),
                                                padding=12,
                                                bgcolor=ft.Colors.with_opacity(0.03, COLOR_TEXTO),
                                                border_radius=12,
                                            ),
                                        ], spacing=8),
                                        
                                        ft.Container(height=24),
                                        
                                        # Misión
                                        ft.Text(
                                            "Nuestra Misión",
                                            size=20,
                                            weight="w700",
                                            color=COLOR_PRIMARIO,
                                        ),
                                        
                                        ft.Container(height=8),
                                        
                                        ft.Text(
                                            "Brindar una experiencia única que combine la calidez de la atención "
                                            "personalizada con la excelencia en cada detalle. Nos esforzamos por "
                                            "crear momentos memorables que perduren en el tiempo.",
                                            size=15,
                                            color=COLOR_TEXTO,
                                            text_align=ft.TextAlign.JUSTIFY,
                                        ),
                                        
                                        ft.Container(height=24),
                                        
                                        # Visión
                                        ft.Text(
                                            "Visión a Futuro",
                                            size=20,
                                            weight="w700",
                                            color=COLOR_PRIMARIO,
                                        ),
                                        
                                        ft.Container(height=8),
                                        
                                        ft.Text(
                                            "Aspiramos a consolidarnos como un referente en hospitalidad, "
                                            "apostando por la sostenibilidad, la innovación constante y el desarrollo "
                                            "de nuevos servicios que enriquezcan cada estancia.",
                                            size=15,
                                            color=COLOR_TEXTO,
                                            text_align=ft.TextAlign.JUSTIFY,
                                        ),
                                        
                                        ft.Container(height=24),
                                        
                                        # Quote destacado
                                        ft.Container(
                                            content=ft.Column([
                                                ft.Icon(ft.Icons.FORMAT_QUOTE, size=32, color=COLOR_ACENTO),
                                                ft.Text(
                                                    "En Sheldon, cada visita se transforma en un recuerdo memorable.",
                                                    size=18,
                                                    weight="w600",
                                                    color=COLOR_PRIMARIO,
                                                    text_align=ft.TextAlign.CENTER,
                                                ),
                                            ], 
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=12),
                                            padding=32,
                                            bgcolor=ft.Colors.with_opacity(0.05, COLOR_ACENTO),
                                            border_radius=16,
                                            border=ft.border.all(2, ft.Colors.with_opacity(0.1, COLOR_ACENTO)),
                                        ),
                                        
                                    ], spacing=0, scroll=ft.ScrollMode.ALWAYS),
                                    padding=32,
                                ),
                            ], scroll=ft.ScrollMode.ALWAYS),
                            bgcolor=COLOR_CARD,
                            border_radius=16,
                            border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
                            width=560,
                            height=700,
                        ),
                        
                        # Columna derecha - Imagen
                        ft.Container(
                            content=ft.Column([
                                ft.Container(
                                    content=ft.Image(
                                        src="https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
                                        width=560,
                                        height=620,
                                        border_radius=16,
                                        fit=ft.ImageFit.COVER
                                    ),
                                    border_radius=16,
                                ),
                                ft.Container(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.LOCATION_ON, size=16, color=COLOR_ACENTO),
                                        ft.Text(
                                            "Unquillo, Córdoba",
                                            size=14,
                                            color=COLOR_SECUNDARIO,
                                            weight="w500",
                                        ),
                                    ], spacing=8),
                                    padding=ft.padding.only(top=12),
                                ),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=16,
                        )
                    ],
                    spacing=40,
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=48,
        bgcolor=COLOR_FONDO,
    )