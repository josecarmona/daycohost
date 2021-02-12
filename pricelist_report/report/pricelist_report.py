# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import time
import datetime 
from odoo import models, api, fields


class ReportProductpPricelistReport(models.AbstractModel):
    _name = "report.pricelist_report.report_pricelist"
    _description = "Exam Marksheet Report"



    def get_lines(self, obj):
        domain= [('product_tmpl_id', '=', obj.id),'|',('date_start','=',False),
        ('date_end','=',False)]
        lines=[]
        search=self.env['product.pricelist.item'].search(domain)
        search = search.filtered(lambda r: (r.date_start == False or r.date_start <= fecha_actual) and (r.date_end == False or r.date_end >= fecha_actual) )
        for line in search:
            lines.append(line)

        return lines

    def get_date(self, date):
        date1 = fields.Date.to_date(date)
        return str(date1.month) + ' / ' + str(date1.year)

    def get_total(self, result_line):
        total = [x.exam_id.total_marks for x in result_line]
        return sum(total)

    @api.model
    def _get_report_values(self, docids, data=None):
        product_ids=self.env['product.pricelist.item'].search([])
        date_now=datetime.date.today()
        filter_product = product_ids.filtered(lambda r: (r.date_start == False or r.date_start <= date_now) and (r.date_end == False or r.date_end >= date_now) )
  
        product_ids=sorted([ x.product_tmpl_id for x in filter_product if x.product_tmpl_id and x.product_tmpl_id.active==True],key = lambda x:(x.categ_id.norder_report,x.name)  )
        
        line_ids=docids
        docs={}
        for product in product_ids:
            domain= [('product_tmpl_id', '=', product.id)]
            search=self.env['product.pricelist.item'].search(domain)
            docs[product]=[]
            for x in search:
	            docs[product].append(x)

   
        
        docargs = {
            'doc_model': 'product.pricelist.item',
            'docs': docs,
            'line_ids': line_ids,
            'time': time,
            'get_lines': self.get_lines,
            'get_date': self.get_date,
            'get_total': self.get_total,
        }
        return docargs
