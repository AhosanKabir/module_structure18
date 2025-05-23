{
    'name': 'Module Name',
    'version': '18.0.0.1',
    'depends': [],
    'author': 'Author Name',
    'co-author': 'Co-Author name',
    'category': '',
    'website': 'https://company_website_url.com', #if available
    'license': 'LGPL-3',
    'sequence': 10,
    'summary': """
        module summary goes to here
    """,
    'description': """
        module details goes to here
    """,
    'data': [
        # 'security/ir.model.access.csv',
        # "views/templates.xml"
    ],
    'assets': {
        'web.assets_frontend': [
            # '/module_name/static/src/js/.js',
            # '/module_name/static/src/xml/.xml',
            # '/module_name/static/src/scss/.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
