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
                DeviceTypeChoices.GENERIC,
                DeviceTypeChoices.CISCO_ASA,
                DeviceTypeChoices.CISCO_IOS,
                DeviceTypeChoices.CISCO_XE,
                DeviceTypeChoices.CISCO_NXOS,
                DeviceTypeChoices.CISCO_XR,
                DeviceTypeChoices.CISCO_SDWAN,
                DeviceTypeChoices.CISCO_WLC,
                DeviceTypeChoices.CISCO_WLC_85,
                DeviceTypeChoices.ALCATEL_AOS,
                DeviceTypeChoices.ALCATEL_SROS,
                DeviceTypeChoices.APRESIA_AEOS,
                DeviceTypeChoices.ARISTA_EOS,
                DeviceTypeChoices.CIENA_SAOS,
                DeviceTypeChoices.DELL_FORCE10,
                DeviceTypeChoices.DELL_OS9,
                DeviceTypeChoices.DELL_OS10,
                DeviceTypeChoices.DELL_POWERCONNECT,
                DeviceTypeChoices.F5_TMSH,
                DeviceTypeChoices.F5_LINUX,
                DeviceTypeChoices.HP_COMWARE,
                DeviceTypeChoices.HUAWEI,
                DeviceTypeChoices.JUNIPER_JUNOS,
                DeviceTypeChoices.LINUX,
                DeviceTypeChoices.ERICSSON_IPOS,
                DeviceTypeChoices.EXTREME_EXOS,
                DeviceTypeChoices.EXTREME_NETIRON,
                DeviceTypeChoices.EXTREME_SLX,
                DeviceTypeChoices.EXTREME_TIERRA,
                DeviceTypeChoices.MIKROTIK_ROUTER,
                DeviceTypeChoices.MIKROTIK_SWITCH,
                DeviceTypeChoices.UBIQUITI_EDGESWITCH,
                DeviceTypeChoices.UBIQUITI_EDGE,
                DeviceTypeChoices.UBIQUITI_EDGEROUTER,
                DeviceTypeChoices.MELLANOX_MLNXOS,
                DeviceTypeChoices.YAMAHA,
                DeviceTypeChoices.FORTINET,
                DeviceTypeChoices.PALOALTO_PANOS,
                DeviceTypeChoices.SUPERMICRO_SMIS,
                DeviceTypeChoices.FLEXVNF,
            ],
            'Uniwersal': [
                DeviceTypeChoices.GENERIC,
            ],
            'Cisco software': [
                DeviceTypeChoices.CISCO_ASA,
                DeviceTypeChoices.CISCO_IOS,
                DeviceTypeChoices.CISCO_XE,
                DeviceTypeChoices.CISCO_NXOS,
                DeviceTypeChoices.CISCO_SDWAN,
                DeviceTypeChoices.CISCO_XR,
                DeviceTypeChoices.CISCO_WLC,
                DeviceTypeChoices.CISCO_WLC_85,
            ],
            'FortiNet': [
                DeviceTypeChoices.FORTINET,
            ],
            'Extream': [
                DeviceTypeChoices.MIKROTIK_ROUTER,
                DeviceTypeChoices.MIKROTIK_SWITCH,
            ],
            'Dell': [
                DeviceTypeChoices.DELL_FORCE10,
                DeviceTypeChoices.DELL_OS9,
                DeviceTypeChoices.DELL_OS10,
                DeviceTypeChoices.DELL_POWERCONNECT,
            ],
            'MikroTik': [
                DeviceTypeChoices.EXTREME_EXOS,
                DeviceTypeChoices.EXTREME_NETIRON,
                DeviceTypeChoices.EXTREME_SLX,
                DeviceTypeChoices.EXTREME_TIERRA,
            ],
            'F5': [
                DeviceTypeChoices.F5_TMSH,
                DeviceTypeChoices.F5_LINUX,
            ],
        }
        return sections
