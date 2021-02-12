# -*- coding: utf-8 -*-
from odoo import http

# class /home/luis/dev11/l10nVeStateMunicipalityParish(http.Controller):
#     @http.route('//home/luis/dev_11/l10n_ve_state_municipality_parish//home/luis/dev_11/l10n_ve_state_municipality_parish/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/luis/dev_11/l10n_ve_state_municipality_parish//home/luis/dev_11/l10n_ve_state_municipality_parish/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/luis/dev_11/l10n_ve_state_municipality_parish.listing', {
#             'root': '//home/luis/dev_11/l10n_ve_state_municipality_parish//home/luis/dev_11/l10n_ve_state_municipality_parish',
#             'objects': http.request.env['/home/luis/dev_11/l10n_ve_state_municipality_parish./home/luis/dev_11/l10n_ve_state_municipality_parish'].search([]),
#         })

#     @http.route('//home/luis/dev_11/l10n_ve_state_municipality_parish//home/luis/dev_11/l10n_ve_state_municipality_parish/objects/<model("/home/luis/dev_11/l10n_ve_state_municipality_parish./home/luis/dev_11/l10n_ve_state_municipality_parish"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/luis/dev_11/l10n_ve_state_municipality_parish.object', {
#             'object': obj
#         })