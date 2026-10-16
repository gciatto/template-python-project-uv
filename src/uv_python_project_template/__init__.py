import logging
from importlib.metadata import version

__version__ = version("uv-python-project-template")  # pyproject.toml is the only source

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("uv_python_project_template")


class MyClass:
    def my_method(self):
        return "Hello World"


logger.info("uv_python_project_template loaded")
