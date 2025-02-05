import tkinter as tk
import random
import time


class PigGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pig Game")
        self.root.configure(bg="#f0f0f0")
        self.root.geometry("400x300")

        self.scores = [0, 0]
        self.current_score = 0
        self.current_player = 0

        self.player_names = ["", "Computer"]
        self.computer_personality = None  # Личност на компютъра

        self.label_title = tk.Label(root, text="Pig Game", font=("Arial", 20), bg="#f0f0f0")
        self.label_title.pack()

        self.label_info = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.label_info.pack()

        self.label_scores = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
        self.label_scores.pack()

        self.label_current = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
        self.label_current.pack()

        self.btn_roll = tk.Button(root, text="Roll Dice", command=self.roll_dice, bg="#4CAF50", fg="white",
                                  state=tk.DISABLED)
        self.btn_roll.pack(pady=5)

        self.btn_hold = tk.Button(root, text="Hold", command=self.hold, bg="#2196F3", fg="white", state=tk.DISABLED)
        self.btn_hold.pack(pady=5)

        self.get_player_name()

    def get_player_name(self):
        """Позволява на играча да въведе своето име и избира характера на AI-то."""
        name_window = tk.Toplevel(self.root)
        name_window.title("Enter Player Name & AI Type")
        name_window.geometry("300x200")
        name_window.configure(bg="#f0f0f0")

        tk.Label(name_window, text="Enter Your Name:", bg="#f0f0f0").pack()
        entry_p1 = tk.Entry(name_window)
        entry_p1.pack()

        tk.Label(name_window, text="Choose COM Personality:", bg="#f0f0f0").pack()
        personality_var = tk.StringVar(value="Balanced")

        personalities = ["Risky", "Cautious", "Balanced"]
        for p in personalities:
            tk.Radiobutton(name_window, text=p, variable=personality_var, value=p, bg="#f0f0f0").pack()

        def save_settings():
            self.player_names[0] = entry_p1.get().strip() or "Player 1"
            self.computer_personality = personality_var.get()
            self.label_info.config(text=f"{self.player_names[0]}'s turn")
            self.label_scores.config(text=self.get_scores_text())
            self.label_current.config(text=f"Current Round Points: {self.current_score}")
            self.btn_roll.config(state=tk.NORMAL)
            self.btn_hold.config(state=tk.NORMAL)
            name_window.destroy()

        tk.Button(name_window, text="Start", command=save_settings, bg="#4CAF50", fg="white").pack(pady=5)

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.label_info.config(text=f"{self.player_names[self.current_player]} rolled {roll}")

        if roll == 1:
            self.current_score = 0
            self.switch_player()
        else:
            self.current_score += roll

        self.update_display()

        if self.player_names[self.current_player] == "Computer":
            self.root.after(1000, self.computer_turn)

    def hold(self):
        self.scores[self.current_player] += self.current_score
        self.current_score = 0
        if self.check_winner():
            return
        self.switch_player()
        self.update_display()

        if self.player_names[self.current_player] == "Computer":
            self.root.after(1000, self.computer_turn)

    def computer_turn(self):
        self.label_info.config(text=f"Computer ({self.computer_personality}) is thinking...")

        if self.computer_personality == "Risky":
            threshold = random.randint(18, 25)  # Поема риск, ще хвърля повече
        elif self.computer_personality == "Cautious":
            threshold = random.randint(8, 14)  # Играе предпазливо, задържа по-рано
        else:
            threshold = random.randint(12, 18)  # Среден баланс между риск и предпазливост

        while self.current_player == 1 and self.current_score < threshold:
            self.root.update()
            time.sleep(1)
            roll = random.randint(1, 6)
            self.label_info.config(text=f"Computer rolled {roll}")
            self.root.update()

            if roll == 1:
                self.current_score = 0
                break
            else:
                self.current_score += roll

            if self.scores[1] + self.current_score >= 100:
                break

        self.hold()

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_winner(self):
        if self.scores[0] >= 100:
            self.label_info.config(text=f"{self.player_names[0]} wins the game! 🏆")
            self.disable_buttons()
            return True
        elif self.scores[1] >= 100:
            self.label_info.config(text=f"Computer ({self.computer_personality}) wins the game! 🏆")
            self.disable_buttons()
            return True
        return False

    def update_display(self):
        self.label_scores.config(text=self.get_scores_text())
        self.label_current.config(text=f"Current Round Points: {self.current_score}")
        self.label_info.config(text=f"{self.player_names[self.current_player]}'s turn")

    def get_scores_text(self):
        return f"Scores - {self.player_names[0]}: {self.scores[0]}, Computer: {self.scores[1]}"

    def disable_buttons(self):
        self.btn_roll.config(state=tk.DISABLED)
        self.btn_hold.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = PigGameGUI(root)
    root.mainloop()
