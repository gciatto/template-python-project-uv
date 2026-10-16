import logging
from importlib.metadata import version

__version__ = version("uv-python-project-template")  # pyproject.toml is the only source

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main_package")
