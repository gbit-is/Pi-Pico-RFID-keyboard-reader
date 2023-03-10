# SPDX-FileCopyrightText: 2021 Neradoc NeraOnGit@ri1.fr
#
# SPDX-License-Identifier: MIT
"""
This file was automatically generated using Circuitpython_Keyboard_Layouts
"""
from adafruit_hid.keyboard_layout_base import KeyboardLayoutBase


__version__ = "0.0.1-alpha.0"
__repo__ = "https://github.com/Neradoc/Circuitpython_Keyboard_Layouts.git"


class KeyboardLayout(KeyboardLayoutBase):
    ASCII_TO_KEYCODE = (
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2a'  # BACKSPACE
        b'\x2b'  # '\t'
        b'\x28'  # '\n'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x29'  # ESC
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x00'
        b'\x2c'  # ' '
        b'\x9e'  # '!'
        b'\x9f'  # '"'
        b'\xa0'  # '#'
        b'\xa1'  # '$'
        b'\xa2'  # '%'
        b'\xa3'  # '&'
        b'\x30'  # "'"
        b'\xa5'  # '('
        b'\xa6'  # ')'
        b'\xb1'  # '*'
        b'\x31'  # '+'
        b'\x36'  # ','
        b'\x2e'  # '-'
        b'\x37'  # '.'
        b'\xa4'  # '/'
        b'\x27'  # '0'
        b'\x1e'  # '1'
        b'\x1f'  # '2'
        b'\x20'  # '3'
        b'\x21'  # '4'
        b'\x22'  # '5'
        b'\x23'  # '6'
        b'\x24'  # '7'
        b'\x25'  # '8'
        b'\x26'  # '9'
        b'\xb7'  # ':'
        b'\xb6'  # ';'
        b'\x64'  # '<'
        b'\xa7'  # '='
        b'\xe4'  # '>'
        b'\xb0'  # '?'
        b'\x14'  # '@'
        b'\x84'  # 'A'
        b'\x85'  # 'B'
        b'\x86'  # 'C'
        b'\x87'  # 'D'
        b'\x88'  # 'E'
        b'\x89'  # 'F'
        b'\x8a'  # 'G'
        b'\x8b'  # 'H'
        b'\x8c'  # 'I'
        b'\x8d'  # 'J'
        b'\x8e'  # 'K'
        b'\x8f'  # 'L'
        b'\x90'  # 'M'
        b'\x91'  # 'N'
        b'\x92'  # 'O'
        b'\x93'  # 'P'
        b'\x94'  # 'Q'
        b'\x95'  # 'R'
        b'\x96'  # 'S'
        b'\x97'  # 'T'
        b'\x98'  # 'U'
        b'\x99'  # 'V'
        b'\x9a'  # 'W'
        b'\x9b'  # 'X'
        b'\x9c'  # 'Y'
        b'\x9d'  # 'Z'
        b'\x25'  # '['
        b'\x2d'  # '\\'
        b'\x26'  # ']'
        b'\x00'  # '^' (Dead key)
        b'\xae'  # '_'
        b'\x00'  # '`' (Dead key)
        b'\x04'  # 'a'
        b'\x05'  # 'b'
        b'\x06'  # 'c'
        b'\x07'  # 'd'
        b'\x08'  # 'e'
        b'\x09'  # 'f'
        b'\x0a'  # 'g'
        b'\x0b'  # 'h'
        b'\x0c'  # 'i'
        b'\x0d'  # 'j'
        b'\x0e'  # 'k'
        b'\x0f'  # 'l'
        b'\x10'  # 'm'
        b'\x11'  # 'n'
        b'\x12'  # 'o'
        b'\x13'  # 'p'
        b'\x14'  # 'q'
        b'\x15'  # 'r'
        b'\x16'  # 's'
        b'\x17'  # 't'
        b'\x18'  # 'u'
        b'\x19'  # 'v'
        b'\x1a'  # 'w'
        b'\x1b'  # 'x'
        b'\x1c'  # 'y'
        b'\x1d'  # 'z'
        b'\x24'  # '{'
        b'\x64'  # '|'
        b'\x27'  # '}'
        b'\x30'  # '~'
        b'\x00'
    )
    NEED_ALTGR = '@[\\]{|}~°µ€'
    HIGHER_ASCII = {
        0x20ac: 0x22,  # '€'
        0xf6: 0x2d,  # 'ö'
        0xd6: 0xad,  # 'Ö'
        0xf0: 0x2f,  # 'ð'
        0xd0: 0xaf,  # 'Ð'
        0xe6: 0x33,  # 'æ'
        0xc6: 0xb3,  # 'Æ'
        0xb0: 0x35,  # '°'
        0xb5: 0x10,  # 'µ'
        0xfe: 0x38,  # 'þ'
        0xde: 0xb8,  # 'Þ'
    }
    COMBINED_KEYS = {
        0xe1: 0x3461,  # 'á'
        0xe9: 0x3465,  # 'é'
        0xed: 0x3469,  # 'í'
        0xf3: 0x346f,  # 'ó'
        0xfa: 0x3475,  # 'ú'
        0xfd: 0x3479,  # 'ý'
        0xc1: 0x3441,  # 'Á'
        0xc9: 0x3445,  # 'É'
        0xcd: 0x3449,  # 'Í'
        0xd3: 0x344f,  # 'Ó'
        0xda: 0x3455,  # 'Ú'
        0xdd: 0x3459,  # 'Ý'
        0xb4: 0x3420,  # '´'
        0xe2: 0x34e1,  # 'â'
        0xea: 0x34e5,  # 'ê'
        0xee: 0x34e9,  # 'î'
        0xf4: 0x34ef,  # 'ô'
        0xfb: 0x34f5,  # 'û'
        0xc2: 0x34c1,  # 'Â'
        0xca: 0x34c5,  # 'Ê'
        0xce: 0x34c9,  # 'Î'
        0xd4: 0x34cf,  # 'Ô'
        0xdb: 0x34d5,  # 'Û'
        0x5e: 0x34a0,  # '^'
        0xe5: 0x3561,  # 'å'
        0xc5: 0x3541,  # 'Å'
        0xb0: 0x3520,  # '°'
        0xe4: 0xb561,  # 'ä'
        0xeb: 0xb565,  # 'ë'
        0xef: 0xb569,  # 'ï'
        0xf6: 0xb56f,  # 'ö'
        0xfc: 0xb575,  # 'ü'
        0xff: 0xb579,  # 'ÿ'
        0xc4: 0xb541,  # 'Ä'
        0xcb: 0xb545,  # 'Ë'
        0xcf: 0xb549,  # 'Ï'
        0xd6: 0xb54f,  # 'Ö'
        0xdc: 0xb555,  # 'Ü'
        0xa8: 0xb520,  # '¨'
        0xe0: 0x31e1,  # 'à'
        0xe8: 0x31e5,  # 'è'
        0xec: 0x31e9,  # 'ì'
        0xf2: 0x31ef,  # 'ò'
        0xf9: 0x31f5,  # 'ù'
        0xc0: 0x31c1,  # 'À'
        0xc8: 0x31c5,  # 'È'
        0xcc: 0x31c9,  # 'Ì'
        0xd2: 0x31cf,  # 'Ò'
        0xd9: 0x31d5,  # 'Ù'
        0x60: 0x31a0,  # '`'
    }
