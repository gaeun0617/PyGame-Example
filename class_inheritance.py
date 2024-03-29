class AudioVisual:
    def __init__(self, power, volume):
        self.power = power
        self.volume = volume
    def switch(self, on_off):
        self.power = on_off
    def set_volume(self, vol):
        self.volume = vol

class Audio(AudioVisual):
    def __init__(self, power, volume):
        super().__init__(power, volume)
    def tune(self):
        str = "La la la..." if self.power else "turn it on"
        print(str)

class TV(AudioVisual):
    def __init__(self, power, volume, size):
        super().__init__(power, volume)
        self.size = size
    def watch(self):
        str = "have fun!" if self.power else "switch on"
        print(str)