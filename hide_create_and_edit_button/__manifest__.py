# -*- coding: utf-8 -*-
{
    'name': "hide_create_and_edit_button",

    'summary': """
        Hide creat and edit button in crm opportunity""",

    'author': "IT Sales",

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/security.xml',
    ],
}
