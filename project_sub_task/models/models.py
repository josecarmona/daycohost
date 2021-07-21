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
        ('pase_produccion', 'Pase a Producción')], string="Tipo de Servicio")
    percentage_progress = fields.Float((5,2),required=True)
    weighting_factor = fields.Float(string="FP", required=True , help="Factor de Ponderación")
    
    
    #PAGE: Server Installation
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

    #--- PAGE: Clone Server ---
    
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
    
    #--- PAGE: Expansion decrease of processing storage capacities ---
    amp_hostname = fields.Char(string="Hostname", required=True, 
    help="Indica el nombre del servidor a ajustar las capacidades.")

    #Server Resources
    amp_server_ram = fields.Integer(string="RAM", help="Indica a cuantos GB RAM se va incrementar o disminuir.")
    amp_server_cpu = fields.Integer(string="CPU", help="Indica a cuantos VCORE se va incrementar o disminuir.")
    amp_server_storage = fields.Integer(string="Almacenamiento Total Contratado", help="Indica a cuantos GB de almacenamiento se va incrementar o disminuir. Indica la partición, disco o punto de montura.")

    amp_ip_addres = fields.Char(string="Dirección IP", required=True)
    
    #--- PAGE: Links ---
    link_location = fields.Selection([('ctdc','CTDC'),('ctdv','CTDV')],string="Ubicación")
    link_destination = fields.Selection([('enlace_colocado','Colocado'),('nube_dayco','Nube Dayco'),('enlace_internet','Internet')],string="Destino")
    link_dayco_cloud = fields.Selection([('infra_dayco','Infraestructura Dayco'),('infra_aliado','Infraestructura Aliado'),('no_aplica','N/A')],string="Nube Dayco")
    link_dci = fields.Boolean(string="DCI")
    link_bandwidth = fields.Char(string="Ancho de Banda DCI")
    
    #--- PAGE: Internet Service ---
    internet_location = fields.Selection([('ctdc','CTDC'),('ctdv','CTDV')],string="Ubicación")
    internet_destination = fields.Selection([('internet_colocado','Colocado'),('internet_nube_dayco','Nube Dayco'),('internet_enlace','Enlace'),('internet_todas','Todas')],string="Destino")
    internet_security = fields.Boolean(string="Seguridad")
    internet_public_addresses = fields.Char(string="Direcciones Publicas") 
    internet_dayco_cloud = fields.Selection([('internet_infra_dayco','Infraestructura Dayco'),('internet_infra_aliado','Infraestructura Aliado')],string="Nube Dayco")
    internet_bandwidth = fields.Char(string="Ancho de Banda")

    #--- PAGE: Security Service ---
    secu_serv_security_level = fields.Selection([('seguridad_avanzado','Seguridad Avanzado'),('seguridad_basico','Seguridad Básico'),('seguridad_dedicada','Seguridad Dedicada'),],string="Nivel de Seguridad")

    #VPN
    secu_serv_vpn_required = fields.Boolean(string="Requiere VPN")
    secu_serv_vpn_type = fields.Selection([('ssl','SSL'),('site_to_site','Site-to-Site')],string="Tipo de VPN")
    secu_serv_schedule_annex = fields.Char(string="Anexo de Planilla site-to-site")
    
    #Dayco Server
    secu_serv_number_servers = fields.Integer(string="Cantidad de Servidores")
    secu_serv_public_servers = fields.Char(string="Servidores Públicos")
    secu_serv_ports = fields.Integer(string="Puertos")

    #Placement
    secu_serv_placement_number_servers = fields.Integer(string="Cantidad de Servidores")
    secu_serv_placement_public_servers = fields.Char(string="Servidores Públicos")
    secu_serv_outgoing_traffic_ports = fields.Char(string="Puertos Tráfico de Salida")
    secu_serv_placement_ports = fields.Char(string="Puertos")

    #Add Service
    secu_serv_ips = fields.Char(string="IPS")
    secu_serv_ids = fields.Char(string="IDS")
    secu_serv_web_filtering = fields.Boolean(string="Web Filtering")
    secu_serv_waf = fields.Boolean(string="WAF")
    secu_serv_app_control = fields.Boolean(string="Application Control")
    secu_serv_ldap = fields.Boolean(string="LDAP")
    secu_serv_fsso = fields.Boolean(string="FSSO")

    #Balancer
    secu_serv_dir_ip_1 = fields.Char(string="Dirección IP (1)")
    secu_serv_dir_ip_2 = fields.Char(string="Dirección IP (2)")
    secu_serv_dir_ip_3 = fields.Char(string="Dirección IP (3)")
    secu_serv_balancer_ports = fields.Integer(string="Puertos")

    #--- PAGE: Placement ---
    
    # Placement request
    place_m2c_cage = fields.Float(string="m2 (jaula)")
    place_one_rack = fields.Char(string="1 Rack")
    place_one_three_rack = fields.Char(string="1/3 Rack")
    place_telecom_tower = fields.Float(string="Espacio en Torre Telecom")

    # Equipment listings
    place_item = fields.Char(string="Item")
    place_equipment_description = fields.Char(string="Descripción del equipo")    
    place_equipment_brand = fields.Char(string="Marca")
    place_equipment_model = fields.Char(string="Modelo")
    place_equipment_serial = fields.Char(string="Serial")
    palce_type = fields.Selection([('place_servidor', 'Servidor'),('palce_telecom', 'Telecom')],string="Tipo")
    palce_request = fields.Char(string="Solicitud")
    palce_delivery = fields.Char(string="Entrega")
    palce_dimensions = fields.Char(string="Dimensiones (U de rack)")
    palce_nominal_load = fields.Char(string="Carga Nominal (KVA)")
    palce_tension_level = fields.Char(string="Nivel de Tensión (V)")
    place_current = fields.Char(string="Corriente (A)")
    place_number_power_sources = fields.Integer(string="Cantidad de Fuentes de Poder")
    place_btu = fields.Char(string="BTU")
    place_remarks = fields.Char(string="Observaciones")
    
    #--- PAGE: Cabling UTP ---

    utp_location = fields.Selection([('utp_valencia', 'Valencia'),('utp_caracas', 'Caracas')], string="Localidad en la que se requiere")
    utp_date = fields.Date(string="Fecha requerida")

    utp_service_type = fields.Selection([('utp_intra_connect', 'Intra-Connect'),('utp_cross_conect', 'Cross-Conect'),('utp_interconexion', 'Interconexión'),('utp_dci', 'DCI')], string="Tipo de Servicio")
    utp_origin_rack = fields.Char(string="Rack de Origen")
    utp_destination_rack = fields.Char(string="Rack de Destino")
    utp_category = fields.Selection([('utp_cat5e', 'CAT 5e (Telefonia)'),('utp_cat6', 'CAT 6'),('utp_cat6a', 'CAT 6A')], string="Categoría")
    utp_quantity = fields.Integer(string="Cantidad")
    utp_completed = fields.Boolean(string="Completado")
    utp_observations = fields.Char(string="Observaciones")

    #--- PAGE: Cabling FO ---
    fo_location = fields.Selection([('fo_valencia', 'Valencia'),('fo_caracas', 'Caracas')], string="Localidad en la que se requiere")
    fo_date = fields.Date(string="Fecha requerida")

    fo_service_type = fields.Selection([('fo_intra_connect', 'Intra-Connect'),('fo_cross_conect', 'Cross-Conect'),('fo_interconexion', 'Interconexión'),('fo_dci', 'DCI')], string="Tipo de Servicio")
    fo_fiber_mode = fields.Selection([('fo_monomodo_om1', 'Monomodo OM1'),('fo_monomodo_om2', 'Monomodo OM2'),('fo_monomodo_om3', 'Monomodo OM3'),('fo_monomodo_om4', 'Monomodo OM4'),('fo_multimodo', 'Multimodo (OS1 / OS2)')], string="Modo de Fibra")
    fo_fiber_type = fields.Selection([('fo_simplex', 'Simplex'),('fo_duplex', 'Duplex')],string="Tipo de Fibra")
    
    fo_origin_rack = fields.Char(string="Rack de Origen")
    fo_origin_connector = fields.Selection([('fo_orig_st', 'ST'),('fo_orig_lc', 'LC'),('fo_orig_sc', 'SC'),('fo_orig_mpt_mpo', 'MPT/MPO')],string="Conector Origen")
    
    fo_destination_rack = fields.Char(string="Rack de Destino")
    fo_destination_connector = fields.Selection([('fo_dest_st', 'ST'),('fo_dest_lc', 'LC'),('fo_dest_sc', 'SC'),('fo_dest_mpt_mpo', 'MPT/MPO')],string="Conector Destino")

    
    fo_quantity = fields.Integer(string="Cantidad")
    fo_completed = fields.Boolean(string="Completado")
    fo_observations = fields.Char(string="Observaciones")

    #--- PAGE: Coaxial Cabling ---
    co_location = fields.Selection([('co_valencia', 'Valencia'),('co_caracas', 'Caracas')], string="Localidad en la que se requiere")
    co_date = fields.Date(string="Fecha requerida")

    co_service_type = fields.Selection([('co_intra_connect', 'Intra-Connect'),('co_cross_conect', 'Cross-Conect'),('co_interconexion', 'Interconexión'),('co_dci', 'DCI')], string="Tipo de Servicio")
    co_origin_rack = fields.Char(string="Rack de Origen")
    co_destination_rack = fields.Char(string="Rack de Destino")
    co_driver = fields.Selection([('co_coaxial', 'Coaxial'),('co_minicoaxial', 'Minicoaxial')], string="Conductor")
    co_type = fields.Selection([('co_r559', 'R559'),('co_rg11', 'RG11')],string="Tipo")
    co_quantity = fields.Integer(string="Cantidad")
    co_completed = fields.Boolean(string="Completado")
    co_observations = fields.Char(string="Observaciones")


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
    
    @api.onchange('link_bandwidth','internet_bandwidth')
    @api.constrains('link_bandwidth','internet_bandwidth')
    def check_link_bandwidth(self):
        
        error = False
        for record in self:
            if (record.link_bandwidth and not len(record.link_bandwidth) <= 12) or (record.internet_bandwidth and not len(record.internet_bandwidth) <= 12):
                error = True
                error_message = "La longtud no debe ser mayor a 12 caracteres."
            if error:
                raise exceptions.ValidationError('Ancho de Banda. ' + error_message)

    @api.onchange('percentage_progress','weighting_factor')
    @api.constrains('percentage_progress','weighting_factor')
    def check_progress(self):
        error = False
        for record in self:
            if not (record.percentage_progress >= 0 and record.percentage_progress <= 100):
                error = True
                error_message = "Porcentaje"
            elif not (record.weighting_factor >= 0 and record.weighting_factor <= 100):
                error = True
                error_message = "Factor de Ponderación"
            if error:
                raise exceptions.ValidationError('El valor del ' + error_message + ' debe estar entre [0, 100]')
