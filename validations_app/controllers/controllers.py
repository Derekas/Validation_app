# -*- coding: utf-8 -*-
# from odoo import http


# class ValidationsApp(http.Controller):
#     @http.route('/validations_app/validations_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/validations_app/validations_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('validations_app.listing', {
#             'root': '/validations_app/validations_app',
#             'objects': http.request.env['validations_app.validations_app'].search([]),
#         })

#     @http.route('/validations_app/validations_app/objects/<model("validations_app.validations_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('validations_app.object', {
#             'object': obj
#         })
