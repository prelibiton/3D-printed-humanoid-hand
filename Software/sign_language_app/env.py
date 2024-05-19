extend_thumb = b'\x55\x34\x04\x01\x02'
bend_thumb = b'\x55\x34\x04\x01\x01'

extend_index = b'\x55\x36\x04\x01\x02'
bend_index = b'\x55\x36\x04\x01\x01'

extend_middle = b'\x55\x38\x04\x01\x02'
bend_middle = b'\x55\x38\x04\x01\x01'

extend_ring = b'\x55\x3A\x04\x01\x02'
bend_ring = b'\x55\x3A\x04\x01\x01'

extend_pinky = b'\x55\x3C\x04\x01\x02'
bend_pinky = b'\x55\x3C\x04\x01\x01'

commands = {}
commands["thumb"] = {}
commands["thumb"]["extend"] = extend_thumb
commands["thumb"]["bend"] = bend_thumb

commands["index"] = {}
commands["index"]["extend"] = extend_index
commands["index"]["bend"] = bend_index

commands["middle"] = {}
commands["middle"]["extend"] = extend_middle
commands["middle"]["bend"] = bend_middle

commands["ring"] = {}
commands["ring"]["extend"] = extend_ring
commands["ring"]["bend"] = bend_ring

commands["pinky"] = {}
commands["pinky"]["extend"] = extend_pinky
commands["pinky"]["bend"] = bend_pinky