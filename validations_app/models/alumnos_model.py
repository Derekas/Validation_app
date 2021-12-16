# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random

class alumnosModel(models.Model):
    _name = 'validations_app.alumnos_model'
    _description = 'Alumnos Model'

    name = fields.Char("Student Name",required=True)
    password = fields.Char('Password', required=True)
    foto = fields.Binary('Photo', required=True)
    edad = fields.Integer('Age', required=True)
    localidad = fields.Char('Location', required=True)
    provincia = fields.Char('Province', required=True)
    email = fields.Char('Email', required=True)

    convalidaciones=fields.One2many("validations_app.conva_model","alumno_id","Convalidaciones")
    
    def generatePassword(self):
        self.password=""
        for i in range (10):
            self.password+=random.choice("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") 
