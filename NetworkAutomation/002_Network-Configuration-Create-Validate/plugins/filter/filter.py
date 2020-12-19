"""
Author: Calvin Hua-Nguyen

File has custom filters for use in Ansible playbooks
"""


class FilterModule:
    """
    Defines a filter module object
    """

    @staticmethod
    def filters():
        """
        Returns dictionary of filter names and
        callables to expose filters to playbooks
        """
        return {
            "interface_vlan_diff": FilterModule.interface_vlan_diff,
        }

    @staticmethod
    def interface_vlan_diff(intended_vlans, running_vlans):
        """
        Returns passed in text in upper case format
        """
        vlans_dict = dict()

        intended_vlans_set = set(intended_vlans)
        running_vlans_set = set(running_vlans)

        vlans_dict.update(
            {"vlans_kept": list(intended_vlans_set.intersection(running_vlans_set))}
        )
        vlans_dict.update({"vlans_added": list(intended_vlans_set - running_vlans_set)})
        vlans_dict.update(
            {"vlans_removed": list(running_vlans_set - intended_vlans_set)}
        )

        return vlans_dict
