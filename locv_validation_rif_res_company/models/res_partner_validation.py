# -*- coding: UTF-8 -*-
#    type of the change:  Created
#    Comments: Creacion de generacion de codigo para clientes y proveedores (depends for res_partner)



from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import re

class RespartnerRif(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        partner = super().create(vals)
        # Se valida si el partner tiene un padre asociado, entonces
        # el mismo se considera como un contacto asociado al cliente o proveedor
        # por lo cual no se aplican la validaciones de RIF y email para clientes y proveedores.
        if not partner.parent_id:
            partner.validate_vat_and_email()
        return partner
    
    def write(self, vals):
        res = super().write(vals)
        partners = self.filtered(lambda r: not r.parent_id)
        if partners:
            partners.validate_vat_and_email()
        return res
    
    def validate_vat_and_email(self):
        for partner in self:
            vat = partner.vat or ''
            email = partner.email or ''
            if vat:
                domain = [('vat', '=', vat), ('id', '!=', partner.id), 
                    '!', ('id', 'child_of', partner.id)]
                partner_count = self.search_count(domain)
                if partner_count:
                    raise UserError('El cliente o proveedor ya se encuentra registrado' 
                    ' con el rif: %s y se encuentra activo' %vat)
                
                if self.validate_rif(vat) is False:
                    raise UserError('El rif tiene el formato incorrecto. Ej:' 
                        'V-012345678, E-012345678, J-012345678 o G-012345678. Por favor'
                        'verifique el formato y si posee los 9 digitos como se indica en' 
                        'el Ej. e intente de nuevo')
            
            if email:
                if self.validate_email_addrs(email) is False:
                    raise UserError('El email es incorrecto. Ej: cuenta@dominio.xxx.' 
                        'Por favor intente de nuevo')

    @api.model
    def validate_rif(self, field_value):
        rif_obj = re.compile(r"^[V|E|J|G]+[-][\d]{9}", re.X)
        if rif_obj.search(field_value.upper()):
            if len(field_value) == 11:
                return True
            else:
                return False
        return False

    @api.model 
    def validate_email_addrs(self, email):
        res = False
        mail_obj = re.compile(r"""
                \b             # comienzo de delimitador de palabra
                [\w.%+-]       # usuario: Cualquier caracter alfanumerico mas los signos (.%+-)
                +@             # seguido de @
                [\w.-]         # dominio: Cualquier caracter alfanumerico mas los signos (.-)
                +\.            # seguido de .
                [a-zA-Z0-9]{1,10}    # dominio de alto nivel: 2 a 6 letras en minúsculas o mayúsculas.
                \b             # fin de delimitador de palabra
                """, re.X)     # bandera de compilacion X: habilita la modo verborrágico, el cual permite organizar
                               # el patrón de búsqueda de una forma que sea más sencilla de entender y leer.
        if mail_obj.search(email):
            res = True
        return res

    @api.constrains('function', 'x_studio_departamento', 'phone', 'mobile', 'x_studio_telfono_2', 'x_studio_movil_2', 'website', 'x_studio_correo_secundario')
    def _check_something(self):
        flag = 0
        for record in self:
            mensaje = "Error en los Campos:"

            if record.x_studio_departamento != False:
                regex = '^[a-zA-Z\s]*$'
                if (re.search(regex, str(record.x_studio_departamento))):
                    aja = 1
                else:
                    flag = 1
                    app = "Departamento solo puede contener letras"
                    mensaje = mensaje + "  \n " + app
            if record.function != False:
                regex = '^[a-zA-Z\s]*$'
                if (re.search(regex, str(record.function))):
                    aja = 1
                else:
                    flag = 1
                    app = "Cargo solo puede contener letras"
                    mensaje = mensaje + "  \n " + app
            if record.phone != False:
                regex = '^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
                if (re.search(regex, str(record.phone))):
                    aja = 1
                else:
                    flag = 1
                    app = "Formato erroneo de Telefono"
                    mensaje = mensaje + "  \n " + app
            if record.mobile != False:
                regex = '^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
                if (re.search(regex, str(record.mobile))):
                    aja = 1
                else:
                    flag = 1
                    app = "Formato erroneo de Móvil"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_telfono_2 != False:
                regex = '^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
                if (re.search(regex, str(record.x_studio_telfono_2))):
                    aja = 1
                else:
                    flag = 1
                    app = "Formato erroneo de Telefono 2"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_movil_2 != False:
                regex = '^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
                if (re.search(regex, str(record.x_studio_movil_2))):
                    aja = 1
                else:
                    flag = 1
                    app = "Formato erroneo de Móvil 2"
                    mensaje = mensaje + "  \n " + app
            if record.website != False:
                regex = '((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'
                if (re.search(regex, str(record.website))):
                    aja = 1
                else:
                    flag = 1
                    app = "Formato erroneo de Sitio Web"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_correo_secundario != False:
                regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if (re.search(regex, str(record.x_studio_correo_secundario))):
                    aja = 1
                else:
                    flag = 1
                    app = "Formato erroneo de Correo Secundario"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_ranking_en_el_sector != False:
                regex = '^[0-9#]+$'
                if (re.search(regex, str(record.x_studio_ranking_en_el_sector))):
                    aja = 1
                else:
                    flag = 1
                    app = "Ranking del secto solo puede contener números"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_nmero_de_empleados != False:
                regex = '^[0-9]+$'
                if (re.search(regex, str(record.x_studio_nmero_de_empleados))):
                    aja = 1
                else:
                    flag = 1
                    app = "Número de empleados solo puede contener números"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_nmero_de_sedes_yo_sucursales != False:
                regex = '^[0-9]+$'
                if (re.search(regex, str(record.x_studio_nmero_de_sedes_yo_sucursales))):
                    aja = 1
                else:
                    flag = 1
                    app = "Número de sedes solo puede contener números"
                    mensaje = mensaje + "  \n " + app
            if record.x_studio_aos_en_el_mercado != False:
                regex = '^[0-9]+$'
                if (re.search(regex, str(record.x_studio_aos_en_el_mercado))):
                    aja = 1
                else:
                    flag = 1
                    app = "Años en el mercado solo puede contener números"
                    mensaje = mensaje + "  \n " + app

            if flag == 1:
                raise ValidationError(mensaje)
