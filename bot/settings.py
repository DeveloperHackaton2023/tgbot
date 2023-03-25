import os
import logging
import logging.config

from dotenv import load_dotenv


# Logging config
logging.basicConfig(level=logging.WARNING,
                    format='%(name)s::%(levelname)s::%(message)s')
logger = logging.getLogger(__name__)


# Environmental variables
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
NOTION_API_TOKEN = os.getenv('NOTION_API_TOKEN')
DB_URL = os.getenv('DB_URL')
API_SERVER_URL = os.getenv('API_SERVER_URL')
API_URL = os.getenv('API_URL')


ADMINS = [
    897651738
]


MODELS = [
    'models.users',
]


DEFAULT_COMMANDS = {
    'list': 'list of possible bot commands',
    'register': 'register',
    'add_ticket': 'create issue',
}
