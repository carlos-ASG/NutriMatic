"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from NutriMatic.ui.nutri_home.views.nutri_home_view import nutri_home_view
from NutriMatic.ui.expediente_clinico.view.expediente_clinico_view import expediente_clinico_view 
from NutriMatic.ui.auth.views.login_view import login_view
from NutriMatic.ui.auth.views.signup_view import signup_view
from NutriMatic.ui.landing_page.views.landing_page import index


app = rx.App()
app.add_page(index)
app.add_page(login_view, route="/login")
app.add_page(signup_view, route="/signup")
app.add_page(nutri_home_view, route="/nutri-home")
app.add_page(expediente_clinico_view, route="/expediente-clinico")





