from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DATA_FILE = env.str("DATA_FILE")
if ENV == "development":
    DEBUG = True
