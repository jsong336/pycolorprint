"""
Zero effort.
"""
import re

COLORPAD = {
    "purple" : '\033[95m',
    "cyan" : '\033[96m',
    "darkcyan" : '\033[36m',
    "blue" : '\033[94m',
    "green" : '\033[92m',
    "yellow" : '\033[93m',
    "red" : '\033[91m',
    "bold" : '\033[1m',
    "underline" : '\033[4m',
    "end" : '\033[0m'
}

RE_COLOR_MATCH = re.compile('\[([a-zA-Z0-9,.?!\-+:\(\)\s+]+):([a-z]{3,10})\]')

class ColorPrinter:
    @staticmethod
    def init():
        for c, v in COLORPAD.items():
            exec("ColorPrinter.%s = lambda msg: \"%s\" + msg + \"%s\"" % (c, v, COLORPAD['end']))
    
    @staticmethod
    def embed_color(msg):
        for m, c in re.findall(RE_COLOR_MATCH, msg):
            msg = msg.replace('[' + m +':' + c + ']', getattr(ColorPrinter, c)(m))
        return msg

    @staticmethod
    def print(msg, strip=True):
        if strip:
            msg = msg.strip()
        print(ColorPrinter.embed_color(msg))
    
ColorPrinter.init()
