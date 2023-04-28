from setuptools import setup, find_packages

config = {
    'description': 'A template for ms-mint-app plugins',
    'author': 'Soren Wacker',
    'url': 'https://github.com/sorenwacker',
    'download_url': 'https://github.com/sorenwacker/ms_mint_plugin_template',
    'author_email': 'swacker@ucalgary.ca',
    'version': '0.0.1',
    'install_requires': [],
    'packages': find_packages(),
    'scripts': [],
    'name': 'ms_mint_app_plugin',
    'entry_points': {
        "ms_mint_app.plugins": [
            "ms_mint_app_plugin = ms_mint_app_plugin.plugin:TemplatePlugin",
        ]
    },    
}

setup(**config)
