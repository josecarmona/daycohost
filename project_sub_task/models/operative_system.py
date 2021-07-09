# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class OperativeSystem(models.Model):
    _name = 'operative.system'

    operative_system_list = ['Linux', 'Linux Centos', 'Linux Debian', 'Linux Fedora',
                             'Linux Oracle', 'Linux Red Hat', 'Linux SUSE', 'Linux Ubuntu', 'Windows']
