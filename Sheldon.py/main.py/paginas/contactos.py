import flet as ft


def contactos(page):
    COLOR_PRIMARIO = "#625956"  
    COLOR_SECUNDARIO = "#475569" 
    COLOR_ACENTO = "#d89c6c"  
    COLOR_FONDO = "#ede8e4"  
    COLOR_TEXTO = "#152540" 
    COLOR_CARD = "#edebeb"

    contactos_info = [
        {
            "icon": ft.Icons.EMAIL_OUTLINED,
            "label": "Email",
            "valor": "info@hotelsheldon.com",
        },
        {
            "icon": ft.Icons.PHONE_OUTLINED,
            "label": "Teléfono",
            "valor": "+54 X XXX XXX-XXXX",
        },
        {
            "icon": ft.Icons.LOCATION_ON_OUTLINED,
            "label": "Dirección",
            "valor": "Alcides Casatti, Unquillo, Córdoba",
        },
        {
            "icon": ft.Icons.CAMERA_ALT_OUTLINED,
            "label": "Instagram",
            "valor": "@Hotel.sheldon.oficial",
        },
    ]

    def contacto_item(info: dict):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(
                        info["icon"],
                        size=20,
                        color=COLOR_ACENTO
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                    border_radius=12,
                    padding=12,
                ),
                ft.Column([
                    ft.Text(
                        info["label"],
                        size=12,
                        weight="w500",
                        color=COLOR_SECUNDARIO,
                    ),
                    ft.Text(
                        info["valor"],
                        size=15,
                        weight="w600",
                        color=COLOR_TEXTO,
                    ),
                ], spacing=16, alignment=ft.MainAxisAlignment.CENTER),
            ], spacing=16, alignment=ft.MainAxisAlignment.START),
            padding=20,
            bgcolor=COLOR_CARD,
            border_radius=16,
            border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
            width=400,
        )

    return ft.Container(
        expand=True,
        content=ft.Stack([
            
            ft.Container(
                bgcolor=ft.Colors.with_opacity(0.75, COLOR_PRIMARIO),
                expand=True,
            ),
            
            ft.Container(
                alignment=ft.alignment.center,
                content=ft.Container(
                    content=ft.Column([
                     
                        ft.Container(
                            content=ft.Icon(
                                ft.Icons.APARTMENT,
                                size=40,
                                color=COLOR_CARD
                            ),
                            bgcolor=COLOR_ACENTO,
                            border_radius=16,
                            padding=16,
                        ),
                        
                        ft.Container(height=16),
                        
                   
                        ft.Column([
                            ft.Container(
                                content=ft.Text(
                                    "CONTACTO",
                                    size=12,
                                    weight="w600",
                                    color=COLOR_ACENTO,

                                ),
                                bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                                padding=ft.padding.symmetric(horizontal=16, vertical=6),
                                border_radius=50,
                            ),
                            ft.Text(
                                "Hablemos",
                                size=29,
                                weight="w700",
                                color=COLOR_PRIMARIO,
                            ),
                            ft.Text(
                                "Estamos disponibles 24/7",
                                size=14,
                                color=COLOR_SECUNDARIO,
                            ),
                        ], 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=8),
                        
                        ft.Container(height=24),
                        
                        
                        ft.Column([
                            contacto_item(info) for info in contactos_info
                        ], 
                        spacing=12,
                        scroll=ft.ScrollMode.ALWAYS,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        
                        ft.Container(height=24),
                        
                       
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Icon(ft.Icons.ACCESS_TIME, size=16, color=COLOR_ACENTO),
                                    ft.Text(
                                        "Respuesta en menos de 24 horas",
                                        size=13,
                                        color=COLOR_SECUNDARIO,
                                        weight="w500"
                                    ),
                                ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                            ], 
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=8),
                            padding=20,
                            bgcolor=ft.Colors.with_opacity(0.05, COLOR_TEXTO),
                            border_radius=12,
                        ),
                        
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0),
                    padding=40,
                    bgcolor=COLOR_CARD,
                    border_radius=24,
                    border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
                    width=480,
                    shadow=ft.BoxShadow(
                        spread_radius=0,
                        blur_radius=32,
                        color=ft.Colors.with_opacity(0.2, COLOR_TEXTO),
                    ),
                )
            )
        ])

    )
