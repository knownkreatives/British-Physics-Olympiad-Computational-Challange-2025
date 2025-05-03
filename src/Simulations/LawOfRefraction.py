import math

def calculate_angle_of_refraction(
    angleOfIncidence: float,
    refractiveIndexIncident: float,
    refractiveIndex: float):
    """
    Calculate the refraction angle based on the law of refraction.
    The angle of refraction is greater than the angle of incidence when the refractive index of the initial medium is greater than the refractive index of the new medium.

    Parameters:
        angleOfIncidence (float): The angle of incidence in degrees.
        refractiveIndexIncident (float): The refractive index of the first medium.
        refractiveIndex (float): The refractive index of the second medium.

    Returns:
        float: The angle of refraction in degrees.
    """

    angleOfIncidenceRad = math.radians(angleOfIncidence)
    
    sineAngleOfRefraction = (refractiveIndexIncident / refractiveIndex) * math.sin(angleOfIncidenceRad)
    
    if sineAngleOfRefraction > 1:
        raise ValueError("Total internal reflection occurs; no refraction.")
    
    angleOfRefractionRad = math.asin(sineAngleOfRefraction)
    angleOfRefraction: float = math.degrees(angleOfRefractionRad)
    
    return angleOfRefraction

def calculate_angle_of_incidence(
    angleOfRefraction: float,
    refractiveIndexIncident: float,
    refractiveIndex: float):
    """
    Calculate the refraction angle based on the law of refraction.
    The angle of refraction is greater than the angle of incidence when the refractive index of the initial medium is greater than the refractive index of the new medium.

    Parameters:
        angleOfRefraction (float): The angle of refaction in degrees.
        refractiveIndexIncident (float): The refractive index of the first medium.
        refractiveIndex (float): The refractive index of the second medium.

    Returns:
        float: The angle of incidence in degrees.
    """

    angleOfRefractionRad = math.radians(angleOfRefraction)
    
    sineAngleOfIncidence = (refractiveIndexIncident / refractiveIndex) * math.sin(angleOfRefractionRad)
    
    if sineAngleOfIncidence > 1:
        raise ValueError("Total internal reflection occurs; no refraction.")
    
    angleOfIncidenceRad = math.asin(sineAngleOfIncidence)
    angleOfIncidence: float = math.degrees(angleOfIncidenceRad)
    
    return angleOfIncidence

def calculate_refractive_index(
    angleOfIncidence: float,
    angleOfRefraction: float,
    refractiveIndexIncident: float):
    """
    Calculate the refractive index of the second medium based on the law of refraction.

    Parameters:
        angleOfIncidence (float): The angle of incidence in degrees.
        angleOfRefraction (float): The angle of refraction in degrees.
        refractiveIndexIncident (float): The refractive index of the first medium.

    Returns:
        float: The refractive index of the second medium.
    """

    angleOfIncidenceRad = math.radians(angleOfIncidence)
    angleOfRefractionRad = math.radians(angleOfRefraction)
    
    refractiveIndexRefacted: float = (refractiveIndexIncident * math.sin(angleOfIncidenceRad)) / math.sin(angleOfRefractionRad)
    
    return refractiveIndexRefacted

def calculate_refractive_index_incident(
    angleOfIncidence: float,
    angleOfRefraction: float,
    refractiveIndex: float):
    """
    Calculate the refractive index of the first medium based on the law of refraction.

    Parameters:
        angleOfIncidence (float): The angle of incidence in degrees.
        angleOfRefraction (float): The angle of refraction in degrees.
        refractiveIndex (float): The refractive index of the second medium.

    Returns:
        float: The refractive index of the first medium.
    """

    angleOfIncidenceRad = math.radians(angleOfIncidence)
    angleOfRefractionRad = math.radians(angleOfRefraction)
    
    refractiveIndexIncident: float = (refractiveIndex * math.sin(angleOfIncidenceRad)) / math.sin(angleOfRefractionRad)
    
    return refractiveIndexIncident