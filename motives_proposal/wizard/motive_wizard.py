# coding: utf-8



from odoo import fields, models, api, exceptions, _
from odoo.exceptions import ValidationError


class MotiveWizard(models.TransientModel):

    _name = "motive.wizard"
    _description = "Wizard motives."


    motive_id = fields.Many2one('motives.proposal',required=True)
    

    def create_proposal(self):
        type_state=self._context.get('type')
        sale_obj = self.env['sale.order']
        motive_id = self.motive_id
        type_motive=self._context.get('type_motive')
        id_order=self._context.get('id_order') 
        

        sale_obj.browse(id_order).write({'motive_id': motive_id,'motive_type': type_motive})

        if type_state=='cancel':
            sale_obj.browse(id_order).write({'state': type_state})
        else:
            self.action_confirm()
            
        return True

    def action_confirm(self):
        id_order=self._context.get('id_order') 
        sale_obj = self.env['sale.order']
    
        if sale_obj._get_forbidden_state_confirm() & set(sale_obj.mapped('state')):
            raise UserError(_(
                'It is not allowed to confirm an order in the following states: %s'
            ) % (', '.join(sale_obj._get_forbidden_state_confirm())))

        for order in sale_obj.filtered(lambda order: order.partner_id not in order.message_partner_ids):
            order.message_subscribe([order.partner_id.id])
        sale_obj.browse(id_order).write({
            'state': 'sale',
            'date_order': fields.Datetime.now()
        })
        sale_obj._action_confirm()
        if sale_obj.env.user.has_group('sale.group_auto_done_setting'):
            sale_obj.action_done()
        return True

