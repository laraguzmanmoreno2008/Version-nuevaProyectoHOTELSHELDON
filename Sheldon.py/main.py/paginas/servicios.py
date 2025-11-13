import flet as ft


def servicios(page):
    # Colores del tema ultra moderno
    COLOR_PRIMARIO = "#625956"  # Slate 900
    COLOR_SECUNDARIO = "#475569"  # Slate 600
    COLOR_ACENTO = "#d89c6c"  # Blue 500
    COLOR_FONDO = "#ede8e4"  # Slate 50
    COLOR_TEXTO = "#152540"  # Slate 950
    COLOR_CARD = "#edebeb"

    servicios_data = [
        {
            "img": "https://images.unsplash.com/photo-1667450799167-09e7dd903e59",
            "titulo": "Habitacion Familiar",
            "desc": "Habitaciones amplias y versátiles, con espacio para toda la familia. Incluye áreas de juego y comodidades especiales para niños.",
            "icon": ft.Icons.FAMILY_RESTROOM
        },
        {
            "img": "https://images.unsplash.com/photo-1532926381893-7542290edf1d",
            "titulo": "Habitacion Spa",
            "desc": "Área de spa con sauna, jacuzzi y tratamientos exclusivos. Disfrute de masajes terapéuticos y tratamientos de belleza en un ambiente de total relajación.",
            "icon": ft.Icons.SPA
        },
        {
            "img": "https://images.unsplash.com/photo-1616594039964-ae9021a400a0",
            "titulo": "Suite de Lujo",
            "desc": "Suite presidencial con cama king size y barra gourmet privada. Vistas panorámicas, sala de estar y baño de mármol italiano.",
            "icon": ft.Icons.DIAMOND
        },
        {
            "img": "https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf",
            "titulo": "Habitacion Estándar",
            "desc": "Cama confortable, baño privado y Wi-Fi gratuito. La opción perfecta para viajeros que buscan comodidad y funcionalidad.",
            "icon": ft.Icons.HOTEL
        }
    ]

    def servicio_card(data: dict):
        def open_dialog(e):
            dlg = ft.AlertDialog(
                title=ft.Text(
                    data["titulo"],
                    color=COLOR_PRIMARIO,
                    size=24,
                    weight="w700",
                ),
                content=ft.Container(
                    content=ft.Text(
                        data["desc"],
                        color=COLOR_TEXTO,
                        size=15,
                    ),
                    padding=16,
                ),
                bgcolor=COLOR_CARD,
                modal=True,
            )
            dlg.actions = [
                ft.TextButton(
                    "Cerrar",
                    on_click=lambda e: page.close(dlg),
                    style=ft.ButtonStyle(color=COLOR_ACENTO),
                )
            ]
            page.open(dlg)

        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Stack([
                        ft.Image(
                            src=data["img"],
                            width=300,
                            height=240,
                            border_radius=16,
                            fit=ft.ImageFit.COVER
                        ),
                        ft.Container(
                            content=ft.Container(
                                content=ft.Icon(
                                    data["icon"],
                                    size=28,
                                    color=COLOR_CARD
                                ),
                                bgcolor=COLOR_ACENTO,
                                border_radius=12,
                                padding=12,
                            ),
                            alignment=ft.alignment.top_right,
                            padding=16,
                        ),
                    ]),
                    on_click=open_dialog,
                    border_radius=16,
                    ink=True,
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            data["titulo"],
                            size=18,
                            weight="w700",
                            color=COLOR_TEXTO
                        ),
                        ft.TextButton(
                            content=ft.Row([
                                ft.Text("Ver detalles", size=13, weight="w500"),
                                ft.Icon(ft.Icons.ARROW_FORWARD, size=16),
                            ], spacing=4),
                            on_click=open_dialog,
                            style=ft.ButtonStyle(color=COLOR_ACENTO, padding=0),
                        ),
                    ], spacing=4),
                    padding=ft.padding.only(top=16, left=8, right=8),
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=0),
            padding=20,
            bgcolor=COLOR_CARD,
            border_radius=20,
            border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
            width=340,
        )

    extras = [
        {"icon": ft.Icons.WIFI, "label": "Wi-Fi Gratis"},
        {"icon": ft.Icons.FREE_BREAKFAST, "label": "Desayuno"},
        {"icon": ft.Icons.POOL, "label": "Piscina"},
        {"icon": ft.Icons.RESTAURANT, "label": "Restaurant"},
        {"icon": ft.Icons.LOCAL_PARKING, "label": "Parking"},
        {"icon": ft.Icons.PETS, "label": "Pet Friendly"}
    ]

    def extra_card(extra: dict):
        return ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Icon(
                        extra["icon"],
                        size=32,
                        color=COLOR_ACENTO
                    ),
                    bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                    border_radius=16,
                    padding=20,
                ),
                ft.Text(
                    extra["label"],
                    size=14,
                    weight="w600",
                    color=COLOR_TEXTO,
                    text_align=ft.TextAlign.CENTER
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12),
            padding=20,
        )

    return ft.Container(
        content=ft.Column([
            # Encabezado ultra moderno
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Text(
                            "SERVICIOS",
                            size=12,
                            weight="w600",
                            color=COLOR_ACENTO,
                          
                        ),
                        bgcolor=ft.Colors.with_opacity(0.1, COLOR_ACENTO),
                        padding=ft.padding.symmetric(horizontal=16, vertical=6),
                        border_radius=50,
                    ),
                    ft.Text(
                        "Nuestros Servicios",
                        size=40,
                        weight="w700",
                        color=COLOR_PRIMARIO,
                    ),
                    ft.Text(
                        "Experiencias diseñadas para su confort",
                        size=16,
                        color=COLOR_SECUNDARIO,
                    ),
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12),
                padding=ft.padding.only(bottom=48, top=24),
            ),

            # Sección de habitaciones
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(
                            "Tipos de Habitaciones",
                            size=28,
                            weight="w700",
                            color=COLOR_TEXTO,
                        ),
                    ]),
                    ft.Container(height=8),
                    ft.Container(
                        content=ft.Row(
                            [servicio_card(s) for s in servicios_data],
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True,
                            spacing=24,
                            run_spacing=24,
                        ),
                        padding=24,
                    ),
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                scroll=ft.ScrollMode.ALWAYS),
                bgcolor=COLOR_CARD,
                border_radius=20,
                padding=40,
                border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
            ),

            # Servicios incluidos
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Servicios Incluidos",
                        size=28,
                        weight="w700",
                        color=COLOR_TEXTO,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=16),
                    ft.Row(
                        [extra_card(e) for e in extras],
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        wrap=True,
                        spacing=16,
                        run_spacing=16,
                    ),
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0),
                bgcolor=COLOR_CARD,
                padding=40,
                border_radius=20,
                border=ft.border.all(1, ft.Colors.with_opacity(0.1, COLOR_TEXTO)),
            ),

        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=32,
        scroll=ft.ScrollMode.ALWAYS),
        padding=48,
        bgcolor=COLOR_FONDO,
    )