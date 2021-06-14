# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotivesProposal(models.Model):
    _name = "motives.proposal"
    _description = "Motives"

    
    name = fields.Char('Description',required=True)
    
    type_motive = fields.Selection([('won', 'Won'),
                              ('lost', 'Lost')],
                             'Type', default='won')
