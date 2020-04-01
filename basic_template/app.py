import pymongo
from basic_template.blog import Blog
from basic_template.menu import Menu
from basic_template.post import Post
from basic_template.database import Database

Database.initialize()

menu = Menu()

menu.run_menu()
