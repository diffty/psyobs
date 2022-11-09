from __future__ import annotations

from typing import List

import obspython as obsapi

import obs
from obs.enums import ESceneDuplicationType


class Scene:
    def __init__(self, scn_api_obj):
        self._scn_api_obj = scn_api_obj
        self._src_api_obj = self.source.api_obj
    
    def duplicate(self, new_name: str, duplicate_type: ESceneDuplicationType = ESceneDuplicationType.OBS_SCENE_DUP_REFS) -> Scene:
        new_scn = obsapi.obs_scene_duplicate(self._scn_api_obj, new_name, duplicate_type)
        return Scene(new_scn)

    @property
    def name(self) -> str:
        return obsapi.obs_source_get_name(self._src_api_obj)
    
    @name.setter
    def name(self, new_name: str):
        obsapi.obs_source_set_name(self._src_api_obj, new_name)
    
    @property
    def sceneitems(self):
        sceneitems_api_list = obsapi.obs_scene_enum_items(self.api_obj)
        return [obs.SceneItem(sceneitem_api) for sceneitem_api in sceneitems_api_list]
    
    @property
    def api_obj(self):
        return self._scn_api_obj
    
    @property
    def source(self) -> obs.Source:
        scn_src = obsapi.obs_scene_get_source(self._scn_api_obj)
        return obs.Source(scn_src)

    def add(self, src: obs.Source):
        obsapi.obs_scene_add(self._scn_api_obj, src.api_obj)
    
    def find_source_by_name(self, src_name: str, recursive: bool = False):
        if recursive:
            api_src = obsapi.obs_scene_find_source_recursive(self._scn_api_obj, src_name)
        else:
            api_src = obsapi.obs_scene_find_source(self._scn_api_obj, src_name)

        if not api_src:
            raise Exception(
                f"Can't find source named {src_name}!")

        return obs.Source(api_src)

    def find_sceneitem_from_source(self, src: obs.Source) -> obs.SceneItem:
        api_scnitem = obsapi.obs_scene_sceneitem_from_source(self._scn_api_obj, src.api_obj)
        if not api_scnitem:
            raise Exception(
                f"Can't find a scene item using source {src} in scene {self.name}!")
        
        return obs.SceneItem(api_scnitem)

    def get_sceneitem_by_num(self, num: int) -> obs.SceneItem:
        scene_item_list = list(obsapi.obs_scene_enum_items(self.api_obj))

        if (num < 0 or num >= len(scene_item_list)):
            raise Exception(
                f"Scene item number {num} in scene {self.name} out of bounds!")

        return obs.SceneItem(scene_item_list[num])

    @staticmethod
    def find_by_name(self, scn_name):
        api_scn = obsapi.obs_get_scene_by_name(scn_name)
        if not api_scn:
            raise Exception(
                f"Can't find scene named {scn_name}!")

        return Scene(api_scn)
    
    @staticmethod
    def active() -> obs.Scene:
        api_scn_src = obsapi.obs_frontend_get_current_scene()
        api_scn = obsapi.obs_scene_from_source(api_scn_src)
        return Scene(api_scn)

    @staticmethod
    def create(add_to_curr_collection=True)-> obs.Scene:
        api_scn = obsapi.obs_scene_create()
        if add_to_curr_collection:
            obsapi.obs_scene_add(api_scn)
        return Scene(api_scn)
    
    @staticmethod
    def create_from_scene_source(api_scn_src)-> obs.Scene:
        api_scn = obsapi.obs_scene_from_source(api_scn_src)
        return Scene(api_scn)
    
    @staticmethod
    def all_scenes() -> List[obs.Scene]:
        return [Scene.create_from_scene_source(api_scn_src)
                    for api_scn_src in obsapi.obs_frontend_get_scenes()]
