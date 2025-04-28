
def wavelength_to_rgb(wavelength):
    gamma: float = 0.8
    intensity_max: int = 255
    factor: float
    R = G = B = 0

    # Normalized values
    if 380 <= wavelength <= 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 < wavelength <= 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 < wavelength <= 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 < wavelength <= 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength <= 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= wavelength <= 750:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = G = B = 0.0

    # Intensity correction
    if 380 <= wavelength <= 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 <= wavelength <= 700:
        factor = 1.0
    elif 700 <= wavelength <= 750:
        factor = 0.3 + 0.7 * (750 - wavelength) / (750 - 700)
    else:
        factor = 0.0

    def adjust(color):
        if color == 0.0:
            return 0
        return round(intensity_max * ((color * factor) ** gamma))

    return adjust(R), adjust(G), adjust(B)

def rgb_to_hex(r, g, b):
    return '#{0:02x}{1:02x}{2:02x}'.format(int(r), int(g), int(b))


