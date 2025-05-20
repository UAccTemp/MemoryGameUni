import tkinter as tk
import random
import pygame.mixer

pygame.mixer.init()

class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Memory Game")
        
        self.last_clicked = None  # Track the last clicked button
        self.waiting_for_second = False  # Track if we're waiting for second card

        # Create list of paired numbers (1-8, each appearing twice)
        self.card_ids = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
        random.shuffle(self.card_ids)  # Randomize the order

        # Create sound mappings (add your sound files)
        self.sounds = {
            1: pygame.mixer.Sound("sounds/sound1.wav"),
            2: pygame.mixer.Sound("sounds/sound2.wav"),
            3: pygame.mixer.Sound("sounds/sound3.wav"),
            4: pygame.mixer.Sound("sounds/sound4.wav"),
            5: pygame.mixer.Sound("sounds/sound5.wav"),
            6: pygame.mixer.Sound("sounds/sound6.wav"),
            7: pygame.mixer.Sound("sounds/sound7.wav"),
            8: pygame.mixer.Sound("sounds/sound8.wav")
        }

        # Create buttons in a 4x4 grid
        self.buttons = []
        for row in range(4):
            for col in range(4):
                button = tk.Button(
                    self.window,
                    width=10,
                    height=5,
                    text="?",
                    command=lambda r=row, c=col: self.button_clicked(r, c)
                )
                # Assign the next random ID to this button
                button.card_id = self.card_ids.pop()
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)

        self.window.mainloop()

    def button_clicked(self, row, col):
        # Get the button's position in the grid
        button_index = row * 4 + col
        button = self.buttons[button_index]
        button["text"] = str(button.card_id)  # Show the card's ID
        #print(f"Button clicked at position ({row}, {col}) - Card ID: {button.card_id}")

        button["state"] = "disabled"  # Prevent clicking same button twice
        
        # Stop all currently playing sounds
        for sound in self.sounds.values():
            sound.stop()

        # Play the sound associated with this card
        self.sounds[button.card_id].play()

        if not self.waiting_for_second:
            # First card of pair
            self.last_clicked = button
            self.waiting_for_second = True
        else:
            # Second card of pair
            if button.card_id == self.last_clicked.card_id:
                print("Match found!")
                # Keep cards face up and disabled
            else:
                print("No match!")
                # Hide cards after a short delay
                self.window.after(1000, self.hide_cards, button, self.last_clicked)
            
            self.waiting_for_second = False
            self.last_clicked = None

    def hide_cards(self, card1, card2):
        card1["text"] = "?"
        card2["text"] = "?"
        card1["state"] = "normal"
        card2["state"] = "normal"


#if name.id == name.secondbuttonclicked.id: = true
#     # Check if the two clicked buttons match
#      if button.card_id == self.first_button.card_id:
#          print("It's a match!")
#      else:
#          print("Not a match.")
#

MyGUI()