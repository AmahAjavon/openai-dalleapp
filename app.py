from auth import auth_token
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import requests


import openai

openai.api_key = auth_token

app = tk.Tk()
app.geometry("532x632")
app.title("DALL-E Image Generator")
ctk.set_appearance_mode("dark")

main_image = tk.Canvas(app, width=512, height=512)
main_image.place(x=10, y=110)

prompt_input = ctk.CTkEntry(master=app,
    height=40,
    width=512,
    border_width=2,
    corner_radius=10,
    placeholder_text="Type in something cool",
)
prompt_input.place(x=10, y=10)


def generate_image():
    global tk_img
    global img

    prompt = prompt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=tk_img)

def save_image():
    prompt = prompt_input.get().replace(" ", "_")
    img.save(f"img/{prompt}.png")

# generate button
magic_button = ctk.CTkButton(master=app,
    height=32,
    width=120,
    text_color="white",
    fg_color=("white", "gray38"),
    corner_radius=8,
    text="CTkButton",
    command=generate_image,
)
magic_button.configure(text="Generate Image")
magic_button.place(x=133, y=60)

# save button
save_button = ctk.CTkButton(master=app,
    height=32,
    width=120,
    text_color="white",
    fg_color=("white", "gray38"),
    corner_radius=8,
    text="CTkButton",
    command=save_image,
)
save_button.configure(text="Save Image")
save_button.place(x=266, y=60)


app.mainloop()
