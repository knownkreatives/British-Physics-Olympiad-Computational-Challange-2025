RED_WAVELENGTH = 650.0  # nm
GREEN_WAVELENGTH = 530.0  # nm
BLUE_WAVELENGTH = 470.0  # nm

RED_FREQUENCY = 460e12  # Hz
GREEN_FREQUENCY = 566e12  # Hz
BLUE_FREQUENCY = 638e12  # Hz

def frequency_to_wavelength(frequency: float) -> float:
    """
    Convert frequency in Hz to wavelength in nm.
    :param frequency: Frequency in Hz
    :return: Wavelength in nm
    """
    speed_of_light = 3e8  # Speed of light in m/s
    wavelength = speed_of_light / frequency  # Wavelength in meters
    return wavelength * 1e9  # Convert to nanometers

def wavelength_to_frequency(wavelength: float) -> float:
    """
    Convert wavelength in nm to frequency in Hz.
    :param wavelength: Wavelength in nm
    :return: Frequency in Hz
    """
    speed_of_light = 3e8  # Speed of light in m/s
    wavelength_meters = wavelength * 1e-9  # Convert to meters
    frequency = speed_of_light / wavelength_meters  # Frequency in Hz
    return frequency

def wavelength_to_rgb(wavelength, scale: float = 1.0) -> tuple[int, int, int]:
    gamma: float = 0.8
    intensity_max: int = 255
    factor: float
    R = G = B = 0

    scaled_wavelength = wavelength * scale

    # Normalized values
    if 380 <= scaled_wavelength <= 440:
        R = -(scaled_wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 < scaled_wavelength <= 490:
        R = 0.0
        G = (scaled_wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 < scaled_wavelength <= 510:
        R = 0.0
        G = 1.0
        B = -(scaled_wavelength - 510) / (510 - 490)
    elif 510 < scaled_wavelength <= 580:
        R = (scaled_wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= scaled_wavelength <= 645:
        R = 1.0
        G = -(scaled_wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= scaled_wavelength <= 750:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = G = B = 0.0

    # Intensity correction
    if 380 <= scaled_wavelength <= 420:
        factor = 0.3 + 0.7 * (scaled_wavelength - 380) / (420 - 380)
    elif 420 <= scaled_wavelength <= 700:
        factor = 1.0
    elif 700 <= scaled_wavelength <= 750:
        factor = 0.3 + 0.7 * (750 - scaled_wavelength) / (750 - 700)
    else:
        factor = 0.0

    def adjust(color):
        if color == 0.0:
            return 0
        return round(intensity_max * ((color * factor) ** gamma))

    return adjust(R), adjust(G), adjust(B)

def rgb_to_hex(r, g, b):
    return '#{0:02x}{1:02x}{2:02x}'.format(int(r), int(g), int(b))

def get_color_gradient(wavelength: list[float]) -> list[float]:
    colors = [wavelength_to_rgb(wl) for wl in wavelength]
    hexColors = [rgb_to_hex(*c) for c in colors]
    segmentColors = hexColors[:-1]  # One less than number of points
    return segmentColors