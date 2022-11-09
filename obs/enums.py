from enum import Enum

import obspython as obsapi


class ETransformAlignment(Enum):
    OBS_ALIGN_CENTER = 0
    OBS_ALIGN_LEFT = 1 << 0
    OBS_ALIGN_RIGHT = 1 << 1
    OBS_ALIGN_TOP = 1 << 2
    OBS_ALIGN_BOTTOM = 1 << 3


class EBoundsType(Enum):
    OBS_BOUNDS_NONE = obsapi.OBS_BOUNDS_NONE
    OBS_BOUNDS_STRETCH = obsapi.OBS_BOUNDS_STRETCH
    OBS_BOUNDS_SCALE_INNER = obsapi.OBS_BOUNDS_SCALE_INNER
    OBS_BOUNDS_SCALE_OUTER = obsapi.OBS_BOUNDS_SCALE_OUTER
    OBS_BOUNDS_SCALE_TO_WIDTH = obsapi.OBS_BOUNDS_SCALE_TO_WIDTH
    OBS_BOUNDS_SCALE_TO_HEIGHT = obsapi.OBS_BOUNDS_SCALE_TO_HEIGHT
    OBS_BOUNDS_MAX_ONLY = obsapi.OBS_BOUNDS_MAX_ONLY


class EScaleType(Enum):
    OBS_SCALE_DISABLE = obsapi.OBS_SCALE_DISABLE
    OBS_SCALE_POINT = obsapi.OBS_SCALE_POINT
    OBS_SCALE_BICUBIC = obsapi.OBS_SCALE_BICUBIC
    OBS_SCALE_BILINEAR = obsapi.OBS_SCALE_BILINEAR
    OBS_SCALE_LANCZOS = obsapi.OBS_SCALE_LANCZOS


class EBlendingType(Enum):
    OBS_BLEND_NORMAL = obsapi.OBS_BLEND_NORMAL
    OBS_BLEND_ADDITIVE = obsapi.OBS_BLEND_ADDITIVE
    OBS_BLEND_SUBTRACT = obsapi.OBS_BLEND_SUBTRACT
    OBS_BLEND_SCREEN = obsapi.OBS_BLEND_SCREEN
    OBS_BLEND_MULTIPLY = obsapi.OBS_BLEND_MULTIPLY
    OBS_BLEND_LIGHTEN = obsapi.OBS_BLEND_LIGHTEN
    OBS_BLEND_DARKEN = obsapi.OBS_BLEND_DARKEN


class EOrderMovement(Enum):
    OBS_ORDER_MOVE_UP = obsapi.OBS_ORDER_MOVE_UP
    OBS_ORDER_MOVE_DOWN = obsapi.OBS_ORDER_MOVE_DOWN
    OBS_ORDER_MOVE_TOP = obsapi.OBS_ORDER_MOVE_TOP
    OBS_ORDER_MOVE_BOTTOM = obsapi.OBS_ORDER_MOVE_BOTTOM


class ESceneDuplicationType(Enum):
    OBS_SCENE_DUP_REFS = obsapi.OBS_SCENE_DUP_COPY                  # Duplicates the scene, but scene items are only duplicated with references
    OBS_SCENE_DUP_COPY = obsapi.OBS_SCENE_DUP_COPY                  # Duplicates the scene, and scene items are also fully duplicated when possible
    OBS_SCENE_DUP_PRIVATE_REFS = obsapi.OBS_SCENE_DUP_PRIVATE_REFS  # Duplicates with references, but the scene is a private source
    OBS_SCENE_DUP_PRIVATE_COPY = obsapi.OBS_SCENE_DUP_PRIVATE_COPY  # Fully duplicates scene items when possible, but the scene and duplicates sources are private sources
