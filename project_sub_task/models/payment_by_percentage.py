# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class paymentbyprencentage(models.Model):
    _name = 'paymentbyprencentage'
    _description = 'Pagos por Porcentajes'

    percentage_value = fields.Float(string="Valor del Porcentaje (%)")
    estimated_payment_date = fields.Date(string="Fecha estimada de pago")
    amount = fields.Float(string="Monto (US $)")
    projectsubtask_id = fields.Many2one(string='Proyectos', comodel_name='project.task')

class partpaymentsfixedamounts(models.Model):
    _name = 'partpaymentsfixedamounts'
    _description = 'Pagos partes o cantidades fijas'

    number_of_parts = fields.Float(string="Número de partes")
    estimated_payment_date = fields.Date(string="Fecha estimada de pago")
    amount = fields.Float(string="Monto (US $)")
    projectsubtaskamount_id = fields.Many2one(string='Proyectos', comodel_name='project.task')
        