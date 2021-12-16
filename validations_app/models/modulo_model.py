# -*- coding: utf-8 -*-

from odoo import models, fields, api
class moduloModel(models.Model):
    _name='validations_app.modulo_model'
    _description = 'Modulo Model'

    name=fields.Char("Name",required=True)
    descripcion=fields.Html("Description",required=True)
    horas=fields.Integer("Hourly load (Hours)",required=True)
    

    ciclo = fields.Many2one("validations_app.ciclo_model","Cicle")
