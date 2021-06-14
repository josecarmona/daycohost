# -*- coding: utf-8 -*-
{
    'name': "motives in crm",

    'summary': """
       Motivos para confirmar o cancelar una oportunidad  """,

    'description': """
        justificar razon en crm
    """,

    'author': "Luis Auyadermont",
    'website': "https://www.instagram.com/yurpro_21/?hl=es-la",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/motives.xml',
        'wizard/motive_wizard_view.xml',
        
    ],
    # only loaded in demonstration mode
    # ~ 'data': [
        # ~ 'demo/demo.xml',
    # ~ ],
}
