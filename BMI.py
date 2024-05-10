import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)
window.config(padx=30, pady=30)

def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "" :
        result.config(text="enter both weight and height !!!")

    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            result.config(text=result_string)
        except:
            result.config(text="enter a valid number!")

#label

weight_label = tkinter.Label(text="enter your weight (kg):")
weight_label.pack()

#entry

weight_entry = tkinter.Entry(width=20)
weight_entry.pack()

#label_2

weight_label_2 = tkinter.Label(text="enter your height (cm):")
weight_label_2.pack()

#entry_2

height_entry = tkinter.Entry(width=20)
height_entry.pack()

calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

#label_3

result = tkinter.Label()
result.pack()

def write_result(bmi):
    result_string = f"Your BMI is : {round(bmi,2)}. You are " #round (yuvarlama)
    if bmi <= 16:
        result_string += "severely thin"
    elif 16 < bmi <= 17:
        result_string += "moderately thin"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin"
    elif 18.5 < bmi <= 25:
        result_string += "normal"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

window.mainloop()
