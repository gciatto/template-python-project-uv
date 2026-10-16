import logging
from importlib.metadata import version

__version__ = version("uv-python-project-template")  # pyproject.toml is the only source

logger = logging.getLogger("main_package")
