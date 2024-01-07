class DebugInspector:
    def __init__(self):
        self.input_type = None

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "code": ("STRING", {"multiline": True, "default": "# Write your code here\n"}),

            },
            "optional": {
                "value1": ("*",),
                "value2": ("*",),
            },
        }

    RETURN_TYPES = ("*","*",)
    RETURN_NAMES = ("value1", "value2")

    FUNCTION = "execute_code"

    CATEGORY = "utils/DebugInspector"

    def execute_code(self, code, value1=None, value2=None):
        exec_locals = {
            "value1": value1,
            "value2": value2
        }
        exec(code, {}, exec_locals)
        value1 = exec_locals.get("value1", value1)
        value2 = exec_locals.get("value2", value2)
        return (value1,value2)

class TypeConversion:
    def __init__(self):
        self.input_type = None

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("*",)
            }
        }

    RETURN_TYPES = (
        "INT", "FLOAT", "BOOL", "STRING",
        "CLIP", "CONDITIONING", "IMAGE",
        "LATENT","MASK", "MODEL", "VAE"
    )

    FUNCTION = "TypeConversion"

    CATEGORY = "utils/TypeConversion"

    def TypeConversion(self, value,):
        return (value,value,value,value,
                value,value,value,value,
                value,value,value,)

NODE_CLASS_MAPPINGS = {
    "DebugInspector": DebugInspector,
    "TypeConversio": TypeConversion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DebugInspector": "DebugInspector",
    "TypeConversio": "Type Conversion",

}
