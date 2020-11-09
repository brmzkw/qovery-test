from setuptools import find_packages, setup
import os
import re


PACKAGE = 'qovery_test'

DEPENDENCIES = [
    'flask',
    'flask-sqlalchemy',
]

TEST_DEPENDENCIES = [
]


def get_pkgvar(name):
    here = os.path.abspath(os.path.dirname(__file__))
    init_path = os.path.join(here, PACKAGE, '__init__.py')

    # Cache file content into get_pkgvar.init_content to avoid reading the
    # __init__.py file several times.
    if not hasattr(get_pkgvar, 'init_content'):
        with open(init_path) as handle:
            get_pkgvar.init_content = handle.read().splitlines()

    for line in get_pkgvar.init_content:
        res = re.search(r'^%s\s*=\s*["\'](.*)["\']' % name, line)
        if res:
            return res.groups()[0]

    raise ValueError('%s not found in %s' % (name, init_path))


setup(
    name=PACKAGE.replace('_', '-'),
    version='0.1.0',
    description='qovery test',
    packages=find_packages(),
    install_requires=DEPENDENCIES
)
