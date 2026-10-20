
from pyscript import document, display

my_list = ["Sean Lee", "Matthew Saldana", "Deion Decierto", "Kaleb Villanueva","Dustin Decierto"]

def check_member(e):
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    full_name = first_name + " " + last_name

    result = full_name in my_list

    message = document.getElementById("message")

    if result:
        message.innerHTML = "Congratulations, " + full_name + "! You are now part of the Kaleb Club."
    else:
        message.innerHTML = "Sorry, " + full_name + ", your name is not on the list."
