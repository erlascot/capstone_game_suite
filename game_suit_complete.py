import tkinter as tk, random


def game_suit_gui():
    """Program for the game selection screen"""

    # Launch Hangman upon button press
    def HM():
        window.destroy()
        hangman_gui()

    # Launch Tic Tac Toe upon button press
    def TTT():
        window.destroy()
        tictactoe_gui()

    # Launch Rock, Paper, Scissor upon button press
    def RPS():
        window.destroy()
        rock_paper_scissor_gui()

    # Launch Number Guesser upon button press
    def NG():
        window.destroy()
        number_guesser_gui()

    # Create the main window
    window = tk.Tk()
    window.title("Game Suit")
    frame = tk.Frame(master=window)

    # Create the heading label
    heading = tk.Label(text="Choose A Game", font=("Arial", 25))

    # Create the button for Hangman
    btn_HM = tk.Button(
        text="Hangman",
        master=frame,
        relief=tk.RAISED,
        borderwidth=5,
        width=20,
        height=5,
        command=HM,
    )

    # Create the button for Tic Tac Toe
    btn_TTT = tk.Button(
        text="Tic Tac Toe\n(requires 2 players)",
        master=frame,
        relief=tk.RAISED,
        borderwidth=5,
        width=20,
        height=5,
        command=TTT,
    )

    # Create the button for Rock, Paper, Scissor
    btn_RPS = tk.Button(
        text="Rock, Paper, Scissors",
        master=frame,
        relief=tk.RAISED,
        borderwidth=5,
        width=20,
        height=5,
        command=RPS,
    )

    # Create the button for Number Guesser
    btn_NG = tk.Button(
        text="Number Guesser",
        master=frame,
        relief=tk.RAISED,
        borderwidth=5,
        width=20,
        height=5,
        command=NG,
    )

    # Place the heading and buttons into the window grid
    heading.grid(row=0)
    frame.grid(row=1)
    btn_HM.grid(row=1, column=0)
    btn_TTT.grid(row=1, column=1)
    btn_RPS.grid(row=2, column=0)
    btn_NG.grid(row=2, column=1)

    window.mainloop()


def tictactoe_gui():
    """Program for the game Tic Tac Toe"""

    # Designate starting player.
    global player
    player = "X"

    def check_game_over():
        """Checks the condition of the board to determ in game is over or should continue."""

        # Check for a win.
        if (
            (button_0["text"] == button_1["text"] == button_2["text"])
            or (button_3["text"] == button_4["text"] == button_5["text"])
            or (button_6["text"] == button_7["text"] == button_8["text"])
            or (button_0["text"] == button_3["text"] == button_6["text"])
            or (button_1["text"] == button_4["text"] == button_7["text"])
            or (button_2["text"] == button_5["text"] == button_8["text"])
            or (button_0["text"] == button_4["text"] == button_8["text"])
            or (button_2["text"] == button_4["text"] == button_6["text"])
        ):
            game_over()

        # Check for a tie.
        elif (
            (button_0["text"] == "X" or button_0["text"] == "O")
            and (button_1["text"] == "X" or button_1["text"] == "O")
            and (button_2["text"] == "X" or button_2["text"] == "O")
            and (button_3["text"] == "X" or button_3["text"] == "O")
            and (button_4["text"] == "X" or button_4["text"] == "O")
            and (button_5["text"] == "X" or button_5["text"] == "O")
            and (button_6["text"] == "X" or button_6["text"] == "O")
            and (button_7["text"] == "X" or button_7["text"] == "O")
            and (button_8["text"] == "X" or button_8["text"] == "O")
        ):
            game_tie()

        # If neither condition is met continue play.
        else:
            pass

    def click_0():
        """Processes a click of button_0"""
        if button_0["text"] == "":
            global player
            button_0["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_1():
        """Processes a click of button_1"""
        if button_1["text"] == " ":
            global player
            button_1["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_2():
        """Processes a click of button_2"""
        if button_2["text"] == "  ":
            global player
            button_2["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_3():
        """Processes a click of button_3"""
        if button_3["text"] == "   ":
            global player
            button_3["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_4():
        """Processes a click of button_4"""
        if button_4["text"] == "    ":
            global player
            button_4["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_5():
        """Processes a click of button_5"""
        if button_5["text"] == "   ":
            global player
            button_5["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_6():
        """Processes a click of button_6"""
        if button_6["text"] == "  ":
            global player
            button_6["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_7():
        """Processes a click of button_7"""
        if button_7["text"] == " ":
            global player
            button_7["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def click_8():
        """Processes a click of button_8"""
        if button_8["text"] == "":
            global player
            button_8["text"] = player
            if not check_game_over():
                player = "O" if player == "X" else "X"
                message_center["text"] = f"{player}'s Turn"
        else:
            message_center[
                "text"
            ] = "Square is taken.\nPlease select a different position."

    def game_over():
        """Define what to do when someone wins."""
        # Destroy the game board and message center.
        frame_game_board.destroy()
        message_center.destroy()

        # Reconfigure the window to properly display new content.
        window.columnconfigure([0, 1, 2], minsize=150, weight=1)

        # Create new message and button widgets for post game.
        msg_win = tk.Label(text=player + " WINS!", master=window, font=("Arial", 25))
        btn_replay = tk.Button(text="Play Again?", master=window, command=replay)
        btn_return = tk.Button(
            text="Return to game selection", master=window, command=game_select
        )

        # Assign the message and button widgets to window.
        msg_win.grid(row=0, column=1, pady=15)
        btn_replay.grid(row=0, column=0, padx=10)
        btn_return.grid(row=0, column=2, padx=10)

    def game_tie():
        """Define what to do when the game ends in a tie."""
        # Destroy the game board and message center.
        frame_game_board.destroy()
        message_center.destroy()

        # Reconfigue the window to properly display new content.
        window.columnconfigure([0, 1, 2], minsize=150, weight=1)

        # Create new message and button widgets for post game.
        msg_tie = tk.Label(text="It's a TIE!", master=window, font=("Arial", 25))
        btn_replay = tk.Button(text="Play Again?", master=window, command=replay)
        btn_return = tk.Button(
            text="Return to game selection", master=window, command=game_select
        )

        # Assign the widgets to window.
        msg_tie.grid(row=0, column=1, pady=15)
        btn_replay.grid(row=0, column=0, padx=10)
        btn_return.grid(row=0, column=2, padx=10)

    # Define post game buttons.
    def replay():
        window.destroy()
        tictactoe_gui()

    def game_select():
        window.destroy()
        game_suit_gui()

    # Creates the game window.
    window = tk.Tk()
    window.title("Tic Tac Toe")
    frame_game_board = tk.Frame(master=window)

    # Creates the button widgets used as the game board with variable text spacing to allow for win condition checks.
    button_0 = tk.Button(
        text="", master=frame_game_board, width=5, height=2, command=click_0
    )
    button_1 = tk.Button(
        text=" ", master=frame_game_board, width=5, height=2, command=click_1
    )
    button_2 = tk.Button(
        text="  ", master=frame_game_board, width=5, height=2, command=click_2
    )
    button_3 = tk.Button(
        text="   ", master=frame_game_board, width=5, height=2, command=click_3
    )
    button_4 = tk.Button(
        text="    ", master=frame_game_board, width=5, height=2, command=click_4
    )
    button_5 = tk.Button(
        text="   ", master=frame_game_board, width=5, height=2, command=click_5
    )
    button_6 = tk.Button(
        text="  ", master=frame_game_board, width=5, height=2, command=click_6
    )
    button_7 = tk.Button(
        text=" ", master=frame_game_board, width=5, height=2, command=click_7
    )
    button_8 = tk.Button(
        text="", master=frame_game_board, width=5, height=2, command=click_8
    )

    # Create the message center widget.
    message_center = tk.Label(
        text=player + "'s Turn", master=window, width=40, height=2
    )

    # Assigns all widgets to window to create the game board.
    frame_game_board.grid()
    button_0.grid(row=0, column=0, sticky="nsew")
    button_1.grid(row=0, column=1, sticky="nsew")
    button_2.grid(row=0, column=2, sticky="nsew")
    button_3.grid(row=1, column=0, sticky="nsew")
    button_4.grid(row=1, column=1, sticky="nsew")
    button_5.grid(row=1, column=2, sticky="nsew")
    button_6.grid(row=2, column=0, sticky="nsew")
    button_7.grid(row=2, column=1, sticky="nsew")
    button_8.grid(row=2, column=2, sticky="nsew")
    message_center.grid(row=3)

    window.mainloop()


def rock_paper_scissor_gui():
    """Program for the game Rock Paper Scissors"""

    def cpu_throw(opponent):
        """Use Random module to select CPU choice."""
        throw = random.randint(1, 3)
        if throw == 1:
            opponent = "ROCK"
        if throw == 2:
            opponent = "PAPER"
        if throw == 3:
            opponent = "SCISSOR"
        return opponent

    def game_over(player, opponent):
        """Check CPU choice agaist players choice and determine winner. If tie, play again automatically."""
        if opponent == "ROCK" and player == "PAPER":
            message_center["text"] = (
                "OPPONENT PLAYS "
                + opponent
                + "\nYOU WIN! To Play Again, Select New Throw"
            )
        elif opponent == "PAPER" and player == "SCISSOR":
            message_center["text"] = (
                "OPPONENT PLAYS "
                + opponent
                + "\nYOU WIN! To Play Again, Select New Throw"
            )
        elif opponent == "SCISSOR" and player == "ROCK":
            message_center["text"] = (
                "OPPONENT PLAYS "
                + opponent
                + "\nYOU WIN! To Play Again, Select New Throw"
            )
        elif opponent == player:
            message_center["text"] = (
                "OPPONENT PLAYS " + opponent + "\nTIE! Select Again!"
            )
        else:
            message_center["text"] = (
                "OPPONENT PLAYS "
                + opponent
                + "\nYOU LOSE. To Try Again, Select New Throw"
            )

    # Define button commands
    def rock():
        player = "ROCK"
        game_over(player, cpu_throw(""))

    def paper():
        player = "PAPER"
        game_over(player, cpu_throw(""))

    def scissor():
        player = "SCISSOR"
        game_over(player, cpu_throw(""))

    def game_select():
        window.destroy()
        game_suit_gui()

    # Create the widgets for the gui
    window = tk.Tk()
    window.title("Rock, Paper, Scissors!")
    frame1 = tk.Frame(master=window)
    frame2 = tk.Frame(master=window)
    img_rock = tk.PhotoImage(file="rock.png")
    img_paper = tk.PhotoImage(file="paper.png")
    img_scissor = tk.PhotoImage(file="scissor.png")
    btn_rock = tk.Button(
        master=frame1, text="rock", image=img_rock, relief="flat", command=rock
    )
    btn_paper = tk.Button(
        master=frame2, text="paper", image=img_paper, relief="flat", command=paper
    )
    btn_scissor = tk.Button(
        master=frame2, text="scissor", image=img_scissor, relief="flat", command=scissor
    )
    message_center = tk.Label(
        master=window, text="What do you throw?\n", font=("Arial", 20)
    )
    btn_game_sel = tk.Button(
        master=window, text="Return to Game Selection", command=game_select
    )

    # Place the widgets within the window
    frame1.grid(row=0)
    frame2.grid(row=1)
    btn_rock.grid(row=0, pady=5)
    btn_paper.grid(row=1, column=0, padx=10, pady=5)
    btn_scissor.grid(row=1, column=1, padx=10, pady=5)
    message_center.grid(row=2, pady=5)
    btn_game_sel.grid(row=3)

    window.mainloop()


def number_guesser_gui():
    """Program for the game Number Guesser"""

    # Reset global variables for new game
    global guess_counter
    global rnd_number
    guess_counter = 1
    rnd_number = 0

    def submit_max():
        """Command for when the submit button is pressed while deciding maximum number range"""
        try:
            global rnd_number
            # Obtain and convert users input for maximum range to an integer.
            max_number = user_entry.get()

            # Randomly generate an integer between 1 and users maximum range.
            rnd_number = random.randint(1, int(max_number))

            # Change the message_center widget text.
            message_center["text"] = "What is your first guess?"

            # Clear the entry field of all text.
            user_entry.delete(0, "end")

            # Swap the submit button to allow multiple commands. Should not be visible to user.
            btn_submit_max.grid_forget()
            btn_submit_guess.grid(row=2, column=1)

        # Instruct user to enter an integer if program fails.
        except Exception as e:
            # Prints error in the event program failed for reasons other than user input.
            print(e)
            message_center["text"] = "Please enter a whole number"
            user_entry.delete(0, "end")

    def submit_guess():
        """Command for when the submit button is pressed while guessing"""
        try:
            global guess_counter
            # Obtain and convert users guess to integer.
            guess = int(user_entry.get())

            # Check if the users guess is the same as the random number.
            if guess == rnd_number:
                message_center[
                    "text"
                ] = f"Congratulations! It took you\n{str(guess_counter)}\nattempts to guess the number!"

                # Create the post game widgets.
                replay_message = tk.Label(
                    text="Would you like to play again?", font=("Arial", 15)
                )
                btn_yes = tk.Button(text="REPLAY", command=replay)
                btn_return = tk.Button(
                    text="Return to game selection", command=game_select
                )
                btn_no = tk.Button(text="EXIT", command=close)

                # Forget the widgets used during gameplay.
                user_entry.grid_forget()
                btn_submit_guess.grid_forget()

                # Assign the post game widgets.
                replay_message.grid(row=1, column=1)
                btn_yes.grid(row=2, column=0)
                btn_return.grid(row=2, column=1)
                btn_no.grid(row=2, column=2)

            # Check if the users guess is smaller then the random number and provide feedback to user.
            elif guess < rnd_number:
                message_center["text"] = "My number is higher. Try again."
                user_entry.delete(0, "end")
                guess_counter += 1

            # Check if the users guess is larger then the random number and provide feedback to user.
            elif guess > rnd_number:
                message_center["text"] = "My number is lower. Try again."
                user_entry.delete(0, "end")
                guess_counter += 1

        # Instruct user to enter an integer if program fails.
        except Exception as e:
            # Prints error in the event program failed for reasons other than user input.
            print(e)
            # Notifies user of incorrect input.
            message_center["text"] = "Please enter a whole number"
            # Clears the entry widget.
            user_entry.delete(0, "end")

    # Define post game buttons.
    def replay():
        window.destroy()
        number_guesser_gui()

    def game_select():
        window.destroy()
        game_suit_gui()

    def close():
        window.destroy()

    # Create the main window for the user interface.
    window = tk.Tk()
    window.title("Number Guesser")
    window.geometry("600x300")
    window.rowconfigure([0, 1, 2], minsize=100, weight=1)
    window.columnconfigure([0, 1, 2], weight=1)

    # Create the widgets used in the program.
    message_center = tk.Label(
        text='Input the max range of possible numbers\nand click "Submit"',
        font=("Arial", 20),
    )
    user_entry = tk.Entry(justify="center")
    btn_submit_max = tk.Button(text="Submit", command=submit_max)
    btn_submit_guess = tk.Button(text="Submit", command=submit_guess)

    # Assign the widgets to the window.
    message_center.grid(row=0, column=1)
    user_entry.grid(row=1, column=1)
    btn_submit_max.grid(row=2, column=1)

    window.mainloop()


def hangman_gui():
    """Program for the game Hangman"""

    # Create Global variables used between the functions.
    global hanged_man
    global correct_guess
    global word_len_int
    global word_list
    global letters
    global list_guessed_letters

    hanged_man = 0
    correct_guess = 0
    word_len_int = 0
    word_list = []
    letters = []
    list_guessed_letters = []

    def sub_word_len():
        """Defines command for the submit button used when selecting the length of the word"""

        word_len = ent_user.get()
        global word_list
        global word_len_int

        # Checks if user entered a number.
        if not word_len.isdigit():
            msg_ctr["text"] = "Please enter a number"
            ent_user.delete(0, "end")

        else:
            # Create dictionary of words from text file, keys == length of word, values == words of that length; all upper case.
            dict = {}
            with open("google-10000-english-usa.txt") as lib:
                for word in lib:
                    word = word.rstrip()
                    l = str(len(word))
                    if l not in dict:
                        dict[l] = [word.upper()]
                    dict[l].append(word.upper())

                # Convert word length from string to integer.
                word_len_int = int(word_len)

            # Checks if dictionary has a key == to user entry.
            if word_len_int > 16 or word_len_int < 1:
                msg_ctr["text"] = "Please select between 1 and 16"
                ent_user.delete(0, "end")

            # Adjusts the GUI to allow further gameplay.
            else:
                msg_ctr["text"] = "Guess a letter"
                ent_user.delete(0, "end")
                btn_submit_len.pack_forget()
                btn_submit_letter.pack()
                frame_word.pack()

                # Build a bank of possible words based on the desiered length.
                word_bank = dict[word_len]

                # Select a random word from the word bank.
                random_index = random.randint(0, len(word_bank))
                word = word_bank[random_index]

                # Convert word to a list of letters. Used to check user guesses.
                word_list = list(word)

                # Generates blank labels representing each letter of the word.
                for i in range(word_len_int):
                    letters.append(
                        tk.Label(
                            master=frame_word,
                            relief=tk.RAISED,
                            text=" ",
                            font=("Arial", 15),
                            padx=5,
                        )
                    )
                    letters[i].grid(row=1, column=i)

    def sub_letter():
        """Defines command for the submit button when user is guessing letters."""

        letter_guess = ent_user.get()

        # Sanity check if user entered a letter.
        if not letter_guess.isalpha():
            msg_ctr["text"] = "Please enter a letter"
            ent_user.delete(0, "end")

        # Sanity check if user entered a single letter.
        elif len(letter_guess) > 1:
            msg_ctr["text"] = "Please enter a single letter"
            ent_user.delete(0, "end")

        else:
            # Convert the user input to upper case.
            guess = letter_guess.upper()

            # Clear the entry box.
            ent_user.delete(0, "end")

            # Check if input was previously entered.
            if guess in list_guessed_letters:
                msg_ctr["text"] = "You already guessed that letter. Guess again."

            # Check if user's guess is in the word.
            elif guess in word_list:
                # Reveal the placement of the guessed letter in the word to the user.
                for i in range(len(word_list)):
                    if word_list[i] in guess:
                        letters[i].config(text=guess)

                        # Increment correct guess for game winning condition
                        global correct_guess
                        correct_guess += 1

                # Add guess to list of attempted letters and correct the message center if needed.
                list_guessed_letters.append(guess)
                msg_ctr["text"] = "Guess a letter"

                # Check if the entire word has been guessed and notify the user.
                if correct_guess == word_len_int:
                    msg_ctr["text"] = "You've saved the stickman!"
                    ent_user.pack_forget()
                    btn_submit_letter.pack_forget()
                    btn_replay.pack()
                    btn_game_sel.pack()

            # Increment hanged_man for incorrect guesses and notify user of how many attmpts they have left.
            else:
                global hanged_man
                list_guessed_letters.append(guess)
                hanged_man += 1
                msg_ctr["text"] = "Guess a letter"

                # Changes lbl_gallows image based on number of incorrect guesses
                if hanged_man == 1:
                    lbl_gallows["image"] = img_hgm1

                if hanged_man == 2:
                    lbl_gallows["image"] = img_hgm2

                if hanged_man == 3:
                    lbl_gallows["image"] = img_hgm3

                if hanged_man == 4:
                    lbl_gallows["image"] = img_hgm4

                if hanged_man == 5:
                    lbl_gallows["image"] = img_hgm5

                if hanged_man == 6:
                    lbl_gallows["image"] = img_hgm6

                    # End game with loss notification.
                    msg_ctr["text"] = "You lost, the word was"

                    # Reveal the word to user.
                    for i in range(word_len_int):
                        letters[i].config(text=word_list[i])

                    # Reconfigue GUI for post game options.
                    ent_user.pack_forget()
                    btn_submit_letter.pack_forget()
                    btn_replay.pack()
                    btn_game_sel.pack()

    # Define post game buttons.
    def replay():
        window.destroy()
        hangman_gui()

    def game_select():
        window.destroy()
        game_suit_gui()

    # Create Tkinter window
    window = tk.Tk()
    window.title("Hangman")
    window.geometry("450x525")
    frame_word = tk.Frame()

    # Create image files used in program.
    img_hgm0 = tk.PhotoImage(file="hangman0.png")
    img_hgm1 = tk.PhotoImage(file="hangman1.png")
    img_hgm2 = tk.PhotoImage(file="hangman2.png")
    img_hgm3 = tk.PhotoImage(file="hangman3.png")
    img_hgm4 = tk.PhotoImage(file="hangman4.png")
    img_hgm5 = tk.PhotoImage(file="hangman5.png")
    img_hgm6 = tk.PhotoImage(file="hangman6.png")

    # Create GUI elements.
    lbl_gallows = tk.Label(master=window, image=img_hgm0, relief="flat")
    msg_ctr = tk.Label(
        master=window, text="How long of a word would you like?", font=("Arial", 15)
    )
    ent_user = tk.Entry(justify="center")
    btn_submit_len = tk.Button(text="SUBMIT", command=sub_word_len)
    btn_submit_letter = tk.Button(text="SUBMIT", command=sub_letter)
    btn_replay = tk.Button(text="Play Again?", command=replay)
    btn_game_sel = tk.Button(text="Game Selection", command=game_select)

    # Pack GUI elements into window.
    lbl_gallows.pack()
    msg_ctr.pack()
    ent_user.pack()
    btn_submit_len.pack()

    window.mainloop()


game_suit_gui()
