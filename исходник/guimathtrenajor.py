import data_time
import tkinter as tk
import data


class switchButton():
    global level

    level = 0

    def switchButtonState_1():
        global level
        but_1['state'] = tk.DISABLED
        but_2['state'] = tk.NORMAL
        but_3['state'] = tk.NORMAL
        but_4['state'] = tk.NORMAL
        but_start['state'] = tk.NORMAL
        level = 1

    def switchButtonState_2():
        global level
        but_1['state'] = tk.NORMAL
        but_2['state'] = tk.DISABLED
        but_3['state'] = tk.NORMAL
        but_4['state'] = tk.NORMAL
        but_start['state'] = tk.NORMAL
        level = 2

    def switchButtonState_3():
        global level
        but_1['state'] = tk.NORMAL
        but_2['state'] = tk.NORMAL
        but_3['state'] = tk.DISABLED
        but_4['state'] = tk.NORMAL
        but_start['state'] = tk.NORMAL
        level = 3

    def switchButtonState_4():
        global level
        but_1['state'] = tk.NORMAL
        but_2['state'] = tk.NORMAL
        but_3['state'] = tk.NORMAL
        but_4['state'] = tk.DISABLED
        but_start['state'] = tk.NORMAL
        level = 4

# Начало программы -----------------------------------------------------------------------


def settings():
    global root_s
    root_s = tk.Tk()
    root_s.title("Настройки")
    root_s.geometry("280x90+780+320")
    root_s.resizable(False, False)
    root_s.iconbitmap('data\\geek.ico')
    root_s.config(bg='#ffcc80')

    def quit():
        global root
        root_s.destroy()
        root_1.destroy()
        welcome()

    def stata():
        root_s.destroy()
        root_st = tk.Tk()
        root_st.title("Статистика")
        root_st.geometry("800x900+300+70")
        root_st.resizable(False, False)
        root_st.iconbitmap('data\\geek.ico')
        root_st.config(bg='#ffcc80')

        my_file_1 = open("data\\result_level1.txt")
        mf1 = my_file_1.readlines()

        my_file_2 = open("data\\result_level2.txt")
        mf2 = my_file_2.readlines()

        my_file_3 = open("data\\result_level3.txt")
        mf3 = my_file_3.readlines()

        my_file_4 = open("data\\result_level4.txt")
        mf4 = my_file_4.readlines()

        lab_lev1 = tk.Label(root_st, text="Лёгкий:",
                            font=("Comic Sans MS", 20),
                            bg='#b3ff61')
        lab_sum1 = tk.Label(root_st, text=f"Правильных ответов {mf1[0]}",
                            font=("Comic Sans MS", 20),
                            bg='#ffcc80')
        lab_sum_not1 = tk.Label(root_st, text=f"Не правильных ответов {mf1[1]}",
                                font=("Comic Sans MS", 20),
                                bg='#ffcc80')

        lab_lev2 = tk.Label(root_st, text="Нормальный:",
                            font=("Comic Sans MS", 20),
                            bg='#b3ff61')
        lab_sum2 = tk.Label(root_st, text=f"Правильных ответов {mf2[0]}",
                            font=("Comic Sans MS", 20),
                            bg='#ffcc80')
        lab_sum_not2 = tk.Label(root_st, text=f"Не правильных ответов {mf2[1]}",
                                font=("Comic Sans MS", 20),
                                bg='#ffcc80')

        lab_lev3 = tk.Label(root_st, text="Сложный:",
                            font=("Comic Sans MS", 20),
                            bg='#b3ff61')
        lab_sum3 = tk.Label(root_st, text=f"Правильных ответов {mf3[0]}",
                            font=("Comic Sans MS", 20),
                            bg='#ffcc80')
        lab_sum_not3 = tk.Label(root_st, text=f"Не правильных ответов {mf3[1]}",
                                font=("Comic Sans MS", 20),
                                bg='#ffcc80')

        lab_lev4 = tk.Label(root_st, text="Мега мозг:",
                            font=("Comic Sans MS", 20),
                            bg='#b3ff61')
        lab_sum4 = tk.Label(root_st, text=f"Правильных ответов {mf4[0]}",
                            font=("Comic Sans MS", 20),
                            bg='#ffcc80')
        lab_sum_not4 = tk.Label(root_st, text=f"Не правильных ответов {mf4[1]}",
                                font=("Comic Sans MS", 20),
                                bg='#ffcc80')

        lab_lev1.grid(row=0,columnspan=1,sticky="we")
        lab_sum1.grid(row=1,columnspan=1,sticky="w")
        lab_sum_not1.grid(row=2,columnspan=1,sticky="w")
        lab_lev2.grid(row=3,columnspan=1,sticky="we")
        lab_sum2.grid(row=4,columnspan=1,sticky="w")
        lab_sum_not2.grid(row=5,columnspan=1,sticky="w")
        lab_lev3.grid(row=6,columnspan=1,sticky="we")
        lab_sum3.grid(row=7,columnspan=1,sticky="w")
        lab_sum_not3.grid(row=8,columnspan=1,sticky="w")
        lab_lev4.grid(row=9,columnspan=1,sticky="we")
        lab_sum4.grid(row=10,columnspan=1,sticky="w")
        lab_sum_not4.grid(row=11,columnspan=1,sticky="w")
    lab_s = tk.Button(root_s, text="Изменить уровень сложности",
                      anchor='w',
                      font=("Comic Sans MS", 14),
                      bg="#a6ffd1",
                      command=quit)
    lab_s.grid(row=0, column=0)

    lab_s1 = tk.Button(root_s, text="Посмотреть статистику",
                       anchor='w',
                       font=("Comic Sans MS", 14),
                       bg="#a6ffd1",
                       command=stata)
    lab_s1.grid(row=1, column=0, columnspan=1, sticky="we")


def start():
    global sum, sum_not, root_1
    root.destroy()
    sum = 0
    sum_not = 0
    sum_primer = 0

    def start_game():
        global root_1
        root_1 = tk.Tk()
        root_1.title("Тренажер для устного счёта")
        root_1.geometry("930x768+480+120")
        root_1.resizable(False, False)
        root_1.iconbitmap('data\\geek.ico')
        root_1.config(bg='#ffcc80')

        def result():
            global sum, sum_not
            root_2 = tk.Tk()
            root_2.title("Результат")
            root_2.geometry("700x308+580+300")
            root_2.resizable(False, False)
            root_2.iconbitmap('data\\geek.ico')
            root_2.config(bg='#2be06d')

            def save():
                global root_sv
                root_sv = tk.Tk()
                root_sv.title("Сохранить")
                root_sv.geometry("170x80+850+450")
                root_sv.resizable(False, False)
                root_sv.iconbitmap('data\\geek.ico')

                def save_no():
                    root_sv.destroy()

                def save_yes():
                    global my_file_1, my_file_2, my_file_3, my_file_4
                    if level == 1:
                        my_file_1 = open("data\\result_level1.txt", "w+")
                        my_file_1.write(f"{sum}\n")
                        my_file_1.write(f"{sum_not}")
                        my_file_1.close()

                    elif level == 2:
                        my_file_2 = open("data\\result_level2.txt", "w+")
                        my_file_2.write(f"{sum}\n")
                        my_file_2.write(f"{sum_not}")
                        my_file_2.close()

                    elif level == 3:
                        my_file_3 = open("data\\result_level3.txt", "w+")
                        my_file_3.write(f"{sum}\n")
                        my_file_3.write(f"{sum_not}")
                        my_file_3.close()

                    elif level == 4:
                        my_file_4 = open("data\\result_level4.txt", "w+")
                        my_file_4.write(f"{sum}\n")
                        my_file_4.write(f"{sum_not}")
                        my_file_4.close()

                lab_sav = tk.Label(root_sv, text="Сохранить?",
                                   font=(13))
                but_yes = tk.Button(root_sv, text="Да",
                                    font=(13),
                                    command=save_yes)
                but_no = tk.Button(root_sv, text="Нет",
                                   font=(13),
                                   command=save_no)
                lab_sav.grid(row=0, column=1)
                but_yes.grid(row=1, column=0, columnspan=1, sticky="w")
                but_no.grid(row=1, column=2, columnspan=1, sticky="e")

            lab_sum = tk.Label(root_2, text=f"Правильных ответов {sum}",
                               font=("Comic Sans MS", 30),
                               bg='#2be06d')
            lab_sum_not = tk.Label(root_2, text=f"Не правильных ответов {sum_not}",
                                   font=("Comic Sans MS", 30),
                                   bg='#2be06d')

            but_save = tk.Button(root_2, text="Сохранить",
                                 font=("Comic Sans MS", 30),
                                 command=save)

            lab_sum.grid(row=0, column=0, columnspan=1, sticky="we")
            lab_sum_not.grid(row=1, column=0, columnspan=1, sticky="we")
            but_save.grid(row=2, column=0, sticky="w")
            root_2.grid_rowconfigure(2, minsize=200)

            root_2.mainloop()

        def check():
            global sum, sum_not

            def start_game_new():
                root_1.destroy()
                start_game()
            if (ent_1.get() == str(data.proverka())):
                sum = sum + 1
                lab_3 = tk.Label(root_1, text=f"Правильно",
                                 font=("Comic Sans MS", 30),
                                 bg='#ffcc80')
                ent_1.delete(0, tk.END)
                but_next = tk.Button(root_1, text="Дальше",
                                     font=("Comic Sans MS", 30),
                                     command=start_game_new)

                but_answer['state'] = tk.DISABLED
                but_next.grid(row=2, column=0, columnspan=1, sticky="e")
                lab_3.grid(row=2)
                root_1.grid_columnconfigure(1, minsize=200)
                root_1.grid_rowconfigure(2, minsize=0)
            else:
                sum_not = sum_not + 1
                lab_4 = tk.Label(root_1, text=f"Не правильно",
                                 font=("Comic Sans MS", 30),
                                 bg='#ffcc80')

                lab_2 = tk.Label(root_1, text=f"Правильный ответ: {data.proverka()}",
                                 font=("Comic Sans MS", 30),
                                 bg='#ffcc80')

                but_next = tk.Button(root_1, text="Дальше",
                                     font=("Comic Sans MS", 30),
                                     command=start_game_new)

                but_answer['state'] = tk.DISABLED
                but_next.grid(row=2, column=0, columnspan=1, sticky="e")
                lab_2.grid(column=3)
                lab_4.grid(row=2)
                root_1.grid_columnconfigure(1, minsize=400)
                root_1.grid_rowconfigure(2, minsize=0)
        lab_1 = tk.Label(root_1, text=data.score(level),
                         font=("Comic Sans MS", 30),
                         bg="#4ef5a4",
                         bd=20,
                         width=37)
        ent_1 = tk.Entry(root_1,
                         font=("Comic Sans MS", 30),
                         justify=tk.CENTER)

        but_answer = tk.Button(root_1, text="Проверить",
                               font=("Comic Sans MS", 30),
                               command=check)

        but_result = tk.Button(root_1, text="Результаты",
                               font=("Comic Sans MS", 30),
                               command=result)

        but_settings = tk.Button(root_1, text="Настройки",
                                 font=("Comic Sans MS", 30),
                                 command=settings)

        but_settings.grid(row=3, column=0, columnspan=1)
        but_result.grid(row=3, column=0, sticky="w")
        root_1.grid_rowconfigure(3, minsize=325)
        but_answer.grid(row=2, column=0, columnspan=1, sticky="w")
        ent_1.grid(row=1, column=0, sticky="we")
        lab_1.grid(row=0, column=0, sticky="we")
        root_1.mainloop()
    start_game()


# ---------------------------------------------------------------------------
def welcome():
    global but_1, but_2, but_3, but_4, but_start, root
    root = tk.Tk()
    root.title("Тренажер для устного счёта")
    root.geometry("480x302+740+230")
    root.resizable(False, False)
    root.iconbitmap('data\\geek.ico')
    root.config(bg="#a6ffd1")

    lab_1 = tk.Label(root, text="Тренажер для устного счёта в уме",
                     bg="#a6ffd1",
                     font=("Comic Sans MS", 18)).grid(row=0, column=0, columnspan=4)
    lab_2 = tk.Label(root, text="Выберете уровень сложности:",
                     anchor='w',
                     font=("Comic Sans MS", 14),
                     bg="#a6ffd1").grid(row=1, column=0, columnspan=4, sticky="we")
    but_1 = tk.Button(root, text="Лёгкий",
                      font=("Comic Sans MS", 14),
                      bg="#23b86b",
                      bd=5,
                      command=switchButton.switchButtonState_1)
    but_2 = tk.Button(root, text="Средний",
                      font=("Comic Sans MS", 14),
                      bg="#23b86b",
                      bd=5,
                      command=switchButton.switchButtonState_2)
    but_3 = tk.Button(root, text="Сложный",
                      font=("Comic Sans MS", 14),
                      bg="#23b86b",
                      bd=5,
                      command=switchButton.switchButtonState_3)
    but_4 = tk.Button(root, text="Мега мозг",
                      font=("Comic Sans MS", 14),
                      bg="#23b86b",
                      bd=5,
                      command=switchButton.switchButtonState_4)

    but_1.grid(row=2, column=0, columnspan=1, sticky="we")
    but_2.grid(row=2, column=1, columnspan=1, sticky="we")
    but_3.grid(row=2, column=2, columnspan=1, sticky="we")
    but_4.grid(row=2, column=3, columnspan=1, sticky="we")
    root.grid_rowconfigure(1, minsize=70)
    root.grid_columnconfigure(0, minsize=120)
    root.grid_columnconfigure(1, minsize=120)
    root.grid_columnconfigure(2, minsize=120)
    root.grid_columnconfigure(3, minsize=120)
    root.grid_rowconfigure(4, minsize=150)

    but_start = tk.Button(root, text="Начать",
                          font=("Comic Sans MS", 18),
                          bg="#2ca88d",
                          bd=5,
                          command=start,
                          state=tk.DISABLED)
    but_start.grid(row=4, column=1, columnspan=2, sticky="we")
    root.mainloop()


welcome()
