# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cicloModel(models.Model):
    _name='validations_app.ciclo_model'
    _description = 'Ciclos Model'


    name =fields.Char("Cycle Code",required=True,size=10,help="Name of Cycle")
    descripcion=fields.Html("Description",required=True,size=100,help="Input Description")
    
    modulos=fields.One2many("validations_app.modulo_model","ciclo","Modulos")
    
