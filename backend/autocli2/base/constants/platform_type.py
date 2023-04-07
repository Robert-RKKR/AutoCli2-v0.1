# AutoCli2 - base integer model import:
from autocli2.base.constants.base.base_choices import BaseTextChoices

# Django - translation model import:
from django.utils.translation import gettext_lazy as _


# Choices class:
class PlatformTypeChoices(BaseTextChoices):

    # Choices values:
    GENERIC = 'generic', 'Generic Device'
    CISCO_ASA = 'cisco_asa', 'Cisco ASA'
    CISCO_IOS = 'cisco_ios', 'Cisco IOS'
    CISCO_XE = 'cisco_xe', 'Cisco IOS XE'
    CISCO_NXOS = 'cisco_nxos', 'Cisco NXOS'
    CISCO_XR = 'cisco_xr', 'Cisco IOS XR'
    CISCO_SDWAN = 'cisco_viptela', 'Cisco SD-WAN',
    CISCO_WLC = 'cisco_wlc', 'Cisco WLC'
    CISCO_WLC_85 = 'cisco_wlc_85', 'Cisco WLC 85'
    ALCATEL_AOS = 'alcatel_aos', 'Alcatel AOS'
    ALCATEL_SROS = 'alcatel_sros', 'Alcatel SROS'
    APRESIA_AEOS = 'apresia_aeos', 'Apresia AEOS'
    ARISTA_EOS = 'arista_eos', 'Arista EOS'
    CIENA_SAOS = 'ciena_saos', 'Ciena SAOS'
    DELL_FORCE10 = 'dell_force10', 'Dell Force10'
    DELL_OS9 = 'dell_os9', 'Dell OS9'
    DELL_OS10 = 'dell_os10', 'Dell OS10'
    DELL_POWERCONNECT = 'dell_powerconnect', 'Dell Powerconnect'
    F5_TMSH = 'f5_tmsh', 'F5 Tmsh'
    F5_LINUX = 'f5_linux', 'F5 Linux'
    HP_COMWARE = 'hp_comware', 'Hp Comware'
    HUAWEI = 'huawei', 'Huawei'
    JUNIPER_JUNOS = 'juniper_junos', 'Juniper Junos'
    LINUX = 'linux', 'Linux'
    ERICSSON_IPOS = 'ericsson_ipos', 'Ericsson IPOS'
    EXTREME_EXOS = 'extreme_exos', 'Extreme EXOS'
    EXTREME_NETIRON = 'extreme_netiron', 'Extreme Netiron'
    EXTREME_SLX = 'extreme_slx', 'Extreme SLX'
    EXTREME_TIERRA = 'extreme_tierra', 'Extreme Tierra'
    MIKROTIK_ROUTER = 'mikrotik_routeros', 'MikroTik Router OS'
    MIKROTIK_SWITCH = 'mikrotik_switchos', 'MikroTik Switch OS'
    UBIQUITI_EDGESWITCH = 'ubiquiti_edgeswitch', 'Ubiquiti Edgeswitch'
    UBIQUITI_EDGE = 'ubiquiti_edge', 'Ubiquiti Edge'
    UBIQUITI_EDGEROUTER = 'ubiquiti_edgerouter', 'Ubiquiti Edge Router'
    MELLANOX_MLNXOS = 'mellanox_mlnxos', 'Mellanox Mlnxos'
    YAMAHA = 'yamaha', 'Yamaha'
    FORTINET = 'fortinet', 'Fortinet'
    PALOALTO_PANOS = 'paloalto_panos', 'Paloalto Panos'
    SUPERMICRO_SMIS = 'supermicro_smis', 'Supermicro Smis'
    FLEXVNF = 'flexvnf', 'Flexvnf'

    @classmethod
    def get_sections(cls):
        sections = {
            'All': [
                cls.GENERIC,
                cls.CISCO_ASA,
                cls.CISCO_IOS,
                cls.CISCO_XE,
                cls.CISCO_NXOS,
                cls.CISCO_XR,
                cls.CISCO_SDWAN,
                cls.CISCO_WLC,
                cls.CISCO_WLC_85,
                cls.ALCATEL_AOS,
                cls.ALCATEL_SROS,
                cls.APRESIA_AEOS,
                cls.ARISTA_EOS,
                cls.CIENA_SAOS,
                cls.DELL_FORCE10,
                cls.DELL_OS9,
                cls.DELL_OS10,
                cls.DELL_POWERCONNECT,
                cls.F5_TMSH,
                cls.F5_LINUX,
                cls.HP_COMWARE,
                cls.HUAWEI,
                cls.JUNIPER_JUNOS,
                cls.LINUX,
                cls.ERICSSON_IPOS,
                cls.EXTREME_EXOS,
                cls.EXTREME_NETIRON,
                cls.EXTREME_SLX,
                cls.EXTREME_TIERRA,
                cls.MIKROTIK_ROUTER,
                cls.MIKROTIK_SWITCH,
                cls.UBIQUITI_EDGESWITCH,
                cls.UBIQUITI_EDGE,
                cls.UBIQUITI_EDGEROUTER,
                cls.MELLANOX_MLNXOS,
                cls.YAMAHA,
                cls.FORTINET,
                cls.PALOALTO_PANOS,
                cls.SUPERMICRO_SMIS,
                cls.FLEXVNF,
            ],
            'Uniwersal': [
                cls.GENERIC,
            ],
            'Cisco software': [
                cls.CISCO_ASA,
                cls.CISCO_IOS,
                cls.CISCO_XE,
                cls.CISCO_NXOS,
                cls.CISCO_SDWAN,
                cls.CISCO_XR,
                cls.CISCO_WLC,
                cls.CISCO_WLC_85,
            ],
            'FortiNet': [
                cls.FORTINET,
            ],
            'Extream': [
                cls.MIKROTIK_ROUTER,
                cls.MIKROTIK_SWITCH,
            ],
            'Dell': [
                cls.DELL_FORCE10,
                cls.DELL_OS9,
                cls.DELL_OS10,
                cls.DELL_POWERCONNECT,
            ],
            'MikroTik': [
                cls.EXTREME_EXOS,
                cls.EXTREME_NETIRON,
                cls.EXTREME_SLX,
                cls.EXTREME_TIERRA,
            ],
            'F5': [
                cls.F5_TMSH,
                cls.F5_LINUX,
            ],
        }
        return sections
