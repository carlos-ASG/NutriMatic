"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from NutriMatic.ui.auth.login.views.login_view import login_view
from NutriMatic.ui.auth.signup.views.signup_view import signup_view
from NutriMatic.ui.landing_page.views.landing_page import index


app = rx.App()
app.add_page(index)
app.add_page(login_view, route="/login")
app.add_page(signup_view, route="/signup")

