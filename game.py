# Import the dialog_options.py and locations.py files as modules.
import locations, dialog_options, keys

def main(locations, dialog_options, keys):
    # The players location
    current_location = "bedroom"

    # Set locations to room.
    rooms = locations.locations()
    
    # Pull dialog options.
    dialog = dialog_options.available_dialog()

    # All dialog the player has seen.
    played_dialog = dialog_options.played_dialog()

    # The players current collection of items.
    inventory = list()

    # Key locations.
    key_locations = keys.keys()

    # All locked doors.
    locked_doors = keys.locked_doors()

    # The games status.
    done = False

    # The game itself running under a while loop.
    while done == False:
        # Collect all of the available locations.
        location_choices = [room for room in rooms[current_location]]

        # Show user inventory once they collect the first item.
        if len(inventory) > 0:
            print(f"Inventory: {inventory}")

        # Show player the unplayed dialog.
        if current_location in dialog and current_location not in played_dialog:
            location_dialog = [game_key for game_key in dialog[current_location]]

            for talk in location_dialog:
                input(talk)

            if current_location == "front door" or current_location == "firewood":
                done = True
                break

            played_dialog.append(current_location)

        # Print all available locations.
        for door_num, room in enumerate(location_choices, start=1):
            print(f"{door_num}. {room.capitalize()}")

        # Have the user select the next location.
        choice = input("Choose your next location: ").lower()

        # Exit program if user types exit.
        if choice == "exit":
            sys.exit()
        
        # Try converting the answer to an integer if need be and pass if it is not.
        try:
            choice_number = int(choice)
        except (ValueError, IndexError):
            pass
        else:
            if 1 <= choice_number <= len(location_choices):
                choice = location_choices[choice_number - 1]
            else:
                print(f"{choice_number} is not an available location.")
                continue
        
        # Detect if a location is available to move to.
        if choice in locked_doors and locked_doors[choice] not in inventory:
            print(f"{choice} is locked.")
        elif choice in location_choices:
            if choice in key_locations and key_locations[choice] not in inventory:
                new_key = key_locations[choice]
                inventory.append(new_key)
                print(f"You found the {new_key} key!")
            current_location = choice
        else:
            print(f"{choice} is not an availalbe location.")

    # Ending statement.
    print("Thanks for playing my CLI adventure game!")

# Invoke the main() function.
main(locations, dialog_options, keys)
