# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

TYPE_SELECTION = [
    ('won', 'Ganada'),
    ('lost', 'Perdida')

]

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    motive_id = fields.Many2one('motives.proposal')
    
    motive_type = fields.Selection(string='Type Motive',related='motive_id.type_motive' ,selection=TYPE_SELECTION, store=True)

    

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

        



