# -*- coding: utf-8 -*-
{
    'name': "Filtro de actividades en CRM",

    'summary': """
        FIltro para ver actividades activas y no activas en CRM""",

    'description': """
        FIltro en la table de actividades de CRM para poder mostrar tanto las actividades activas como las inactivas
    """,

    'author': "IT Sales",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'CRM',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        # 'models/crm_type.py',
        'views/filter_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
