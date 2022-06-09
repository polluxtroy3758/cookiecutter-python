import re
import sys

PACKAGE_NAME_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

package_name = "{{ cookiecutter.package_slug }}"

if not re.match(PACKAGE_NAME_REGEX, package_name):
    print(f"ERROR: {package_name} is not a valid Python package name!")

    sys.exit(1)
