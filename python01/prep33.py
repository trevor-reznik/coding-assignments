def get_ok_items(carryon, personal, restricted):
    a = []
    for _ in carryon:
        if _ in restricted:
            a.append(_)
    for _ in a:
        carryon.discard(_)
    a = []
    for _ in personal:
        if _ in restricted:
            a.append(_)
    for _ in a:
        personal.discard(_)
    personal.update(carryon)
    return personal
