from flask import Blueprint
from app.models.planets import planet_list

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    results_list = []

    for planet in planet_list:
        results_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            size=planet.size
        ))

    return results_list



