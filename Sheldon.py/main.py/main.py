import flet as ft
from paginas.inicio import inicio
from paginas.sobre_nosotros import sobre_nosotros
from paginas.servicios import servicios
from paginas.contactos import contactos
from paginas.reservas import reserva


def main(page: ft.Page):
    # Colores del tema ultra moderno
    COLOR_PRIMARIO = "#625956"  # Slate 900 - Muy oscuro
    COLOR_SECUNDARIO = "#475569"  # Slate 600 - Medio
    COLOR_ACENTO = "#d89c6c"  # Blue 500 - Azul vibrante
    COLOR_FONDO = "#ede8e4"  # Slate 50 - Casi blanco
    COLOR_TEXTO = "#152540"  # Slate 950 - Negro azulado
    COLOR_CARD = "#edebeb"  # Blanco puro
    
    page.title = "Hotel Sheldon"
    page.window.maximized = True
    page.theme_mode = "light"
    page.scroll = "auto"
    page.bgcolor = COLOR_FONDO

    selected_section = ft.Ref[ft.Text]()
    selected_section.current = ft.Text("Inicio")

    main_content = ft.Column([], expand=True)
    
    # Logo minimalista
    logo = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Icon(
                    ft.Icons.APARTMENT,
                    size=20,
                    color=COLOR_CARD
                ),
                bgcolor=COLOR_PRIMARIO,
                border_radius=8,
                padding=8,
            ),
            ft.Text(
                "SHELDON",
                size=14,
                weight="w700",
                color=COLOR_PRIMARIO,
            ),
        ], spacing=12),
        padding=10,
    )
    
    nav_bar = ft.Row(alignment=ft.MainAxisAlignment.END, spacing=4)

    def go_to(section):
        section = section.lower()
        selected_section.current.value = section.capitalize()

        nav_bar.controls.clear()
        for name in ["Inicio", "Sobre Nosotros", "Servicios", "Contactos", "Reservas"]:
            is_selected = selected_section.current.value == name
            
            if is_selected:
                btn = ft.Container(
                    content=ft.Text(
                        name,
                        size=14,
                        weight="w600",
                        color=COLOR_CARD,
                    ),
                    bgcolor=COLOR_PRIMARIO,
                    padding=ft.padding.symmetric(horizontal=24, vertical=12),
                    border_radius=40,
                    ink=True,
                    on_click=lambda e, s=name: go_to(s),
                )
            else:
                btn = ft.Container(
                    content=ft.Text(
                        name,
                        size=14,
                        weight="w500",
                        color=COLOR_SECUNDARIO,
                    ),
                    padding=ft.padding.symmetric(horizontal=24, vertical=12),
                    border_radius=50,
                    ink=True,
                    on_click=lambda e, s=name: go_to(s),
                    on_hover=lambda e: None,
                )
            
            nav_bar.controls.append(btn)

        main_content.controls.clear()
        if section == "inicio":
            main_content.controls.append(inicio(page, go_to))
        elif section == "sobre nosotros":
            main_content.controls.append(sobre_nosotros(page))
        elif section == "servicios":
            main_content.controls.append(servicios(page))
        elif section == "contactos":
            main_content.controls.append(contactos(page))
        elif section == "reservas":
            main_content.controls.append(reserva(page))

        page.update()

    go_to("inicio")

    # Navbar ultra moderna - flotante y minimalista
    nav_container = ft.Container(
        content=ft.Container(
            content=ft.Row([
                logo,
                ft.Container(expand=True),
                nav_bar,
            ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor=COLOR_CARD,
            padding=ft.padding.symmetric(horizontal=25, vertical=16),
            border_radius=16,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=24,
                color=ft.Colors.with_opacity(0.08, COLOR_TEXTO),
                offset=ft.Offset(0, 4),
            ),
        ),
        padding=ft.padding.symmetric(horizontal=24, vertical=16),
    )

    page.add(
        nav_container,
        ft.Container(
            content=main_content,
            expand=True,
            alignment=ft.alignment.top_center
        )
    )


ft.app(target=main)