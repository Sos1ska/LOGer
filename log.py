# Author: Sos1ska
# Link GitHub -> https://github/Sos1ska
# Link VK -> https://vk.com/nikitasos1ska
import datetime
from ColorSos import SetColor

Root = 'root'

Text = str

View_dict = {
    'View':{
        'txt':  [
                'text', 'txt', 'log', 'TXT', 'LOG'
                ],
        'str':  [
                'str', 'STR', 'out'
                ]
    }
}

def _main_debug_(_TEXT_, _NickName, _Sender, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if msg == True:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] --- {_Sender} '
    else:
        if msg == True:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ] <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ DEBUG {_TEXT_} ]'

def _main_info_(_TEXT_, _NickName):
    return f'[ {_NickName} ] - [ INFO {_TEXT_} ] '

def _main_error_(_TEXT_, _NickName, _Sender, _TypeError, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeError == False or _TypeError == None:
        _TE = False
    else:
        _TE = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} --- {_Sender} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_Sender}'
    else:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] --- {_TypeError} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ] <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ ERROR {_TEXT_} ]'
    
def _main_warning_(_TEXT_, _NickName, _TypeMSG):
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if msg == True:
        return f'[ {_NickName} ] - [ WARNING {_TEXT_} ] <--- {_TypeMSG} '
    else:
        return f'[ {_NickName} ] - [ WARNING {_TEXT_} ]'

def _debug_(View, TEXT=Text, NickName=Root, Sender=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View =='str':
        if WriteTime == True:
            print(
                _main_debug_(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_debug_(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_debug_(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
        else:
            return _main_debug_(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                )
def _info_(View, TEXT=Text, NickName=Root, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) 
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
        else:
            return _main_info_(
                            _TEXT_=TEXT,
                            _NickName=NickName
                )
def _error_(View, TEXT=Text, NickName=Root, Sender=None, TypeError=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_error_(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now()))
        else:
            print(
                _main_error_(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_error_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now())
        else:
            return _main_error_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                )
def _warning_(View, TEXT=Text, NickName=Root, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_warning_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_warning_(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_warning_(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            ) + str(datetime.datetime.now())
        else:
            return _main_warning_(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            )
def _main_debug_color(_TEXT_, _NickName, _Sender, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if msg == True:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] --- {_Sender} '
    else:
        if msg == True:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ]'
def _main_info_color(_TEXT_, _NickName):
    return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}INFO{SetColor.Clear()} {_TEXT_} ] '
def _main_error_color(_TEXT_, _NickName, _Sender, _TypeError, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeError == False or _TypeError == None:
        _TE = False
    else:
        _TE = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} --- {_Sender} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_Sender}'
    else:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ]'
def _main_warning_color(_TEXT_, _NickName, _TypeMSG):
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if msg == True:
        return f'[ {_NickName} ] - [ {SetColor.Fore(color="yellow")}{SetColor.Style(type="bold")}WARNING{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
    else:
        return f'[ {_NickName} ] - [ {SetColor.Fore(color="yellow")}{SetColor.Style(type="bold")}WARNING{SetColor.Clear()} {_TEXT_} ]'

def _main_debug_color(_TEXT_, _NickName, _Sender, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if msg == True:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] --- {_Sender} '
    else:
        if msg == True:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
        else:
            return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}{SetColor.Style(type="underlined")}DEBUG{SetColor.Clear()} {_TEXT_} ]'
def _main_info_color(_TEXT_, _NickName):
    return f'[ {_NickName} ] - [ {SetColor.Fore(color="green")}{SetColor.Style(type="bold")}INFO{SetColor.Clear()} {_TEXT_} ] '
def _main_error_color(_TEXT_, _NickName, _Sender, _TypeError, _TypeMSG):
    if _Sender == False or _Sender == None:
        _Send = False
    else:
        _Send = True
    if _TypeError == False or _TypeError == None:
        _TE = False
    else:
        _TE = True
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if _Send == True:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} --- {_Sender} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_Sender} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_Sender}'
    else:
        if _TE == True:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] --- {_TypeError} '
        else:
            if msg == True:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
            else:
                return f'[ {_NickName} ] - [ {SetColor.Fore(color="red")}{SetColor.Style(type="bold")}ERROR{SetColor.Clear()} {_TEXT_} ]'
def _main_warning_color(_TEXT_, _NickName, _TypeMSG):
    if _TypeMSG == False or _TypeMSG == None:
        msg = False
    else:
        msg = True
    if msg == True:
        return f'[ {_NickName} ] - [ {SetColor.Fore(color="yellow")}{SetColor.Style(type="bold")}WARNING{SetColor.Clear()} {_TEXT_} ] <--- {_TypeMSG} '
    else:
        return f'[ {_NickName} ] - [ {SetColor.Fore(color="yellow")}{SetColor.Style(type="bold")}WARNING{SetColor.Clear()} {_TEXT_} ]'
    
def _debug_color_(View, TEXT=Text, NickName=Root, Sender=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View =='str':
        if WriteTime == True:
            print(
                _main_debug_color(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_debug_color(
                            _TEXT_=TEXT,
                            _NickName=NickName, 
                            _Sender=Sender, 
                            _TypeMSG=TypeMSG
                            )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_debug_color(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
        else:
            return _main_debug_color(
                                _TEXT_=TEXT, 
                                _NickName=NickName, 
                                _Sender=Sender, 
                                _TypeMSG=TypeMSG
                                )
def _info_color(View, TEXT=Text, NickName=Root, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) 
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
                ) + str(datetime.datetime.now())
        else:
            return _main_info_color(
                            _TEXT_=TEXT,
                            _NickName=NickName
            )
def _error_color(View, TEXT=Text, NickName=Root, Sender=None, TypeError=None, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_error_color(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now()))
        else:
            print(
                _main_error_color(
                            _TEXT_=TEXT,
                            _NickName=NickName,
                            _Sender=Sender,
                            _TypeError=TypeError,
                            _TypeMSG=TypeMSG
                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_error_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                ) + str(datetime.datetime.now())
        else:
            return _main_error_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _Sender=Sender,
                                _TypeError=TypeError,
                                _TypeMSG=TypeMSG
                )
def _warning_color(View, TEXT=Text, NickName=Root, TypeMSG=None, WriteTime=True):
    for k, v in View_dict["View"].items():
        if View in v:
            View = k
    if View == 'str':
        if WriteTime == True:
            print(
                _main_warning_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                ) + str(datetime.datetime.now())
            )
        else:
            print(
                _main_warning_color(
                                _TEXT_=TEXT,
                                _NickName=NickName,
                                _TypeMSG=TypeMSG
                                )
            )
    elif View == 'txt':
        if WriteTime == True:
            return _main_warning_color(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            ) + str(datetime.datetime.now())
        else:
            return _main_warning_color(
                                    _TEXT_=TEXT,
                                    _NickName=NickName,
                                    _TypeMSG=TypeMSG
            )

typeloglist = {
            "Type":{
                "error": ['error', 'ERROR', 'Error'],
                "debug": ['debug', 'DEBUG', 'Debug'],
                "warning": ['warning', 'WARNING', 'Warning', 'Warn'],
                "info": ['info', 'INFO', 'Info']
            }
        }
        
typeloglist = {
            "Type":{
                "error": ['error', 'ERROR', 'Error'],
                "debug": ['debug', 'DEBUG', 'Debug'],
                "warning": ['warning', 'WARNING', 'Warning', 'Warn'],
                "info": ['info', 'INFO', 'Info']
            }
        }

class autolog:
    def __init__(self, typelog, text, typemsg=None, wayerror=bytes, waydebug=bytes, waywarn=bytes, wayinfo=bytes, waygeneral=bytes, nick=Root, without_out_console=True | False):
        for k, v in typeloglist["Type"].items():
            if typelog in v:
                typelog=k
        if typelog == 'error':
            if without_out_console == True:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral) as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _error_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) +'\n')
                except TypeError:
                    pass
        elif typelog == 'debug':
            if without_out_console == True:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _debug_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'warning':
            if without_out_console == True:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _warning_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'info':
            if without_out_console == True:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                _info_(View='str', TEXT=text, NickName=nick, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
class autolog_color:
    def __init__(self, typelog, text, typemsg=None, wayerror=bytes, waydebug=bytes, waywarn=bytes, wayinfo=bytes, waygeneral=bytes, nick=Root, without_out_console=True | False):
        for k, v in typeloglist["Type"].items():
            if typelog in v:
                typelog=k
        if typelog == 'error':
            if without_out_console == True:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral) as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayerror, 'a') as error_log:
                    error_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _error_color(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_error_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) +'\n')
                except TypeError:
                    pass
        elif typelog == 'debug':
            if without_out_console == True:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waydebug, 'a') as debug_log:
                    debug_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _debug_color_(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_debug_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'warning':
            if without_out_console == True:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(waywarn, 'a') as warn_log:
                    warn_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                _warning_color(View='str', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_warning_(View='txt', TEXT=text, NickName=nick, TypeMSG=typemsg, WriteTime=True) + '\n')
                except TypeError:
                    pass
        elif typelog == 'info':
            if without_out_console == True:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
            elif without_out_console == False:
                with open(wayinfo, 'a') as info_log:
                    info_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                _info_color(View='str', TEXT=text, NickName=nick, WriteTime=False)
                try:
                    with open(waygeneral, 'a') as general_log:
                        general_log.write(_info_(View='txt', TEXT=text, NickName=nick, WriteTime=True) + '\n')
                except TypeError:
                    pass
                
if __name__ == '__main__':
    _debug_(View='str', TEXT='This is "str" `View`', NickName=Root, Sender=Root, TypeMSG='TEST')
    print(_debug_(View='txt', TEXT='This is "txt" `View`', NickName=Root, Sender=Root, TypeMSG='TEST'))
    print("1. _debug_(View='str', TEXT='This is \"str\" `View`', NickName=Root, Sender=Root, TypeMSG='TEST')")
    print("2. print(_debug(View='txt', TEXT='This is \"txt\" `View`', NickName=Root, Sender=Root, TypeMSG='TEST'))")
    _error_(View='str', TEXT='This is "str" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST')
    print(_error_(View='txt', TEXT='This is "txt" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST'))
    print("""1. _error_(View='str', TEXT='This is "str" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST')""")
    print("""2. print(_error_(View='txt', TEXT='This is "txt" `View`', NickName=Root, Sender=Root, TypeError='TEST Type', TypeMSG='TEST'))""")
    _info_(View='str', TEXT='This is "str" `View`', NickName=Root)
    print(_info_(View='txt', TEXT='This is "txt" `View`', NickName=Root))
    print("""1. _info_(View='str', TEXT='This is "str" `View`', NickName=Root)""")
    print("""2. print(_info_(View='txt', TEXT='This is "txt" `View`', NickName=Root))""")
    _warning_(View='str', TEXT='This is "str" `View`', NickName=Root, TypeMSG='TEST')
    print(_warning_(View='txt', TEXT='This is "txt" `View`', NickName=Root, TypeMSG='TEST'))
    print("""1. _warning_(View='str', TEXT='This is "str" `View`', NickName=Root, TypeMSG='TEST')""")
    print("""2. print(_warning_(View='txt', TEXT='This is "txt" `View`', NickName=Root, TypeMSG='TEST'))""")
