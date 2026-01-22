import alchemy.elements

def healing_potion():
    return (
        f"Healing potion brewed with {alchemy.elements.create_fire()} and "
        f"{alchemy.elements.create_water()}"
    )


def strength_potion():
    return (
        f"Strength potion brewed with {alchemy.elements.create_earth()} and"
        f" {alchemy.elements.create_fire()}"
    )


def invisibility_potion():
    return (
        f"Invisibility potion brewed with {alchemy.elements.create_air()} and"
        f"{alchemy.elements.create_water()}"
    )


def wisdom_potion():
    return (
        "Wisdom potion brewed with all elements:"
        f"{alchemy.elements.create_air()}"
        f"{alchemy.elements.create_earth()}"
        f"{alchemy.elements.create_water()}"
        f"{alchemy.elements.create_fire()}"
    )
