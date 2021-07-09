# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class ProjectSubTask(models.Model):
    _inherit = 'project.task'
    
    edt = fields.Char(string="EDT", required=True)
    service_type = fields.Selection([('instalar_servidor', 'Instalar Servidor'), (
        'clonar_servidor', 'Clonar Servidor'), ('ampliacion_disminucion_servicio', 'Ampliación o Disminución de Servicio'),
        ('enlaces', 'Enlaces'), ('servicio_internet', 'Internet'), ('servicio_seguridad', 'Servicio de Seguridad'), 
        ('colocacion', 'Colocación'), ('cableado_utp', 'Cableado UTP'), ('cableado_fo', 'Cableado FO'), 
        ('cableado_coaxial', 'Cableado Coaxial'), ('recursos_adicionales', 'Recursos Adicionales'), 
        ('pase_produccion', 'Pase a Producción')], string="Tipo de Servicio", required=True)
    percentage_progress = fields.Float(required=True)

    #Page: Server Installation
    hostname = fields.Char(string="Hostname", required=True, 
    help="El Nombre para el Host NO debe iniciar con un Numero y su Longitud NO debe ser mayor a 14 caracteres.")
    
    #Server Resources
    server_ram = fields.Integer(string="RAM (GB)", required=True, help="La cantidad de memoria RAM solo debe contener como máximo 4 dígitos.")
    server_cpu = fields.Integer(string="CPU (Unidades)", required=True, help="La cantidad de unidades de CPU's solo debe contener como máximo 3 dígitos.")
    server_storage = fields.Integer(string="Almacenamiento (GB)", required=True, help="La cantidad de Almacenamiento Total Contratado solo debe contener como máximo 6 dígitos.")

    #Operating System
    operative_system = fields.Selection(
        [('windows', 'Windows'), ('linux', 'Linux')], string="Tipo SO", required=True)
    operating_system_arch = fields.Selection(
        [('32', '32 bits'), ('64', '64 bits')], string="Arquitectura del Sistema Operativo", required=True)
    lang_operating_system = fields.Selection(
        [('ingles', 'Ingles'), ('espanol', 'Español')], string="Idioma", required=True)
    server_on_internet = fields.Boolean(
        string="¿El servidor publicará hacía internet?", required=True)
    server_function = fields.Char(string="Función del servidor", required=True)
    server_impact = fields.Selection(
        [('alto', 'Alto'), ('medio', 'Medio'), ('bajo', 'Bajo')], string="Impacto", required=True)
    mission_critical = fields.Selection([('servicio_critico', 'Servicio Critico'), ('servicio_no_critico', 'Servicio No Critico'), (
        'sede_principal', 'Sede Principal'), ('sede_alterna', 'Sede Alterna'), ('sede_principal_alterna', 'Sede Principal / Alterno')], string="Misión Crítica", required=True)
    server_role = fields.Selection([('desarrollo', 'Desarrollo'), ('calidad','Calidad'), ('produccion', 'Producción')], string="Rol", required=True)
    service_classification = fields.Selection([('no_aplica', 'No Aplica'), (
        'estandar', 'Estándar'), ('soluciones', 'Soluciones')], string="Clasificación del Servicio", required=True)
    req_internet_access = fields.Boolean(
        string="¿Requiere acceso a internet (S/N)?", required=True)
    additional_conf = fields.Char(string="Configuraciones Adicionales")
    num_inc_out_ports = fields.Integer(
        string="Números de puertos entrantes y salientes")
    add_requirement = fields.Char(string="Algún requerimiento adicional")
    description_monitoring_system = fields.Char(
        string="Descripción en el sistema de monitoreo", required=True)
    virtual_platform = fields.Selection([('sos', 'SOS'), ('daycohost', 'Daycohost'), (
        'slas_consulting', 'SLAS Consulting')], string="Plataforma Virtual donde se alojara el servidor", required=True)
    
    # Disk Characteristics
    size_operating_system_level = fields.Integer(
        string="Tamaño a nivel de sistema operativo (GB)", required=True, help="El tamaño a nivel de Sistema Operativo debe contener como máximo 6 dígitos.")
    size_hypervisor_level = fields.Integer(
        string="Tamaño a nivel de hypervisor (GB)", required=True, help="El tamaño a nivel de Hypervisor debe contener como máximo 6 dígitos.")
    disk_type = fields.Char(string="Tipo de Disco", required=True)
    virtual_disk_extension = fields.Integer(string="Extension del disco virtual (GB)", required=True, help="El tamaño de la Extension del Disco Virtual debe contener como máximo 6 dígitos.")

    # Installation Features
    partitions_name_size = fields.Char(string="Particiones: Nombre / Tamaño", required=True)

    #--- Page: Clone Server ---
    
    clo_hostname = fields.Char(string="Hostname", required=True, 
    help="El Nombre para el Host NO debe iniciar con un Numero y su Longitud NO debe ser mayor a 14 caracteres.")
    
    #Server Resources
    clo_server_ram = fields.Integer(string="RAM (GB)", required=True, help="La cantidad de memoria RAM solo debe contener como máximo 4 dígitos.")
    clo_server_cpu = fields.Integer(string="CPU (Unidades)", required=True, help="La cantidad de unidades de CPU's solo debe contener como máximo 3 dígitos.")
    clo_server_storage = fields.Integer(string="Almacenamiento (GB)", required=True, help="La cantidad de Almacenamiento Total Contratado solo debe contener como máximo 6 dígitos.")

    hypervisor_virtual_server_comes = fields.Selection([('hyperv','HyperV'),('vmware','VMWARE'),('xen','XEN')],required=True,string="Hypervisor donde proviene el servidor virtual")
    vm_version_in_vmware = fields.Selection([('version_vmware','VMWARE'),('windows','Windows')],required=True,string="Versión de la MV en VMWARE / Generación de la MV en HyperV")

    #Operating System
    clo_operative_system = fields.Selection(
        [('windows', 'Windows'), ('linux', 'Linux')], string="Tipo SO", required=True)
    clo_operating_system_arch = fields.Selection(
        [('32', '32 bits'), ('64', '64 bits')], string="Arquitectura del Sistema Operativo", required=True)
    clo_lang_operating_system = fields.Selection(
        [('ingles', 'Ingles'), ('espanol', 'Español')], string="Idioma", required=True)
    clo_server_on_internet = fields.Boolean(
        string="¿El servidor publicará hacía internet?", required=True)
    clo_server_function = fields.Char(string="Función del servidor", required=True)
    clo_server_impact = fields.Selection(
        [('alto', 'Alto'), ('medio', 'Medio'), ('bajo', 'Bajo')], string="Impacto", required=True)
    clo_mission_critical = fields.Selection([('servicio_critico', 'Servicio Critico'), ('servicio_no_critico', 'Servicio No Critico'), (
        'sede_principal', 'Sede Principal'), ('sede_alterna', 'Sede Alterna'), ('sede_principal_alterna', 'Sede Principal / Alterno')], string="Misión Crítica", required=True)
    clo_server_role = fields.Selection([('desarrollo', 'Desarrollo'), ('calidad','Calidad'), ('produccion', 'Producción')], string="Rol", required=True)
    clo_service_classification = fields.Selection([('no_aplica', 'No Aplica'), (
        'estandar', 'Estándar'), ('soluciones', 'Soluciones')], string="Clasificación del Servicio", required=True)
    clo_req_internet_access = fields.Boolean(
        string="¿Requiere acceso a internet (S/N)?", required=True)
    clo_additional_conf = fields.Char(string="Configuraciones Adicionales")
    clo_num_inc_out_ports = fields.Integer(
        string="Números de puertos entrantes y salientes")
    clo_add_requirement = fields.Char(string="Algún requerimiento adicional")
    clo_description_monitoring_system = fields.Char(
        string="Descripción en el sistema de monitoreo", required=True)
    clo_virtual_platform = fields.Selection([('sos', 'SOS'), ('daycohost', 'Daycohost'), (
        'slas_consulting', 'SLAS Consulting')], string="Plataforma Virtual donde se alojara el servidor", required=True)

    # Disk Characteristics
    clo_size_operating_system_level = fields.Integer(
        string="Tamaño a nivel de sistema operativo (GB)", required=True, help="El tamaño a nivel de Sistema Operativo debe contener como máximo 6 dígitos.")
    clo_size_hypervisor_level = fields.Integer(
        string="Tamaño a nivel de hypervisor (GB)", required=True, help="El tamaño a nivel de Hypervisor debe contener como máximo 6 dígitos.")
    clo_disk_type = fields.Char(string="Tipo de Disco", required=True)
    clo_virtual_disk_extension = fields.Integer(string="Extension del disco virtual (GB)", required=True, help="El tamaño de la Extension del Disco Virtual debe contener como máximo 6 dígitos.")

    # Installation Features
    clo_partitions_name_size = fields.Char(string="Particiones: Nombre / Tamaño", required=True)
    
    #--- Page: Expansion decrease of processing storage capacities ---
    amp_hostname = fields.Char(string="Hostname", required=True, 
    help="Indica el nombre del servidor a ajustar las capacidades.")

    #Server Resources
    amp_server_ram = fields.Integer(string="RAM", help="Indica a cuantos GB RAM se va incrementar o disminuir.")
    amp_server_cpu = fields.Integer(string="CPU", help="Indica a cuantos VCORE se va incrementar o disminuir.")
    amp_server_storage = fields.Integer(string="Almacenamiento Total Contratado", help="Indica a cuantos GB de almacenamiento se va incrementar o disminuir. Indica la partición, disco o punto de montura.")

    amp_ip_addres = fields.Char(string="Dirección IP", required=True)
    
    #--- Page: Links ---
    link_location = fields.Selection([('ctdc','CTDC'),('ctdv','CTDV')],string="Ubicación")
    link_destination = fields.Selection([('enlace_colocado','Colocado'),('nube_dayco','Nube Dayco'),('enlace_internet','Internet')],string="Destino")
    link_dayco_cloud = fields.Selection([('infra_dayco','Infraestructura Dayco'),('infra_aliado','Infraestructura Aliado'),('no_aplica','N/A')],string="Nube Dayco")
    link_dci = fields.Boolean(string="DCI")
    link_bandwidth = fields.Char(string="Ancho de Banda")
    
    #Validations
    @api.onchange('hostname','clo_hostname','amp_hostname')
    @api.constrains('hostname','clo_hostname','amp_hostname')
    def check_hostname(self):
        """" Check that for the hostname field, 
        the length of the text is no longer than 14, 
        that it is alphanumeric and does not begin with a number. """

        error = False
        for record in self:
            if (record.hostname and not len(record.hostname) <= 14) or (record.clo_hostname and not len(record.clo_hostname) <= 14) or (record.amp_hostname and not len(record.amp_hostname) <= 14):
                error = True
                error_message = "La longtud no debe ser mayor a 14 caracteres."
            elif (record.hostname and record.hostname[0].isdecimal()) or (record.clo_hostname and record.clo_hostname[0].isdecimal()) or (record.amp_hostname and record.amp_hostname[0].isdecimal()):
                error = True
                error_message = "El nombre no debe iniciar con un número."
            ''' elif not record.hostname.isprintable() or not record.clo_hostname.isprintable():
                error = True
                error_message = "El texto ingresado solo debe contener letras y números." '''
            if error:
                raise exceptions.ValidationError('Hostname. ' + error_message)

    @api.onchange('server_ram','server_cpu', 'server_storage','clo_server_ram','clo_server_cpu', 'clo_server_storage','amp_server_ram','amp_server_cpu', 'amp_server_storage')
    @api.constrains('server_ram','server_cpu', 'server_storage','clo_server_ram','clo_server_cpu', 'clo_server_storage','amp_server_ram','amp_server_cpu', 'amp_server_storage')
    def check_server_resources(self):
        """ Check that for the group of fields under Server Resources: 
        the number of digits for ram, cpu and storage are not greater than: 4,3 y 6 """
        
        error = False
        # cast_ram = self.server_ram
        # cast_cpu = self.server_cpu
        # cast_alm = self.server_storage
        for record in self:    
            if (record.server_ram and not len(str(record.server_ram)) <= 4) or (record.clo_server_ram and not len(str(record.clo_server_ram)) <= 4) or (record.amp_server_ram and not len(str(record.amp_server_ram)) <= 4):
                error = True
                error_message = "La cantidad de memoria RAM solo debe contener como máximo 4 dígitos."
            elif (record.server_cpu and not len(str(record.server_cpu)) <= 3) or (record.clo_server_cpu and not len(str(record.clo_server_cpu)) <= 3) or (record.amp_server_cpu and not len(str(record.amp_server_cpu)) <= 3):
                error = True
                error_message = "La cantidad de unidades de CPU's solo debe contener como máximo 3 dígitos."
            elif (record.server_storage and not len(str(record.server_storage)) <= 6) or (record.clo_server_storage and not len(str(record.clo_server_storage)) <= 6) or (record.amp_server_storage and not len(str(record.amp_server_storage)) <= 6):
                error = True
                error_message = "La cantidad de Almacenamiento Total Contratado solo debe contener como máximo 6 dígitos."
            if error:
                raise exceptions.ValidationError('Recursos del Servidor. ' + error_message)

    @api.onchange('size_operating_system_level','size_hypervisor_level','disk_type','virtual_disk_extension','clo_size_operating_system_level','clo_size_hypervisor_level','clo_disk_type','clo_virtual_disk_extension')
    @api.constrains('size_operating_system_level','size_hypervisor_level','disk_type','virtual_disk_extension','clo_size_operating_system_level','clo_size_hypervisor_level','clo_disk_type','clo_virtual_disk_extension')
    def check_disk_characteristics(self):
        """ Check for the group of fields under Disk Characteristics that: 
        The number of digits is not greater than 6 
        and that the text entered is alphanumeric """

        error = False
        # cast_tam_so = self.size_operating_system_level
        # cast_tam_hyp = self.size_hypervisor_level
        # cast_ext_disco = self.virtual_disk_extension
        for record in self:
            if (record.size_operating_system_level and not len(str(record.size_operating_system_level)) <= 6) or (record.clo_size_operating_system_level and not len(str(record.clo_size_operating_system_level)) <= 6):
                error = True
                error_message = "El tamaño a nivel de Sistema Operativo debe contener como máximo 6 dígitos."
            elif (record.size_hypervisor_level and not len(str(record.size_hypervisor_level)) <= 6) or (record.clo_size_hypervisor_level and not len(str(record.clo_size_hypervisor_level)) <= 6):
                error = True
                error_message = "El tamaño a nivel de Hypervisor debe contener como máximo 6 dígitos."
            elif (record.virtual_disk_extension and not len(str(record.virtual_disk_extension)) <= 6) or (record.clo_virtual_disk_extension and not len(str(record.clo_virtual_disk_extension)) <= 6):
                error = True
                error_message = "El tamaño de la Extension del Disco Virtual debe contener como máximo 6 dígitos."
            ''' elif record.disk_type and not record.disk_type.isprintable():
                error = True
                error_message = "Tipo de Disco. El texto ingresado solo debe contener letras y números." '''
            if error:
                raise exceptions.ValidationError('Caracteristicas del Disco. ' + error_message)

    @api.onchange('server_function','clo_server_function')
    @api.constrains('server_function','clo_server_function')
    def check_server_function(self):
        """ Valida que el campo funcion del servidor: 
        de que el texto no inicie con un número """
        
        error = False
        # if not len(self.server_function) <= 14:
        #     error = True
        #     error_message = "La longitud no debe ser mayor a 14 caracteres."
        # if not self.server_function.isprintable():
        #     error = True
        #     error_message = "El texto ingresado solo debe contener letras y números."
        for record in self:  
            if (record.server_function and record.server_function[0].isdecimal()) or (record.clo_server_function and record.clo_server_function[0].isdecimal()):
                error = True
                error_message = "El texto ingresado no debe iniciar con un número."
            if error:
                raise exceptions.ValidationError('Función del Servidor. ' + error_message)

    @api.onchange('additional_conf','add_requirement','partitions_name_size','clo_additional_conf','clo_add_requirement','clo_partitions_name_size')
    @api.constrains('additional_conf','add_requirement','partitions_name_size','clo_additional_conf','clo_add_requirement','clo_partitions_name_size')
    def check_add(self):
        """ Check that the fields: additional config,
        additional requirement and Partitions: Name / Size are alphanumeric. """
        
        error =  False
        for record in self:
            if (record.additional_conf and  not record.additional_conf.isprintable()) or (record.clo_additional_conf and  not record.clo_additional_conf.isprintable()):
                error = True
                error_message = "Configuraciones Adicionales."
            elif (record.add_requirement and not record.add_requirement.isprintable()) or (record.clo_add_requirement and not record.clo_add_requirement.isprintable()):
                error = True
                error_message = "Requerimiento Adicional."
            elif (record.partitions_name_size and not record.partitions_name_size.isprintable()) or (record.clo_partitions_name_size and not record.clo_partitions_name_size.isprintable()):
                error = True
                error_message = "Caracteristicas de la Instalación."
            if error:
                raise exceptions.ValidationError(error_message + ' El texto ingresado solo debe contener letras y números.')
    
    @api.onchange('amp_ip_addres')
    @api.constrains('amp_ip_addres')
    def check_ip(self):
        
        error = False
        for record in self:
            if record.amp_ip_addres and not len(record.amp_ip_addres) <= 15:
                error = True
                error_message = "La longtud no debe ser mayor a 15 caracteres."
            if error:
                raise exceptions.ValidationError('Dirección IP. ' + error_message)
    
    @api.onchange('link_bandwidth')
    @api.constrains('link_bandwidth')
    def check_link_bandwidth(self):
        
        error = False
        for record in self:
            if record.link_bandwidth and not len(record.link_bandwidth) <= 12:
                error = True
                error_message = "La longtud no debe ser mayor a 12 caracteres."
            if error:
                raise exceptions.ValidationError('Ancho de Banda. ' + error_message)
