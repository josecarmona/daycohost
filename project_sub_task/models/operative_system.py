# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class operativesystem(models.Model):
    
    _name = 'project_sub_task.operativesystem'
    _description = 'Define los Sistemas Operativos para la instalación o clonación'

    operative_system = fields.Selection(
        [('windows', 'Windows'), ('linux', 'Linux')], string="Tipo SO", required=True)
    operative_system_arch = fields.Selection(
        [('32', '32 bits'), ('64', '64 bits')], string="Arquitectura del Sistema Operativo", required=True)

    #Relaciones entre tablas
    # Sist. Operativos - Distribucion
    operativesystemlayout_ids = fields.One2many('project_sub_task.operativesystemlayout','operativesystem_id',string='Distribución del Sistema Operativo')
    
class operativesystemlayout(models.Model):
    
    _name = 'project_sub_task.operativesystemlayout'
    _description = 'Define las distintas distribuciones de los Sistemas Operativos'

    windows = fields.Selection([('win_server_2003_estandar', 'Server 2003 estándar'),('win_server_2003_estandar_r2', 'Server 2003 estándar R2'),
    ('win_server_2008_estandar', 'Server 2008 estándar'),('win_server_2008_estandar_r2', 'Server 2008 estándar R2'),
    ('win_server_2012_estandar_r2', 'Server 2012 estándar R2'),('win_server_2016_estandar', 'Server 2016 estándar'),
    ('win_server_2019_estandar', 'Server 2019 estándar'),('win_xp_professional', 'XP Professional'),
    ('win_7_professional', '7 Professional'),('win_10_professional', '10 Professional')],string="Distribución")

    linux = fields.Selection([('linux_appliance', 'Appliance'),('linux_centOS', 'Linux CentOS'),
    ('linux_debian', 'Linux Debian'),('linux_fedora', 'Linux Fedora'),('linux_oracle', 'Linux Oracle'),
    ('linux_red_hat', 'Linux Red Hat'),('linux_suse', 'Linux SUSE'),('linux_ubuntu', 'Linux Ubuntu'),],string="Distribución")

    #Relaciones entre tablas:
    
    # Sist. Operativos - Distribucion
    operativesystem_id = fields.Many2one(
        'project_sub_task.operativesystem', string='Sistemas Operativos')

    # Distribucion - Version
    #operativesystemversion_ids = fields.One2many('project_sub_task.operativesystemversion', 'operativesystemlayout_id', string="Versión del Sistema Operativo")

class operativesystemversion(models.Model):
    
    _name = 'project_sub_task.operativesystemversion'
    _description = 'Define las distintas versiones de los Sistemas Operativos'

    linux_centOS = fields.Selection([('5', '5'),('6', '6'),('7', '7'),('8', '8')],string="Linux CentOS")
    linux_debian = fields.Selection([('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10')],string="Linux Debian")
    linux_fedora = fields.Selection([('22', '22'),('23', '23'),('24', '24'),('25', '25'),('26', '26'),
    ('27', '27'),('28', '28'),('29', '29'),('30', '31'),('32', '32'),
    ('33', '33'),('34', '34'),('35', '35')],string="Linux Fedora")
    linux_oracle = fields.Selection([('6', '6'),('7', '7'),('8', '8')],string="Linux Oracle")
    linux_red_hat = fields.Selection([('5', '5'),('6', '6'),('7', '7'),('8', '8')],string="Linux Red Hat")
    linux_suse = fields.Selection([('11_sp4', '11 SP4'),('12_sp5', '12 SP5'),('15_sp2', '15 SP2')],string="Linux SUSE")
    linux_ubuntu = fields.Selection([('14_04_6_lts', '14.04.6 LTS'),('16_04_7_lts', '16.04.7 LTS'),('18_04_5_lts', '18.04.5 LTS'),('20_04_2_lts', '20.04.2 LTS')],string="Linux Ubuntu")
    
    #Relaciones entre tablas
    # Distribucion - Version
    #operativesystemlayout_id = fields.Many2one(
    #    'project_sub_task.operativesystemlayout', string='Distribución del Sistema Operativo',)
