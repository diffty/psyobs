import obspython as obsapi

import obs


class Source:
    def __init__(self, src_api_obj):
        self._api_obj = src_api_obj
    
    @property
    def api_obj(self):
        return self._api_obj

    @property
    def name(self):
        return obsapi.obs_source_get_name(self._api_obj)
    
    @name.setter
    def name(self, new_name):
        obsapi.obs_source_set_name(self._api_obj, new_name)
    
    @staticmethod
    def create(name, src_type_name):
        api_src = obsapi.obs_source_create(src_type_name, name, None, None)
        return Source(api_src)
