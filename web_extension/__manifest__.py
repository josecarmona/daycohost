# -*- coding: utf-8 -*-
{
    'name': "web_extension",

    'summary': """
        Restringe el boton archivar para un determinado grupo de usuarios""",

    'description': """
        Restringe el boton archivar para un determinado grupo de usuarios
    """,

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'security/security.xml',
    ],
   
}
