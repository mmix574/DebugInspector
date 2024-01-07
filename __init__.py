from .DebugInspector import DebugInspector, TypeConversion

NODE_CLASS_MAPPINGS = {
    "DebugInspector": DebugInspector,
    "TypeConversio": TypeConversion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugInspector": "DebugInspector",
    "TypeConversio": "Type Conversion",

}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
