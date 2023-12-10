import subprocess
import keyboard
import time

def turn_off_ethernet():
    subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "admin=disable"])
    print("Ethernet turned off.")

def turn_on_ethernet():
    subprocess.run(["netsh", "interface", "set", "interface", "Ethernet", "admin=enable"])
    print("Ethernet turned on.")

def exit_app():
    exit

def on_f1(event):
    turn_on_ethernet()
    print("Ethernet turned on.")

def on_f2(event):
    turn_off_ethernet()
    print("Ethernet turned off.")

def on_f3(event):
    print("Quiting the script")
    exit_app()

keyboard.on_press_key("F1", on_f1, suppress=True)
keyboard.on_press_key("F2", on_f2, suppress=True)
keyboard.on_press_key("F3", on_f3)
keyboard.wait("F3")
keyboard.unhook_all()
