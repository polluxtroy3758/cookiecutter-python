{%- if cookiecutter.python_version.split('.')[1]|int >= 8 %}
from importlib import metadata
{%- else %}
import importlib_metadata as metadata
{%- endif %}

__version__ = metadata.version("{{ cookiecutter.package_slug }}")
