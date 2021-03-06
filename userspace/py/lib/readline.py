import ctypes

auto_history = True

py = ctypes.CDLL("libpython3.6m.so")
rline_lib = ctypes.CDLL("libtoaru-rline.so")

readline_func = ctypes.c_void_p.in_dll(py,"PyOS_ReadlineFunctionPointer")
t = ctypes.c_char_p.in_dll(rline_lib,"rline_for_python")
readline_func.value = ctypes.addressof(t)

# Change exit string to "exit()"
exit_string_lib = ctypes.c_char_p.in_dll(rline_lib,"rline_exit_string")
exit_string = ctypes.c_char_p(b"")
exit_string_lib.value = exit_string.value

def parse_and_bind(s):
    pass

def read_init_file(filename=None):
    pass

def get_line_buffer():
    return None

def insert_text(string):
    return None

def redisplay():
    pass

def read_history_file(filename):
    pass

def write_history_file(filename):
    pass

def append_history_file(nelements,filename=None):
    pass

def get_history_length():
    return 0

def set_history_length(length):
    pass

def clear_history():
    pass

def get_current_history_length():
    return ctypes.c_int.in_dll(rline_lib,"rline_history_count").value

def get_history_item(index):
    if index < 1 or index > get_current_history_length():
        raise ValueError("bad history index")
    index -= 1
    return cast(rline_lib.rline_history_get(index), c_char_p).value.decode('utf-8')

def remove_history_item(pos):
    pass

def replace_history_item(pos, item):
    pass

def add_history(line):
    rline_lib.rline_history_insert(line.encode('utf-8'))

def set_auto_history(enabled):
    auto_history = enabled

def set_startup_hook(func=None):
    pass

def set_pre_input_hook(func=None):
    pass

def set_completer(func=None):
    pass

def get_completer():
    return None

def get_completion_type():
    return None

def get_begidx():
    return 0

def get_endidx():
    return 0

def set_completer_delims(string):
    pass

def get_completer_delims():
    return ""

def set_completion_display_matches_hook(func=None):
    pass

