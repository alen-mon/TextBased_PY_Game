from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, static_folder='img')
app.secret_key = 'name'

game_over = False
# Define the game logic
rooms = {
    'Darkroom': {
        'description': 'You are in a dark room.<br> There are two doors in front of you, one on the left and one on the right.',
        'doors': {'left': 'kitchen', 'right': 'living_room'}
    },
    'kitchen': {
        'description': 'You are in the kitchen.<br> There is an Oil on the table.<br> You can go back to the Darkroom (right).There is a bedroom on the (left) ',
        'items': ['oil'],
        'doors': {'right': 'Darkroom', 'left': 'bedroom'}
    },
    'living_room': {
        'description': 'You are in the living room. There is a TV and a remote control.<br> You can go back to the Darkroom (left) There is a locked wooden door on the right. (right).',
        'items': ['remote', 'tv'],
        'doors': {'left': 'Darkroom'}
    },
    'lockedRoom': {
        'description': 'You are in the unlocked room, search room for things that might help you with the puzzle.',
        'items': ['key'],
        'doors': {'left': 'living_room'}
    },
    'bedroom': {
        'description': 'You are in the bedroom.<br> There is a comfortable bed here and a locked chest.<br> You can go back to the living room (right).',
        'doors': {'right': 'kitchen'},
        'puzzle': {
            'description': 'A locked chest is in front of you. It seems to require a key to open.',
            'solved': False,
            'solution': 'use key',
            'absolution':'open chest',
            'success_message': '!!!!!You unlocked the chest and found a valuable treasure inside! Congratulations! You have found the key and won the game!!!!!!'
        }
    }
}

inventory = []
current_room = 'Darkroom'


# Function to handle player input
# Function to handle player input
def handle_input(action):
    global current_room, game_over  # Update current_room and game_over
    if action == 'quit':
        return "Game over. You quit the game. You Failed to find the Treasure"
    elif action == 'inventory':
        return "You are carrying: " + ', '.join(inventory)
    elif rooms[current_room]['doors'].get(action):
        if action == 'lockedRoom' and 'oil' not in inventory:
            return "The door to the locked room is jammed. You need oil to unlock it."
        current_room = rooms[current_room]['doors'][action]
        return rooms[current_room]['description']
    elif action == 'current room':
        return current_room
    elif action.startswith('take '):
        item_name = action[5:].lower()  # Convert item name to lowercase
        if 'items' in rooms[current_room]:
            # Convert all item names in the room to lowercase and check
            room_items = [item.lower() for item in rooms[current_room]['items']]
            if item_name in room_items:
                rooms[current_room]['items'].remove(room_items[room_items.index(item_name)])  # Remove lowercase item
                inventory.append(item_name)  # Append the original item name
                return "You have taken the " + item_name
        return "There is no " + item_name + " here."
    elif action == 'use oil' and current_room == 'living_room':
        if 'oil' in inventory:
            if 'lockedRoom' not in rooms[current_room]['doors']:
                rooms[current_room]['doors']['right'] = 'lockedRoom'
                #inventory.remove('oil')  # Remove the oil from inventory (used once)
                return "You used the oil to unlock the door. The door is now unlocked."
            else:
                return "The door is already unlocked."
        else:
            return "The door is jammed. You need oil to unlock it."
    elif current_room == 'living_room':
        if 'oil' not in inventory:
            return "The door is jammed. You need oil to unlock it."
        if action == 'right' and 'lockedRoom' not in rooms[current_room]['doors']:
            return "You need to use the oil first."
    elif action == 'search room' and current_room == 'lockedRoom':
        if 'key' not in inventory:
            return "Oooh there is a key here !!!!."
    elif current_room == 'bedroom' and not rooms['bedroom']['puzzle']['solved'] and action == \
            rooms['bedroom']['puzzle']['solution']:
        if 'key' in inventory :
            rooms['bedroom']['puzzle']['solved'] = True
            inventory.append('treasure')
            game_over = True

            return rooms['bedroom']['puzzle']['success_message']
        else:
            return "The treasure chest is locked . Seems like it needs something ...."
    elif current_room == 'bedroom' and not rooms['bedroom']['puzzle']['solved'] and action == \
            rooms['bedroom']['puzzle']['absolution']:
        if 'key' in inventory:
            rooms['bedroom']['puzzle']['solved'] = True
            inventory.append('treasure')
            game_over = True

            return rooms['bedroom']['puzzle']['success_message']
        else:
            return "The treasure chest is locked . Seems like it needs something ...."
    else:
        return "No Rooms here. Try again."


# Function to handle player input
def get_initial_description():
    print("Getting initial description")
    return "Welcome to the Text-Based Adventure Game! <br> You find yourself in a dark room.<br> There are two doors in front of you, one on the left and one on the right.<br> Solve the puzzle and find the treasure"


# Flask routes
@app.route('/', methods=['GET', 'POST'])
def index():
    global current_room, game_over
    if request.method == 'GET':
        message = get_initial_description()
    elif request.method == 'POST':
        if game_over:
            message = "Congratulations! You have already won the game."
        else:
            action = request.form['action'].strip().lower()
            message = handle_input(action)
    else:
        message = ""

    # Pass current_room, inventory, and game_over to the template
    return render_template('index.html', message=message, current_room=current_room, inventory=inventory, game_over=game_over)

@app.route('/restart', methods=['POST'])
def restart_game():
    global current_room, inventory, game_over
    current_room = 'Darkroom'
    inventory = []
    game_over = False
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
