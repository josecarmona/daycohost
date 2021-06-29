# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

TYPE_SELECTION = [
    ('awon', 'Won'),
    ('lost', 'Lost')

]

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    motive_id = fields.Many2one('motives.proposal')
    
    motive_type = fields.Selection(string='Type Motive' ,selection=TYPE_SELECTION, store=True)

    cant_edit = fields.Boolean(string="cant edit",compute="_compute_cant_edit")

    def action_confirm(self):
        ctx = self._context.copy()
        domain= [('type_motive', '=', 'awon')]
        search=self.env['motives.proposal'].search(domain)
        ctx['reason']=[x.id for x in search]
        ctx['type'] ='sale'
        ctx['type_motive'] ='awon'
        ctx['id_order'] =self.id

        return {
            'name': _('Motive Proposal'),
            'type': 'ir.actions.act_window',
            'res_model': 'motive.wizard',
            'view_mode': 'form',
            'context': ctx,
            'target': 'new',
        }

    def _compute_cant_edit(self):
        l=self.user_has_groups("base.user_admin")
        if self.user_has_groups("base.user_admin"):
            self.cant_edit =True
        else:
            self.cant_edit =False

    def action_cancel(self):
        ctx = self._context.copy()

        domain= [('type_motive', '=', 'lost')]
        search=self.env['motives.proposal'].search(domain)
        ctx['reason']=[x.id for x in search]
        ctx['type'] ='cancel'
        ctx['type_motive'] ='lost'
        ctx['id_order'] =self.id

        return {
            'name': _('Motive Proposal'),
            'type': 'ir.actions.act_window',
            'res_model': 'motive.wizard',
            'view_mode': 'form',
            'context': ctx,
            'target': 'new',
        }

        

    @api.onchange('motive_type')
    def _onchange_motive_type(self):

        for rec in self:
            if rec.state=='sale':
                rec.motive_type='awon' 
            if rec.state=='cancel':
                rec.motive_type='lost'
            return {'domain': {'motive_id': [('type_motive', '=', rec.motive_type)]}}
