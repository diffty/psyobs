import obspython as obsapi

import obs

from typing import Tuple

from obs.enums import ETransformAlignment
from obs.enums import EOrderMovement
from obs.enums import EBoundsType
from obs.enums import ETransformAlignment


class SceneItem:
    def __init__(self, scnitem_api_obj):
        self._api_obj = scnitem_api_obj
    
    def __repr__(self):
        return f"<SceneItem {self.source.name} ({self.scene.name}#{self.order_idx})>"
    
    @property
    def api_obj(self):
        return self._api_obj
    
    @property
    def scene(self):
        api_scn = obsapi.obs_sceneitem_get_scene(self._api_obj)
        return obs.Scene(api_scn)
    
    @property
    def source(self):
        api_src = obsapi.obs_sceneitem_get_source(self._api_obj)
        return obs.Source(api_src)

    @property
    def visible(self):
        return obsapi.obs_sceneitem_visible()

    @visible.setter
    def visible(self, is_visible: bool):
        obsapi.obs_sceneitem_set_visible(is_visible)

    @property
    def locked(self):
        return obsapi.obs_sceneitem_locked()

    @locked.setter
    def locked(self, is_locked: bool):
        obsapi.obs_sceneitem_set_locked(is_locked)

    @property
    def position(self) -> tuple[float, float]:
        pos = obsapi.vec2()
        obsapi.obs_sceneitem_get_pos(self.api_obj, pos)
        return (pos.x, pos.y)

    @position.setter
    def position(self, new_pos: tuple[float, float]):
        pos = obsapi.vec2()
        pos.x = new_pos[0]
        pos.y = new_pos[1]
        obsapi.obs_sceneitem_set_pos(self._api_obj, pos)

    @property
    def rotation(self) -> float:
        return obsapi.obs_sceneitem_get_rot(self.api_obj)

    @rotation.setter
    def rotation(self, new_rotation: float):
        obsapi.obs_sceneitem_set_rot(self._api_obj, new_rotation)

    @property
    def scale(self) -> tuple[float, float]:
        pos = obsapi.vec2()
        obsapi.obs_sceneitem_get_pos(self.api_obj, pos)
        return (pos.x, pos.y)

    @scale.setter
    def scale(self, new_scale: tuple[float, float]):
        scale = obsapi.vec2()
        scale.x = new_scale[0]
        scale.y = new_scale[1]
        obsapi.obs_sceneitem_set_scale(self._api_obj, scale)

    @property
    def alignment(self) -> int:
        return obsapi.obs_sceneitem_get_alignment(self.api_obj)

    @alignment.setter
    def alignment(self, new_alignment: int):
        '''
        new_alignment: Can be any bitwise OR combination of ETransformAlignment values
        '''
        obsapi.obs_sceneitem_set_alignment(self._api_obj, new_alignment)
    
    def order_up(self):
        return obsapi.obs_sceneitem_set_order(EOrderMovement.OBS_ORDER_MOVE_UP)

    def order_down(self):
        return obsapi.obs_sceneitem_set_order(EOrderMovement.OBS_ORDER_MOVE_DOWN)

    def order_top(self):
        return obsapi.obs_sceneitem_set_order(EOrderMovement.OBS_ORDER_MOVE_TOP)

    def order_bottom(self):
        return obsapi.obs_sceneitem_set_order(EOrderMovement.OBS_ORDER_MOVE_BOTTOM)

    @property
    def order_idx(self):
        return obsapi.obs_sceneitem_get_order_position(self._api_obj)

    @order_idx.setter
    def order_idx(self, new_pos_idx):
        obsapi.obs_sceneitem_set_order_position(self._api_obj, new_pos_idx)

    def destroy(self):
        obsapi.obs_sceneitem_remove(self.api_obj)
    
    @property
    def bounds_type(self) -> EBoundsType:
        return obsapi.obs_sceneitem_get_bounds_type(self.api_obj)
    
    @bounds_type.setter
    def bounds_type(self, bounds_type: EBoundsType):
        obsapi.obs_sceneitem_set_bounds_type(self.api_obj, bounds_type.value)
    
    @property
    def bounds_alignment(self) -> int:
        return obsapi.obs_sceneitem_get_bounds_alignment(self.api_obj)
    
    @bounds_alignment.setter
    def bounds_alignment(self, bounds_alignment: int):
        obsapi.obs_sceneitem_set_bounds_alignment(self.api_obj, bounds_alignment)
    
    @property
    def bounds(self) -> int:
        bounds = obsapi.vec2()
        obsapi.obs_sceneitem_get_bounds(self.api_obj, bounds)
        return (bounds.x, bounds.y)
    
    @bounds.setter
    def bounds(self, new_bounds: tuple[float, float]):
        bounds = obsapi.vec2()
        bounds.x = new_bounds[0]
        bounds.y = new_bounds[1]
        obsapi.obs_sceneitem_set_bounds(self.api_obj, bounds)
    
    #void obs_sceneitem_set_bounds(obs_sceneitem_t *item, const struct vec2 *bounds)
    #void obs_sceneitem_get_bounds(const obs_sceneitem_t *item, struct vec2 *bounds)

    #void obs_sceneitem_set_crop(obs_sceneitem_t *item, const struct obs_sceneitem_crop *crop)
    #void obs_sceneitem_get_crop(const obs_sceneitem_t *item, struct obs_sceneitem_crop *crop)

    #void obs_sceneitem_set_scale_filter(obs_sceneitem_t *item, enum obs_scale_type filter)
    #enum obs_scale_type obs_sceneitem_get_scale_filter(obs_sceneitem_t *item)

    #void obs_sceneitem_set_blending_method(obs_sceneitem_t *item, enum obs_blending_method method)
    #enum obs_blending_method obs_sceneitem_get_blending_method(obs_sceneitem_t *item)

    #void obs_sceneitem_set_blending_mode(obs_sceneitem_t *item, enum obs_blending_type type)
    #enum obs_blending_type obs_sceneitem_get_blending_mode(obs_sceneitem_t *item)

    #void obs_sceneitem_set_show_transition(obs_sceneitem_t *item, obs_source_t *transition)
    #void obs_sceneitem_set_hide_transition(obs_sceneitem_t *item, obs_source_t *transition)

    #obs_source_t *obs_sceneitem_get_show_transition(obs_sceneitem_t *item)
    #obs_source_t *obs_sceneitem_get_hide_transition(obs_sceneitem_t *item)

    #void obs_sceneitem_set_show_transition_duration(obs_sceneitem_t *item, uint32_t duration_ms)
    #void obs_sceneitem_set_hide_transition_duration(obs_sceneitem_t *item, uint32_t duration_ms)

    #uint32_t obs_sceneitem_get_show_transition_duration(obs_sceneitem_t *item)
    #uint32_t obs_sceneitem_get_hide_transition_duration(obs_sceneitem_t *item)




#Scene Item Functions

#obs_data_t *obs_scene_save_transform_states(obs_scene_t *scene, bool all_items)
#void obs_scene_load_transform_states(const char *states)

#void obs_sceneitem_set_info(obs_sceneitem_t *item, const struct obs_transform_info *info)
#void obs_sceneitem_get_info(const obs_sceneitem_t *item, struct obs_transform_info *info)

#void obs_sceneitem_get_draw_transform(const obs_sceneitem_t *item, struct matrix4 *transform)

#void obs_sceneitem_get_box_transform(const obs_sceneitem_t *item, struct matrix4 *transform)

#void obs_sceneitem_defer_update_begin(obs_sceneitem_t *item)
#void obs_sceneitem_defer_update_end(obs_sceneitem_t *item)

#obs_data_t *obs_sceneitem_get_private_settings(obs_sceneitem_t *item)

#void obs_sceneitem_do_transition(obs_sceneitem_t *item, bool visible)


#Scene Item Group Functions

#obs_sceneitem_t *obs_scene_add_group(obs_scene_t *scene, const char *name)

#obs_sceneitem_t *obs_scene_add_group2(obs_scene_t *scene, const char *name, bool signal)

#obs_sceneitem_t *obs_scene_insert_group(obs_scene_t *scene, const char *name, obs_sceneitem_t **items, size_t count)

#obs_sceneitem_t *obs_scene_insert_group2(obs_scene_t *scene, const char *name, obs_sceneitem_t **items, size_t count, bool signal)

#obs_sceneitem_t *obs_scene_get_group(obs_scene_t *scene, const char *name)

#obs_scene_t *obs_group_from_source(const obs_source_t *source)

#obs_scene_t *obs_group_or_scene_from_source(const obs_source_t *source)

#bool obs_sceneitem_is_group(obs_sceneitem_t *item)

#obs_scene_t *obs_sceneitem_group_get_scene(const obs_sceneitem_t *group)

#void obs_sceneitem_group_ungroup(obs_sceneitem_t *group)

#void obs_sceneitem_group_ungroup2(obs_sceneitem_t *group, bool signal)

#void obs_sceneitem_group_add_item(obs_sceneitem_t *group, obs_sceneitem_t *item)

#void obs_sceneitem_group_remove_item(obs_sceneitem_t *item)

#obs_sceneitem_t *obs_sceneitem_get_group(obs_sceneitem_t *item)

#obs_sceneitem_t *obs_sceneitem_group_from_scene(obs_scene_t *scene)

#obs_sceneitem_t *obs_sceneitem_group_from_source(obs_source_t *source)

#void obs_sceneitem_group_enum_items(obs_sceneitem_t *group, bool (*callback)(obs_scene_t*, obs_sceneitem_t*, void*), void *param)

#void obs_sceneitem_defer_group_resize_begin(obs_sceneitem_t *item)

#void obs_sceneitem_defer_group_resize_end(obs_sceneitem_t *item)

