#!/usr/bin/env python3
class FilterModule(object):
    """ Ansible custom filter collection """

    def filters(self):
        return {
            'extract_obj_names': self.extract_obj_names,
        }

    def extract_obj_names(self, objects_list):
        """
        Convert objects list to dictionary:
        
        {obj_uid: obj_name, obj_uid: obj_name, ...}
        """
        uid_dict = {}
        for chkpt_obj in objects_list:
            uid = chkpt_obj['uid']
            name = chkpt_obj['name']
            uid_dict[uid] = name
        return uid_dict
