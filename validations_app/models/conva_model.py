# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class convaModel(models.Model):
    _name='validations_app.conva_model'
    _description = 'Convalidaciones Model'

    fecha=fields.Date("Date",required=True,help="Date")

    modulo_id=fields.Many2one("validations_app.modulo_model","Modules")
    alumno_id=fields.Many2one("validations_app.alumnos_model","Students")


    
