# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = 'sale.order'


    reason_id = fields.Many2one('motives.proposal')
    
    

    def action_confirm(self):
        ctx = self._context.copy()
        domain= [('type_motive', '=', 'won')]
        search=self.env['motives.proposal'].search(domain)
        ctx['reason']=[x.id for x in search]
        ctx['type'] ='sale'
        return {
            'name': _('Motive Proposal'),
            'type': 'ir.actions.act_window',
            'res_model': 'motive.wizard',
            'view_mode': 'form',
            'context': ctx,
            'target': 'new',
        }



    def action_cancel(self):
        ctx = self._context.copy()

        domain= [('type_motive', '=', 'lost')]
        search=self.env['motives.proposal'].search(domain)
        ctx['reason']=[x.id for x in search]
        ctx['type'] ='cancel'

        return {
            'name': _('Motive Proposal'),
            'type': 'ir.actions.act_window',
            'res_model': 'motive.wizard',
            'view_mode': 'form',
            'context': ctx,
            'target': 'new',
        }

        


    # ~ @api.model
    # ~ def create(self, vals):
        # ~ self.search_norder_report(vals['norder_report'])
        # ~ res = super().create(vals)

        # ~ return res

    # ~ def write(self, vals):
        # ~ self.search_norder_report(vals['norder_report'])
        # ~ super().write(vals)

        # ~ return True
    # ~ def search_norder_report(self, norder_report):
        # ~ domain= [('norder_report', '=', norder_report)]
        # ~ search=self.env['product.category'].search(domain)
        # ~ if search:
            # ~ raise ValidationError('Este número ya está asignado en una categoría!')
  
        # ~ return True

    # ~ @api.model
    # ~ def create(self, vals):
        # ~ self.search_norder_report(vals['norder_report'])
        # ~ res = super().create(vals)

        # ~ return res

    # ~ def write(self, vals):
        # ~ self.search_norder_report(vals['norder_report'])
        # ~ super().write(vals)

        # ~ return True
