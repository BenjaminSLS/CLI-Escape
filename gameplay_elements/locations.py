# Locations for the player to go and related.
def location_text():
    return {
        # Top floor
        'bedroom': ('closet', 'bathroom', 'hallway'),
        'closet': ('bedroom',),
        'bathroom': ('tub', 'bedroom'),
        'tub': ('bathroom', ),
        'hallway': ('stairs', 'bedroom', 'playroom'),
        'playroom': ('hallway', ),
        'stairs': ('living room', 'hallway'),

        # Bottom floor
        'living room': ('front door', 'stairs', 'kitchen', 'dining room'),
        'dining room': ('living room', 'kitchen', 'backyard'),
        'kitchen': ('living room', 'dining room'),
    
        # Outside
        'backyard': ('living room',  'shed', 'fence'),
        'fence': ('shed', 'backyard'),
        'shed': ('firewood', 'backyard', 'tools'),
        'tools': ('shed', ),
        'firewood': ('shed', ),

        # Final Location
        'front door': ()
    }

def location_images ():
    return {
        # Top floor
        'bedroom': (' ._ Closet', ' |________', ' | \ |==| |', ' |_/ |__| |', '/         |- Hallway', '||________|', '|_ Bathroom'),
        'closet': ('__', '| |', '|__/'),
        'bathroom': ('  ._ Tub','__|___', '|____|', '| |  |', '|_|___/- Bedroom'),
        'tub': ('______', '|____|', '| |  |- Bathroom', '|_|___/'),
        'hallway': ('._ Bedroom', '| _____', '| |   |\_ Stairs', '| |   |', '|_ \  |', '  |   |', '  |   |', '    |_ Playroom'),
        'playroom': ('    ._ Hallway', '___ | ___', '|__  ~  |', '| |   @ |', '|_|    *|', '|_______|'),
        'stairs': (' ._ Living Room', '_|_', '|-|', '|-|', '|-|', '|-|', '|-|', ' |_ Hallway'),

        # Bottom floor
        'living room' : ('         ._ Front Door', '_________|_________', '|      o  =   |___|', '|      ___        |', '|---|  |o|        |', '|---|  |o| O       \ - Kitchen', '|---|  |_|        |', '|---|________   __|', '  |_ Stairs   |_ Dining Room'),
        'dining room' : ('    ._ Living Room', '    |      ._ Kitchen', '___ | ____ | __', '|      o      |', '|  __o____    |', '| o|_____|o   |', '|    o o      \- Backyard', '|_____________|'),
        'kitchen': ('  _________', '  |__|__. |', '  |     | |', '  |     |%|', '._\     | |', '| |     |0|','| |__   |_|', '|    |_ Dining Room', '|_ Living Room'),
    
        # Outside
        'backyard' : ('     ________', '  .__|      |', '  |         |', '  |         |- Fence', '  |         |', '.-\         |', '| |  ___\__ |', '| |  |    | |', '| |__|____|_|', '|      |_ Shed', '|_ Dining Room'),
        'fence' : ('      ._ Backyard', '   ___|____', '.__|      |', '|         |', '|         |', '|         |', '\         |', '|  ___\__ |', '|  |    | |', '|__|____|_|', '    |_ Shed'),
        'shed' : ('  ._ Firewood', '  | ._ Backyard', ' _|_\__', ' |==  |', ' |___#|', ' |____|', '    |_ Tools'),
        'tools' : ('_|_\__', '|==  |_ Shed', '|___#|', '|____|'),
        'tools' : ('_|_\__', '|==  |_ Shed', '|___#|', '|____|'),

        # Final Location
        'front door': ()
    }
