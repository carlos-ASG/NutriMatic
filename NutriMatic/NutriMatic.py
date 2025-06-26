"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from sqlalchemy import create_engine

from NutriMatic.ui.nutri_home.views.nutri_home import nutri_home_view
from rxconfig import config

from NutriMatic.ui.auth.login.views.login_view import login_view
from NutriMatic.ui.auth.signup.views.signup_view import signup_view
from NutriMatic.ui.landing_page.views.landing_page import index


app = rx.App()
app.add_page(index)
app.add_page(login_view, route="/login")
app.add_page(signup_view, route="/signup")
app.add_page(nutri_home_view, route="/nutri-home")

# Create the SQLAlchemy engine
engine = create_engine(config.database_url)



