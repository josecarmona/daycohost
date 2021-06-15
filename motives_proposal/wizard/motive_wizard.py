# coding: utf-8



from odoo import fields, models, api, exceptions, _
from odoo.exceptions import ValidationError


class MotiveWizard(models.TransientModel):

    _name = "motive.wizard"


    motive_id = fields.Many2one('motives.proposal',required=True)
    

    def create_proposal(self):
        type_motive=self._context.get('type')       
        sale_obj = self.env['sale.order']
        motive_id = self.motive_id
        sale_obj.browse(self._context.get('active_id')).write({'motive_id': motive_id})
        if type_motive=='cancel':
            sale_obj.browse(self._context.get('active_id')).write({'state': type_motive})
        else:
            self.action_confirm()
            
        return True

    def action_confirm(self):
        sale_obj = self.env['sale.order']
        if sale_obj._get_forbidden_state_confirm() & set(sale_obj.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(sale_obj._get_forbidden_state_confirm())))

        for order in sale_obj.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        sale_obj.browse(self._context.get('active_id')).write({
            'state': 'sale',
            'date_order': fields.Datetime.now()
        })
        sale_obj._action_confirm()
        if sale_obj.env.user.has_group('sale.group_auto_done_setting'):
            sale_obj.action_done()
        return True

