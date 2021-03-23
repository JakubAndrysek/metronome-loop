import metronome_loop


def five_sec_prin():
    print("five_sec")


one_sec = metronome_loop.metronome(1000, lambda: print("one_sec"))
five_sec = metronome_loop.metronome(5000, five_sec_prin)
ten_sec = metronome_loop.metronome(10000)

while True:
    one_sec.loop()

    five_sec.loop()

    if ten_sec.loop():
        print("ten_sec")
