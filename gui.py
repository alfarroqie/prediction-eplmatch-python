import tkinter as tk
import calculation as calculation
import utility as utils

from PIL import Image, ImageTk
from tkcalendar import Calendar

def display() :
    windows = tk.Tk()
    windows.geometry("600x680")

    deploy_component(windows)

    windows.mainloop()

def deploy_component(frame) :
    #define callback for change image (home team)
    def image_callback_home(var, indx, mode) :
        load = Image.open(utils.get_image_path(home_team_dropdown_var.get()))
        load = load.resize((200, 200))
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frame, image=render)
        img.image = render
        img.place(x=70, y= 160)

    #define callback for change image (away team)
    def image_callback_away(var, indx, mode) :
        load = Image.open(utils.get_image_path(away_team_dropdown_var.get()))
        load = load.resize((200, 200))
        render = ImageTk.PhotoImage(load)
        img = tk.Label(frame, image=render)
        img.image = render
        img.place(x=310, y= 160)

    #define callback for calculate
    def calculate():
        def dialog_box_close() :
            dialog_box.destroy()

        def result_frame_close() :
            result_frame.destroy()

        print(cal.get_date())
        if home_team_dropdown_var.get() == away_team_dropdown_var.get() :
            #when the team is same
            dialog_box = tk.Toplevel()
            dialog_box.geometry("350x115")

            ok_button = tk.Button(dialog_box, 
                                  text="OK", 
                                  command=dialog_box_close,
                                  height=2,
                                  width=7)
            
            message = tk.Label(dialog_box,
                               text="Please choose a different team",
                               font=("Helvetica", 14))
            
            print(utils.get_image_path("error"))
            loader = Image.open(utils.get_image_path("error"))
            loader = loader.resize((60, 50))
            err_img = ImageTk.PhotoImage(loader)
            err_label = tk.Label(dialog_box, image=err_img)
            err_label.image = err_img

            err_label.place(x=10, y=10)
            message.place(x=70, y=20)
            ok_button.place(x=155, y=55)
                
            dialog_box.mainloop()
        elif home_team_dropdown_var.get() == "Home Team" or away_team_dropdown_var.get() == "Away Team" :
            #when home and away is empty
            dialog_box = tk.Toplevel()
            dialog_box.geometry("350x115")

            message = tk.Label(dialog_box,
                                text="Team field cannot be empty",
                                font=("Helvetica", 14))

            ok_button = tk.Button(dialog_box, 
                                  text="OK", 
                                  command=dialog_box_close,
                                  height=2,
                                  width=7)
            
            loader = Image.open(utils.get_image_path("error"))
            loader = loader.resize((60, 50))
            err_img = ImageTk.PhotoImage(loader)
            err_label = tk.Label(dialog_box, image=err_img)
            err_label.image = err_img

            err_label.place(x=10, y=10)
            message.place(x=85, y=20)
            ok_button.place(x=155, y=55)
                
            dialog_box.mainloop()
        elif cal.get_date() == "" :
            #when date is not picked
            dialog_box = tk.Toplevel()
            dialog_box.geometry("350x115")

            message = tk.Label(dialog_box,
                                text="Date field cannot be empty",
                                font=("Helvetica", 14))

            ok_button = tk.Button(dialog_box, 
                                  text="OK", 
                                  command=dialog_box_close,
                                  height=2,
                                  width=7)
            
            loader = Image.open(utils.get_image_path("error"))
            loader = loader.resize((60, 50))
            err_img = ImageTk.PhotoImage(loader)
            err_label = tk.Label(dialog_box, image=err_img)
            err_label.image = err_img

            err_label.place(x=10, y=10)
            message.place(x=85, y=20)
            ok_button.place(x=155, y=55)
                
            dialog_box.mainloop()
        else :
            #do the calculation
            result_frame = tk.Toplevel()
            result_frame.geometry("350x330")
            
            home_team = home_team_dropdown_var.get()
            away_team = away_team_dropdown_var.get()
            date = cal.get_date()
            season = utils.get_season(date)

            utils.generate_data_for_calculation(home_team, away_team, utils.get_year(date))
            
            result = calculation.calculate(home_team, away_team, season)

            home_info = tk.Label(result_frame,
                                 text="Home Team : "+home_team,
                                 font=("Helvetica", 13))

            away_info = tk.Label(result_frame,
                                 text="Away Team : "+away_team,
                                 font=("Helvetica", 13))
                                
            date_info = tk.Label(result_frame,
                                 text="Date           : "+date,
                                 font=("Helvetica", 13))

            season_info = tk.Label(result_frame,
                                   text="Season       : "+season,
                                   font=("Helvetica", 13))

            result_info = tk.Label(result_frame,
                                   text="Result : ",
                                   font=("Helvetica", 15))

            home_win = tk.Label(result_frame,
                                text="Home Win   : "+str(result[0])+"%",
                                font=("Helvetica", 13))

            home_draw = tk.Label(result_frame,
                                text="Draw           : "+str(result[1])+"%",
                                font=("Helvetica", 13))

            home_lose = tk.Label(result_frame,
                                text="Home Lose  : "+str(result[2])+"%",
                                font=("Helvetica", 13))
            
            the_button = tk.Button(result_frame, 
                                  text="OK", 
                                  command=result_frame_close,
                                  height=2,
                                  width=7)

            #deployment
            home_info.place(x=20, y=20)
            away_info.place(x=20, y=50)
            date_info.place(x=20, y=80)
            season_info.place(x=20, y=110)
            result_info.place(x=20, y=150)
            home_win.place(x=20, y=180)
            home_draw.place(x=20, y=210)
            home_lose.place(x=20, y=240)
            the_button.place(x=140, y=280)
            result_frame.mainloop()

    #define the "Home Team" Label
    home_team_label = tk.Label(frame, 
                               text="Home Team",
                               font=("Helvetica", 15))
    
    #define the "Away Team" Label
    away_team_label = tk.Label(frame, 
                               text="Away Team",
                               font=("Helvetica", 15))

    #define the "Date" Label
    date_label = tk.Label(frame,
                          text="Date",
                          font=("Helvetiva", 16)) 

    #define the home team dropdown
    home_team_dropdown_var = tk.StringVar(frame)
    home_team_dropdown_var.set("Home Team")
    home_team_dropdown_var.trace('w', image_callback_home)
    home_team_dropdown = tk.OptionMenu(frame, home_team_dropdown_var, *utils.get_team_list())
    home_team_dropdown.config(width=25)

    #define the away team dropdown
    away_team_dropdown_var = tk.StringVar(frame)
    away_team_dropdown_var.set("Away Team")
    away_team_dropdown_var.trace('w', image_callback_away)
    away_team_dropdown = tk.OptionMenu(frame, away_team_dropdown_var, *utils.get_team_list())
    away_team_dropdown.config(width=25)

    #define the calendar
    cal = Calendar(frame, selectmode="day", date_pattern="dd/mm/yyyy", year=2019)
    
    #define the button
    calculate_button = tk.Button(frame, text="Calculate", command=calculate)

    #deploying the component
    home_team_label.place(x=120.0, y=50.0)
    away_team_label.place(x=350.0, y=50.0)
    date_label.place(x=270, y=370)
    home_team_dropdown.place(x=70, y=120)
    away_team_dropdown.place(x=310, y=120)
    cal.place(x=170, y=400)
    calculate_button.place(x=260, y=630)


        

