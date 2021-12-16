# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cicloModel(models.Model):
    _name='validations_app.ciclo_model'
    _description = 'Ciclos Model'


    name =fields.Char("Cycle Code",required=True)
    descripcion=fields.Html("Description",required=True)
    
    modulos=fields.One2many("validations_app.modulo_model","ciclo","Modulos")
    
