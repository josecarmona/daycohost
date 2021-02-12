# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class ProductCategory(models.Model):
    _inherit = 'product.category'

    norder_report = fields.Integer('Report order number')


    def search_norder_report(self, norder_report):
        domain= [('norder_report', '=', norder_report)]
        search=self.env['product.category'].search(domain)
        if search:
            raise ValidationError('Este número ya está asignado en una categoría!')
  
        return True

    @api.model
    def create(self, vals):
        self.search_norder_report(vals['norder_report'])
        res = super().create(vals)

        return res

    def write(self, vals):
        self.search_norder_report(vals['norder_report'])
        super().write(vals)

        return True
