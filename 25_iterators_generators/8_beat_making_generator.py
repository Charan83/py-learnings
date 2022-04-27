def current_beat(times):
    beats = (1, 2, 3, 4)
    idx = 0
    _times = 0
    while _times < times:
        yield beats[idx]
        if idx < len(beats)-1:
            idx += 1
        else:
            idx = 0
        _times += 1


gen_cb = current_beat(10)
print(next(gen_cb))
print(next(gen_cb))
print(next(gen_cb))
print(next(gen_cb))
print(next(gen_cb))
print(next(gen_cb))
print(next(gen_cb))
print(next(gen_cb))
