from aiohttp import web
from server.routes import setup_routes
import aiohttp_jinja2
import jinja2

from server.settings import config, BASE_DIR
from db import close_pg, init_pg

app = web.Application()
app['config'] = config
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'server' / 'templates')))
setup_routes(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

web.run_app(app)



