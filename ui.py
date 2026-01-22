import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import *
import sv_ttk, pywinstyles, sys, darkdetect

uds_path = None

root = tk.Tk()
root.title("UDS Configurator")
root.geometry("600x500")
root.resizable(False, False)
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
center_window(root)

def uds_save_reset(*a):
    uds_save_options.config(text="Save")

version = sys.getwindowsversion()
if version.major == 10 and version.build >= 22000:
    if darkdetect.theme() == "Dark":
        pywinstyles.change_header_color(root, "#1c1c1c")
    else:
        pywinstyles.change_header_color(root, "#fafafa")
elif version.major == 10:
    if darkdetect.theme() == "Dark":
        pywinstyles.apply_style(root, "dark")
    else:
        pywinstyles.apply_style(root, "light")
    root.wm_attributes("-alpha", 0.99)
    root.wm_attributes("-alpha", 1)

ttk.Label(root, text="Unturned Dedicated Server Configurator", font=("Bahnschrift", 18)).pack(pady=20)

ttk.Label(root, text="Unturned Dedicated Server Path:", font=("Bahnschrift Light", 12)).pack(pady=8)
def uds_choose_folder():
    uds_folder_path = filedialog.askdirectory()
    if uds_folder_path:
        file = f"{uds_folder_path}\Servers\Default\Server\Commands.dat"
        try:
            with open(file, "r") as file:
                uds_choose_button.config(text=f"{uds_folder_path}")
                global uds_path
                uds_path = f"{uds_folder_path}"
                uds_save_reset()
        except FileNotFoundError:
            uds_choose_button.config(text="This folder does not contain \Servers\Default\Server\Commands.dat file!")
uds_choose_button = ttk.Button(root, text="Choose Folder", command=uds_choose_folder)
uds_choose_button.pack()

ttk.Label(root, text="———————————————— Server Options: ————————————————", font=("Bahnschrift", 12)).pack(pady=40)

#lo1
lo1_x = 0.25
label_x = lo1_x-0.085
other_x = lo1_x+0.11
other_width = 120
all_padding = 0.1
    # Choose Difficulty
y = 0.46
difficulty_optionMenu_selected_option = tk.StringVar(root)
difficulty_optionMenu_options = ["", "Easy", "Normal", "Hard"]
difficulty_optionMenu_selected_option.set(difficulty_optionMenu_options[1])
difficulty_optionMenu_option_menu = ttk.OptionMenu(root, difficulty_optionMenu_selected_option, *difficulty_optionMenu_options, command=uds_save_reset)
difficulty_optionMenu_option_menu.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Difficulty:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
    # Choose Map
y = y + all_padding
map_optionMenu_selected_option = tk.StringVar(root)
map_optionMenu_options = ["", "Germany", "PEI", "Russia", "Washington", "Yukon"]
map_optionMenu_selected_option.set(map_optionMenu_options[1])
map_optionMenu_option_menu = ttk.OptionMenu(root, map_optionMenu_selected_option, *map_optionMenu_options, command=uds_save_reset)
map_optionMenu_option_menu.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Map:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
    # Choose Perspective
y = y + all_padding
perspective_optionMenu_selected_option = tk.StringVar(root)
perspective_optionMenu_options = ["", "First", "Third", "Both"]
perspective_optionMenu_selected_option.set(perspective_optionMenu_options[3])
perspective_optionMenu_option_menu = ttk.OptionMenu(root, perspective_optionMenu_selected_option, *perspective_optionMenu_options, command=uds_save_reset)
perspective_optionMenu_option_menu.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Perspective:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
    # Change MaxPlayers
y = y + all_padding
maxPlayers_spinbox_value = tk.IntVar(value=4)
maxPlayers_spinbox = ttk.Spinbox(root, state="readonly", from_=1, to=32, justify="center", font=("Bahnschrift Light", 12), textvariable=maxPlayers_spinbox_value, command=uds_save_reset)
maxPlayers_spinbox.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Max Players:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)

#lo2
lo2_x = 0.75
label_x = lo2_x-0.085
other_x = lo2_x+0.11
other_width = 120
all_padding = 0.1
    # Enable PvE
y = 0.46
PvE = False
def changePvEmode():
    uds_save_reset()
    global PvE
    if PvE is False:
        PvE = True
        pve_button.config(text="Enabled")
    else:
        PvE = False
        pve_button.config(text="Disabled")
pve_button = ttk.Button(root, text="Disabled", command=changePvEmode)
pve_button.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="PvE:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
    # Change Password
y = y + all_padding
def validate(P):
    uds_save_reset()
    max_len = 12
    if len(P) <= max_len and " " not in P and " " not in P:
        return True
    else:
        return False
vcmd = (root.register(validate), "%P")
password_text = ttk.Entry(root, validate="key", validatecommand=vcmd, font=("Bahnschrift Light", 12))
password_text.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Password:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Empty = Disabled", font=("Bahnschrift Light", 8), foreground="gray").place(relx=label_x, rely=y+0.035, anchor=tk.CENTER)
    # Change MaxPing (Timeout)
y = y + all_padding
maxPing_spinbox_value = tk.IntVar(value=0)
maxPing_spinbox = ttk.Spinbox(root, increment=10, state="readonly", from_=0, to=1000, justify="center", font=("Bahnschrift Light", 12), textvariable=maxPing_spinbox_value, command=uds_save_reset)
maxPing_spinbox.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Max Ping:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="0 = Disabled", font=("Bahnschrift Light", 8), foreground="gray").place(relx=label_x, rely=y+0.035, anchor=tk.CENTER)
    # Change Owner
y = y + all_padding
def validate(P):
    uds_save_reset()
    if P.isdigit() or P == "":
        return True
    else:
        return False
vcmd = (root.register(validate), "%P")
owner_text = ttk.Entry(root, validate="key", validatecommand=vcmd, font=("Bahnschrift Light", 12))
owner_text.place(width=other_width, relx=other_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Owner:", font=("Bahnschrift Light", 12)).place(relx=label_x, rely=y, anchor=tk.CENTER)
ttk.Label(root, text="Empty = Disabled", font=("Bahnschrift Light", 8), foreground="gray").place(relx=label_x, rely=y+0.035, anchor=tk.CENTER)

# Change Theme
if darkdetect.theme() == "Light":
    themeText = "☀"
elif darkdetect.theme() == "Dark":
    themeText = "☾"

def change_theme():
    version = sys.getwindowsversion()
    if sv_ttk.get_theme() == "light":
        sv_ttk.set_theme("dark")
        changeTheme.config(text="☾")

        if version.major == 10 and version.build >= 22000:
            pywinstyles.change_header_color(root, "#1c1c1c")
        elif version.major == 10:
            pywinstyles.apply_style(root, "dark")
            root.wm_attributes("-alpha", 0.99)
            root.wm_attributes("-alpha", 1)

    elif sv_ttk.get_theme() == "dark":
        sv_ttk.set_theme("light")
        changeTheme.config(text="☀")

        if version.major == 10 and version.build >= 22000:
            pywinstyles.change_header_color(root, "#fafafa")
        elif version.major == 10:
            pywinstyles.apply_style(root, "light")
            root.wm_attributes("-alpha", 0.99)
            root.wm_attributes("-alpha", 1)

changeTheme = ttk.Button(root, text=themeText, command=change_theme)
changeTheme.place(relx=0.075, rely=0.95, anchor=tk.CENTER)

# Server Options Info
def serverOptionsInfo():
    inf = tk.Toplevel(root)
    inf.transient(root)
    inf.title("UDS Parameters Info")
    inf.geometry("700x350")
    inf.resizable(False, False)
    inf.grab_set()
    inf.focus_force()
    version = sys.getwindowsversion()
    if version.major == 10 and version.build >= 22000:
        if darkdetect.theme() == "Dark":
            pywinstyles.change_header_color(inf, "#1c1c1c")
        else:
            pywinstyles.change_header_color(inf, "#fafafa")
    elif version.major == 10:
        if darkdetect.theme() == "Dark":
            pywinstyles.apply_style(inf, "dark")
        else:
            pywinstyles.apply_style(inf, "light")
        inf.wm_attributes("-alpha", 0.99)
        inf.wm_attributes("-alpha", 1)
    ttk.Label(inf, text="Parameters Information", font=("Bahnschrift", 18)).pack(pady=30)
    ttk.Label(inf, text="Difficulty: Sets server difficulty.", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="Map: Sets server map.", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="Perspective: Sets allowed perspective (First-Person, Third-Person and Both).", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="Max Players: Sets server maximum player capacity.", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="PvE: Enables PvE mode (basically, disabling PvP).", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="Password: Sets server password.", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="Max Ping: Server will timeout (kick) players that reached this treshhold.", font=("Bahnschrift Light", 12)).pack(pady=5)
    ttk.Label(inf, text="Owner (SteamID): Sets server owner. Owner will get OP (admin priviliges) on server.", font=("Bahnschrift Light", 12)).pack(pady=5)

serverOptionsInfo_button = ttk.Button(root, text="🛈", command=serverOptionsInfo)
serverOptionsInfo_button.place(relx=0.925, rely=0.95, anchor=tk.CENTER)

# Edit & Save UDS files
def save_options():
    if uds_path is None:
        uds_save_options.config(text="UDS Path not choosed!")
    else:
        file = f'{uds_path}\Servers\Default\Server\Commands.dat'
        difficulty = difficulty_optionMenu_selected_option.get()
        map = map_optionMenu_selected_option.get()
        perspective = perspective_optionMenu_selected_option.get()
        maxplayers = maxPlayers_spinbox.get()
        password = password_text.get()
        maxping = maxPing_spinbox.get()
        owner = owner_text.get()
        with open(file, "r+") as f:
            f.seek(0)
            f.truncate()
        with open(file, 'a') as f:
            f.write(f"mode {difficulty}\n")
            f.write(f"map {map}\n")
            f.write(f"perspective {perspective}\n")
            f.write(f"maxplayers {maxplayers}\n")
            if PvE is True:
                f.write(f"pve\n")
            if password != "":
                f.write(f"password {password}\n")
            if maxping != "0":
                f.write(f"timeout {maxping}\n")
            if owner != "":
                f.write(f"owner {owner}\n")
        uds_save_options.config(text="Saved!")

uds_save_options = ttk.Button(root, text="Save", command=save_options)
uds_save_options.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

ttk.Label(root, text="—————————————————————————————————————————", font=("Bahnschrift", 12)).place(relx=0.5, rely=0.89, anchor=tk.CENTER)

sv_ttk.set_theme(darkdetect.theme(), root)
root.mainloop()