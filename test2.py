from Xlib import X, XK, display
from Xlib.ext import record
from Xlib.protocol import rq

local_display = display.Display()
recorded_keys = []

def lookup_keysym(keysym):
    return XK.keysym_to_string(keysym)

def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped or (not reply.key_code and reply.event_type not in [X.KeyPress, X.KeyRelease]):
        return
    if reply.event_type == X.KeyPress:
        keysym = local_display.keycode_to_keysym(reply.key_code, 0)
        if keysym:
            recorded_keys.append(lookup_keysym(keysym))
    elif reply.event_type == X.KeyRelease:
        keysym = local_display.keycode_to_keysym(reply.key_code, 0)
        if keysym:
            recorded_keys.append(lookup_keysym(keysym))
            print(f"Key Released: {' + '.join(recorded_keys)}")
            recorded_keys.clear()

ctx = local_display.record_create_context(
    0,
    [record.AllClients],
    [{
        'core_requests': (0, 0),
        'core_replies': (0, 0),
        'ext_requests': (0, 0, 0, 0),
        'ext_replies': (0, 0, 0, 0),
        'delivered_events': (0, 0),
        'device_events': (X.KeyPress, X.KeyRelease),
        'errors': (0, 0),
        'client_started': False,
        'client_died': False,
    }]
)

local_display.record_enable_context(ctx, record_callback)
local_display.record_free_context(ctx)
