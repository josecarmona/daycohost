# -*- coding: utf-8 -*-
{
    'name': "project_sub_task",

    'summary': """
        Personalización del módulo Proyecto""",

    'description': """
        Personalización del módulo Proyecto
    """,

    'author': "ITSALES",
    'website': "https://www.itsalescorp.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/server_installation.xml',
        'views/clone_server.xml',
        'views/expansion_decrease.xml',
        'views/links.xml',
        'views/internet_service.xml',
        'views/security_service.xml',
        'views/placement.xml',
        'views/cabling_utp.xml',
        'views/cabling_fo.xml',
        'views/coaxial_wiring.xml',
        'views/additional_resources.xml',
        'views/production_pass.xml',
    ],
}
