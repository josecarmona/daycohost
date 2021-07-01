# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'
    # _name = 'crm.lead2opportunity.partner'
    # _description = 'Convert Lead to Opportunity (not in mass)'
 
    @api.model
    def default_get(self, fields):
        result = super(Lead2OpportunityPartner, self).default_get(fields)
        result['action'] = 'exist'
        result['name'] = 'convert'
        return result
       