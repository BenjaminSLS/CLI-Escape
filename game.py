# Import the dialog_options.py, locations.py, and key.py files as modules.
import gameplay_elements/locations, gameplay_elements/dialog_options.py, gameplay_elements/keys

# Import the OS module and refer to the exit() function from the sys module.
import os
from sys import exit

# CLI-Escape
def main(locations, dialog_options, keys):
    # The players location
    current_location = "bedroom"

    # Set locations to room.
    rooms = locations.location_text()

    # Get picture for the room.
    room_images = locations.location_images()
    
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
        # Clear the terminal after a user input.
        os.system(["clear", "cls"][os.name == "nt"])

        # Collect all of the available locations.
        location_choices = [room for room in rooms[current_location]]

        # Show player the unplayed dialog.
        if current_location in dialog and current_location not in played_dialog:
            location_dialog = [game_key for game_key in dialog[current_location]]

            for talk in location_dialog:
                next_line = input(talk + "\n")
                if next_line.lower() == "exit":
                    exit()
                os.system(["clear", "cls"][os.name == "nt"])
                
            if current_location == "front door" or current_location == "firewood":
                done = True
                break

            played_dialog.append(current_location)
        else:
            # Show user inventory once they collect the first item.
            if len(inventory) > 0:
                print(f"Inventory: {inventory}\n")

        # Print the current location.
        print(f"You are in the {current_location.capitalize()}\n")
        
        # Print all available locations.
        print("All Available Locations")
        for door_num, room in enumerate(location_choices, start=1):
            print(f"{door_num}. {room.capitalize()}")

        print("\nRoom Image")
        for i in room_images[current_location]:
            print(i)
        
        # Have the user select the next location.
        choice = input("\nChoose your next location: ").lower()
        
        # Exit program if user types exit.
        if choice == "exit":
            exit()
        
        # Try converting the answer to an integer if need be and pass if it is not.
        try:
            choice_number = int(choice)
        except (ValueError, IndexError):
            pass
        else:
            if 1 <= choice_number <= len(location_choices):
                choice = location_choices[choice_number - 1]
            else:
                prompt_again = input(f"{choice_number} is not an available location.\n")
                if prompt_again.lower() == "exit":
                    exit()
                continue
        
        # Detect if a location is available to move to.
        if choice in location_choices:
            os.system(["clear", "cls"][os.name == "nt"])
            if choice in locked_doors and locked_doors[choice] not in inventory:
                return_to_room = input(f"{choice} is locked.\n")
                if return_to_room.lower() == "exit":
                    exit()
            else:
                if choice in key_locations and key_locations[choice] not in inventory:
                    new_key = key_locations[choice]
                    inventory.append(new_key)
                    accept_key = input(f"You found the {new_key} key!\n")
                    if accept_key.lower() == "exit":
                        exit()
                current_location = choice
        else:            
            prompt_again = input(f"{choice} is not an availalbe location.")
            if prompt_again.lower() == "exit":
                exit()
    
    # Ending statement.
    print("Thanks for playing my CLI adventure game!")

# Invoke the main() function.
main(locations, dialog_options, keys)
