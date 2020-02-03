from api import create_app
from api.settings import ProdConfig

app = create_app(ProdConfig)
