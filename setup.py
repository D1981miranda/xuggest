import os
from setuptools import setup



def get_readme(fname):
    _path = os.path.join(os.path.dirname(__file__), fname)
    return open(_path).read()

    setup(
        name = 'xuggest',
        version = '0.0.1',
        author = 'Orson Adams',
        description = ('Prototype Autosuggest Pipelines in the Command line'),
        license = 'BSD',
        keywords = ['autosuggest', 'autocomplete'],
        url = 'orsonadams.com/projects/xuggest',
        packages = ['xuggest.*', 'tests'],
        install_requires = ['urwin'],
        long_description = read('./README.md'),
        classifiers = [
            'Development Status :: 1 - Planning',
            'Topic :: Frameworks, Utilities',
            'License :: OSI Approved :: BSD License',
        ])
