from setuptools import setup, find_packages

# Loads _version.py module without importing the whole package.
def get_version_and_cmdclass(package_name):
    import os
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location('version',
                                   os.path.join(package_name, '_version.py'))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__version__, module.cmdclass

version, cmdclass = get_version_and_cmdclass('ersilia')

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

install_requires = [
    "bentoml==0.9.2",
    "PyGitHub",
    "autologging",
    "streamlit",
    "pygit2",
    "osfclient",
    "joblib",
    "hashids",
    "bioservices",
    "biopython",
    "chembl_webresource_client",
    "markdown",
    "pycrypto",
    "python-dateutil<2.8.1,>=2.1",
    "urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1",
    "requests<=2.24",
    "dockerfile-parse"
]

test_requires = []

dev_requires = [] + test_requires

docs_requires = []

dev_all = install_requires + dev_requires + docs_requires

yatai_service = []

extras_require = {
    "dev": dev_all,
    "doc_builder": docs_requires + install_requires,  # required by readthedocs.io
    "test": test_requires,
    "yatai_service": yatai_service + install_requires,
}

setup(
    name='ersilia',
    version=version,
    cmdclass=cmdclass,
    author='Ersilia Open Source Initiative',
    author_email='hello@ersilia.io',
    url='https://github.com/ersilia-os/ersilia',
    description='Ersilia model hub for open source drug discovery',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    packages=find_packages(exclude=("utilities")),
    entry_points={
        'console_scripts': [
            'ersilia=ersilia.cli:cli'
        ]
    },
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ),
    keywords='drug-discovery machine-learning ersilia open-science global-health model-hub',
    project_urls={
        "Landing page": "http://ersilia.io",
        "Models": "https://github.com/ersilia-os/eos-models/",
        "Source Code": "https://github.com/ersilia-os/ersilia/",
    },
    include_package_data=True,
)
