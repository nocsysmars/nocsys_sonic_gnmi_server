#
# util_lldp.py
#
# APIs for processing lldp info.
#

import subprocess
import json
import pdb

# input : '7 days, 22:55:53' / '0 day, 00:00:11'
# ret   : xxx
def lldp_cnv_age_to_secs(age_str):
    days = age_str.split(',')
    days_secs = 0
    if len (days) > 1:
        hours = days[1]
        days = days[0].split(' ')
        days_secs = int(days[0]) * 24 * 60 * 60
    else:
        hours = days[0]

    hours = hours.split(":")
    hours_secs = 0
    for k in hours:
        hours_secs = hours_secs * 60 + int(k)

    return (days_secs + hours_secs)

# for set lldp chassis/port
def lldp_set_id_field(obj, fld_str, fld_dict):
    attr_key_type = "_set_%s_id_type" % fld_str
    attr_key_id   = "_set_%s_id" % fld_str

    # refer to _set_xxx_id_type in lldp_binding
    if "id" in fld_dict[fld_str]:
        id_dict = fld_dict[fld_str]["id"]
    else:
        for k, v in fld_dict[fld_str].items():
            id_dict = fld_dict[fld_str][k]["id"]
            if fld_str == "chassis":
                obj._set_system_name(k)
                obj._set_system_description(fld_dict[fld_str][k]["descr"])

    # TODO: type mapping
    #  CHASSIS_COMPONENT/INTERFACE_ALIAS/PORT_COMPONENT/MAC_ADDRESS
    #  NETWORK_ADDRESS/INTERFACE_NAME/LOCAL
    if id_dict["type"] == "mac":
        type_value = "MAC_ADDRESS"

        set_type_fun = getattr(obj, attr_key_type)
        if set_type_fun:
            set_type_fun(type_value)

    set_id_fun = getattr(obj, attr_key_id)
    if set_id_fun:
        set_id_fun(id_dict["value"])

# fill lldp info for one interface
# input : inf - "eth0"
#         val - {"age": ..., "chassis": ... }
def lldp_get_info_interface(lldp_yph, inf, val):
    infs = lldp_yph.get("/interfaces")[0]
    # bcz /lldp/interfaces/interface ref to oc-if:base-interface-ref
    # need to create oc-if's interface for lldp's operation
    if inf not in infs.interface:
        infs.interface.add(inf)

    lldp_infs = lldp_yph.get("/lldp")[0].interfaces
    if inf not in lldp_infs.interface:
        lldp_inf = lldp_infs.interface.add(inf)
    else:
        lldp_inf = lldp_infs.interface[inf]

    # val key: ppvid, via, age, vlan, chassis, rid, pi, port
    #pdb.set_trace()

    nbr = lldp_inf.neighbors.neighbor.add(val["rid"])
    nbr.state._set_age(lldp_cnv_age_to_secs(val["age"]))
    lldp_set_id_field(nbr.state, "chassis", val)
    lldp_set_id_field(nbr.state, "port", val)

def lldp_del_all_inf_neighbors(lldp_yph, inf):
    lldp_infs = lldp_yph.get("/lldp")[0].interfaces
    if inf in lldp_infs.interface:
        lldp_inf = lldp_infs.interface[inf]
        lldp_inf._unset_neighbors()

# fill DUT's current lldp info into lldp_yph
# key_ar [0] : interface name e.g. "eth0"
# ret        : True/False
def lldp_get_info(lldp_yph, key_ar):
    """
    use 'lldpctl -f xml' command to gather local lldp detailed information
    """
    lldp_cmd = 'lldpctl -f json'
    ret_val = False

    #pdb.set_trace()
    p = subprocess.Popen(lldp_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    ## Wait for end of command. Get return code ##
    returncode = p.wait()

    lldp_root = lldp_yph.get("/lldp")[0]
    if returncode == 0:
        lldp_root.config.enabled = True
        lldp_root.config.enabled._mchanged = True

        lldp_info = json.loads(output)

        if "interface" in lldp_info["lldp"]:
            if isinstance(lldp_info["lldp"]["interface"], list):
                for k in lldp_info["lldp"]["interface"]:
                    for inf, val in k.items():
                        if key_ar and inf != key_ar[0]:
                            continue
                        lldp_del_all_inf_neighbors(lldp_yph, inf)
                        # TODO: more than one neighbor ???
                        lldp_get_info_interface(lldp_yph, inf, val)

            if isinstance(lldp_info["lldp"]["interface"], dict):
                for inf, val in lldp_info["lldp"]["interface"].items():
                    if key_ar and inf != key_ar[0]:
                        continue
                    lldp_del_all_inf_neighbors(lldp_yph, inf)
                    lldp_get_info_interface(lldp_yph, inf, val)

        ret_val = True
    else:
        if 'Error response from daemon' in err:
            lldp_root.config.enabled = False
            lldp_root._unset_interfaces()
            ret_val = True

    return ret_val

