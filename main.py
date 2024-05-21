from views.route import *
from views.nav_bar import *
from views.serial_key import *
def main(page: ft.Page):
    page.window_maximized = True
    # page.window_always_on_top=True -used for fix app in top ,other apps will be back
    # page.window_full_screen=True -minimize and max button will not come,only max window
    page.title = "Welcome"
    page.theme_mode = "light"
    page.fonts = {
        "TravelingTypewriter": "fonts/TravelingTypewriter.ttf"
    }
    create_serial_key_database()
    create_user_database()
    create_assembly_process_db()

    def route_change(e):
        e.page.views.clear()
        if not check_serial_key_exists():
            e.page.views.append(serial_key_view)
            e.page.update()
            logging.warning("Serial key added successfully.")
        else:
            result = check_serial_key_in_db_equal_with_system()
            if result:
                e.page.views.append(login_view)
            else:
                logging.warning("DB serial key and fetched serial key is not same.")
                e.page.views.append(serial_key_error_view)
                e.page.update()
                logging.warning("Serial key added successfully.")

        if e.page.route == "/login":
            e.page.views.append(login_view)
        if e.page.route == "/Home":

            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            hint.width=ft.Page.width
            e.page.views.append(
                ft.View(
                    "/Home",
                    [
                        app_bar,
                        menu,
                        color_qr_view,
                        ocr_object_view,
                        assembly_detection_view,
                        hint,

                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )
        if e.page.route == "/user":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            tb = tb_gen()
            e.page.views.append(ft.View(
                "/user",
                [
                    app_bar,
                    menu,
                    reg_button,
                    tb
                ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center",
            ))

        if e.page.route == "/User":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            tb = tb_gen()
            e.page.views.append(ft.View(
                "/User",
                [
                    app_bar,
                    menu,
                    reg_button,
                    tb
                ],
                scroll="always",
                vertical_alignment="center",
                horizontal_alignment="center",
            ))

        if e.page.route == "/edit":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            user_id = e.page.client_storage.get("data")
            user_name = get_username_by_id(user_id)
            user_field.value = user_name
            user_row_edit = user_row_edit_build(user_id)
            e.page.views.append(
                ft.View(
                    "/edit",
                    [
                        app_bar,
                        menu,
                        user_row_edit
                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )

        if e.page.route == "/password_change":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            user_id = e.page.client_storage.get("user_id")
            user_name = get_username_by_id(user_id)
            user_field.value = user_name
            pass_row = pass_row_build(user_id)
            e.page.views.append(
                ft.View(
                    "/edit",
                    [
                        app_bar,
                        menu,
                        pass_row
                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )

        if e.page.route == "/add_user":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            user_id = e.page.client_storage.get("user_id")
            user_name = get_username_by_id(user_id)
            user_field.value = user_name
            e.page.views.append(
                ft.View(
                    "/add_user",
                    [
                        app_bar,
                        menu,
                        new_user_view

                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )

        if e.page.route == "/camera":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            user_id = e.page.client_storage.get("user_id")
            user_name = get_username_by_id(user_id)
            user_field.value = user_name
            cam_tb = cam_tb_gen()
            e.page.views.append(
                ft.View(
                    "/add_user",
                    [
                        app_bar,
                        menu,
                        cam_tb
                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )

        if e.page.route == "/process":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            user_id = e.page.client_storage.get("user_id")
            user_name = get_username_by_id(user_id)
            user_field.value = user_name
            process_tb = process_list_gen()


            e.page.views.append(
                ft.View(
                    "/process",
                    [
                        app_bar,
                        menu,
                        process_tb
                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )


        if e.page.route == "/process_edit":
            admin = (e.page.client_storage.get("admin"))
            menu = get_menu_bar(e, admin)
            user_id = e.page.client_storage.get("user_id")
            user_name = get_username_by_id(user_id)
            user_field.value = user_name
            process = (e.page.client_storage.get("process"))
            print(process)
            edit_sec=edit_sec_gen(process)
            e.page.views.append(
                ft.View(
                    "/process_edit",
                    [
                        app_bar,
                        menu,
                        edit_sec

                    ],
                    scroll="always",
                    vertical_alignment="center",
                    horizontal_alignment="center",
                )
            )




        e.page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.update()

ft.app(target=main,assets_dir="assets")

