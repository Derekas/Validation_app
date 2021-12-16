# -*- coding: utf-8 -*-

from odoo import models, fields, api
class profesorModel(models.Model):
    _name='validations_app.profesor_model'
    _description = 'Modelo de Profesores'


    name =fields.Char("Name",required=True,index=True)
    apellidos =fields.Char("Surname",required=True,index=True)
    foto=fields.Binary()
    dni=fields.Char("DNI",required=True)
    

    alumnos = fields.Many2many("validations_app.alumnos_model","Alumnos")
