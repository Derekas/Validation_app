# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random

class alumnosModel(models.Model):
    _name = 'validations_app.alumnos_model'
    _description = 'Alumnos Model'

    name = fields.Char(string="Student Name",required=True,index=True)
    password = fields.Char(string='Password', required=True,size=10,help="Password Students")
    foto = fields.Binary(string='Photo', required=True)
    edad = fields.Integer(string='Age', required=True,index=True)
    localidad = fields.Char(string='Location', required=True,help="Input Location",size=100)
    provincia = fields.Char(string='Province', required=True,help="Input Province",size=100)
    email = fields.Char(string='Email', required=True,size=100,help="Input Gmail")

    convalidaciones=fields.One2many("validations_app.conva_model","alumno_id",string="Convalidaciones")
    
    def generatePassword(self):
        self.password=""
        for i in range (10):
            self.password+=random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") 
