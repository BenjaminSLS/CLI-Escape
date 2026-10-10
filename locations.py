# Locations for the player to go and related.
def locations():
    return {
        # Top floor
        'bedroom': ['bathroom', 'closet', 'hallway'],
        'closet': ['bedroom'],
        'bathroom': ['tub', 'bedroom'],
        'tub': ['bathroom'],
        'hallway': ['stairs', 'bedroom', 'playroom'],
        'playroom': ['hallway'],
        'stairs': ['hallway', 'living room'],

        # Bottom floor
        'living room': ['stairs', 'front door', 'dining room', 'kitchen'],
        'dining room': ['living room', 'kitchen', 'backyard'],
        'kitchen': ['dining room', 'backyard', 'living room'],
    
        # Outside
        'backyard': ['living room', 'kitchen', 'shed', 'fence'],
        'fence': ['shed', 'backyard'],
        'shed': ['firewood', 'backyard', 'tools'],
        'tools': ['shed'],
        'firewood': ['shed'],

        # Final Location
        'front door': []
    }
