import random
from flask import Flask

rand_no=random.randint(0, 9)
print(f"random number={rand_no}")

app=Flask(__name__)
@app.route('/')
def home_page():
    return '<h1 style="text-align:center">Guess The Number between (0-9)</h1>' \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:choice>")
def user_input(choice):
    if choice> rand_no:
        return f"<h1 style='color:purple'>TOO HIGH try again</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
        
    elif choice< rand_no:
        return f"<h1 style='color:blue'>TOO LOW try again</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return f"<h1 style='color:blue'>You found me!</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
        
        







if __name__ =="__main__":
    app.run(debug=True)