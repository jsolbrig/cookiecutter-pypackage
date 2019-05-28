#!/usr/bin/env python
import os
from glob import glob

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_directory(dirpath):
    for fname in glob('{}/*'.format(os.path.join(PROJECT_DIRECTORY, dirpath))):
        remove_file(fname)
    os.rmdir(os.path.join(PROJECT_DIRECTORY, dirpath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_pytest }}' == 'y':
        remove_file('tests/__init__.py')

    # if '{{ cookiecutter.make_satpy_composite }}' != 'y':
    #     remove_directory('{{cookiecutter.project_slug}}/composites')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
