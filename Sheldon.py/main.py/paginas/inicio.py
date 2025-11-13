import flet as ft


def inicio(page, go_to):
    # Colores del tema ultra moderno
    COLOR_PRIMARIO = "#625956"  # Slate 900
    COLOR_ACENTO = "#d89c6c"  # Blue 500
    COLOR_CARD = "#edebeb"

    return ft.Container(
        expand=True,
        content=ft.Stack([
            # Imagen de fondo
            ft.Image(
                src="https://images.unsplash.com/photo-1566073771259-6a8506099945",
                width=page.width,
                height=page.height,
                fit=ft.ImageFit.COVER
            ),
            # Overlay oscuro dramático
            ft.Container(
                bgcolor=ft.Colors.with_opacity(0.65, COLOR_PRIMARIO),
                width=page.width,
                height=page.height
            ),
            # Contenido principal
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                content=ft.Column([
                    ft.Container(height=20),
                    
                    # Título principal ultra moderno
                    ft.Text(
                        "HOTEL",
                        size=28,
                        weight="w300",
                        color=ft.Colors.with_opacity(0.7, COLOR_CARD),
                        text_align=ft.TextAlign.CENTER,
                       
                    ),
                    ft.Text(
                        "SHELDON",
                        size=67,
                        weight="w700",
                        color=COLOR_CARD,
                        text_align=ft.TextAlign.CENTER,
            
                    ),
                    
                    ft.Container(height=10),
                    
                    # Subtítulo minimalista
                    ft.Container(
                        content=ft.Text(
                            "Experiencia • Confort • Elegancia",
                            size=16,
                            color=ft.Colors.with_opacity(0.9, COLOR_CARD),
                            text_align=ft.TextAlign.CENTER,
                            weight="w400",
                            
                        ),
                        padding=ft.padding.only(bottom=40),
                    ),
                    
                    # Botón CTA ultra moderno
                    ft.Container(
                        content=ft.ElevatedButton(
                            content=ft.Row([
                                ft.Text("Reservar Ahora", size=16, weight="w600"),
                                ft.Icon(ft.Icons.ARROW_FORWARD, size=20),
                            ], 
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=12),
                            bgcolor=COLOR_ACENTO,
                            color=COLOR_CARD,
                            height=56,
                            width=240,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=50),
                                elevation=8,
                            ),
                            on_click=lambda _: go_to("reservas")
                        ),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=32,
                            color=ft.Colors.with_opacity(0.5, COLOR_ACENTO),
                        ),
                    ),
                    
                    ft.Container(height=60),
                    
                    # Stats modernos
                    ft.Row([
                        ft.Column([
                            ft.Text("100+", size=32, weight="w700", color=COLOR_CARD),
                            ft.Text("Habitaciones", size=12, color=ft.Colors.with_opacity(0.7, COLOR_CARD)),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                        
                        ft.Container(width=1, height=50, bgcolor=ft.Colors.with_opacity(0.3, COLOR_CARD)),
                        
                        ft.Column([
                            ft.Text("5★", size=32, weight="w700", color=COLOR_CARD),
                            ft.Text("Calificación", size=12, color=ft.Colors.with_opacity(0.7, COLOR_CARD)),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                        
                        ft.Container(width=1, height=50, bgcolor=ft.Colors.with_opacity(0.3, COLOR_CARD)),
                        
                        ft.Column([
                            ft.Text("24/7", size=32, weight="w700", color=COLOR_CARD),
                            ft.Text("Atención", size=12, color=ft.Colors.with_opacity(0.7, COLOR_CARD)),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=4),
                    ], 
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40),
                    
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0),
            )
        ])
    )