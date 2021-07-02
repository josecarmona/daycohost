# -*- coding: utf-8 -*-
{
    'name': "opportunity_id_visible",
    'summary': "The field opportunity_id is visible for all users",
    'author': "IT Sales",
    'version': '0.1',
    'depends': ['base', 'sale_crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/opportunity_id.xml',
    ],
    
}
