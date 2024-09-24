import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def Show_Rating(kolvo):
    filek = open('input_data.txt')
    list_strs = list()
    list_strs = filek.readlines()
    kt1, kt2, kt3, kt4, kt5, common_rating = [[] for i in range(kolvo)], [[] for i in range(kolvo)],[[] for i in range(kolvo)],\
        [[] for i in range(kolvo)],[[] for i in range(kolvo)],[[] for i in range(kolvo)]
    numbers_reportcard = list()
    for i in range(len(list_strs)):
        list_strs[i] = list_strs[i].replace("\t", "|")
        list_strs[i] = list_strs[i].replace("\n", "")
    for i in range(len(list_strs)):
        if list_strs[i][1] == "|":
            numbers_reportcard.append(list_strs[i][12:15])
        else:
            numbers_reportcard.append(list_strs[i][13:16])
        count = 0
        count_iteration = 0
        for j in range(15, len(list_strs[i])):
            curr_numb = ''
            if list_strs[i][j] == "|":
                count += 1

                if count <= 5:
                    while list_strs[i][j + 1] != '|':
                        curr_numb += list_strs[i][j + 1]
                        j += 1
                    if curr_numb != '':
                        kt1[i].append(int(curr_numb))
                    count_iteration += 1

                if count <= 10 and count > 5:
                    while j + 1 != len(list_strs[i]) and list_strs[i][j + 1] != '|':
                        curr_numb += list_strs[i][j + 1]
                        j += 1
                    if curr_numb != '':
                        kt2[i].append(int(curr_numb))
                    count_iteration += 1

                if count <= 15 and count > 10:
                    while j + 1 != len(list_strs[i]) and list_strs[i][j + 1] != '|':
                        curr_numb += list_strs[i][j + 1]
                        j += 1
                    if curr_numb != '':
                        kt3[i].append(int(curr_numb))
                    count_iteration += 1

                if count <= 20 and count > 15:
                    while j + 1 != len(list_strs[i]) and list_strs[i][j + 1] != '|':
                        curr_numb += list_strs[i][j + 1]
                        j += 1
                    if curr_numb != '':
                        kt4[i].append(int(curr_numb))
                    count_iteration += 1
                if count <= 25 and count > 20:
                    while j + 1 != len(list_strs[i]) and list_strs[i][j + 1] != '|':
                        curr_numb += list_strs[i][j + 1]
                        j += 1
                    if curr_numb != '':
                        kt5[i].append(int(curr_numb))
                    count_iteration += 1

                if count == 27:
                    while j + 1 != len(list_strs[i]) and list_strs[i][j + 1] != '|':
                        curr_numb += list_strs[i][j + 1]
                        j += 1
                    if curr_numb != '':
                        common_rating[i].append(int(curr_numb))
                    count_iteration += 1
    return [kt1, kt2, kt3, kt4, kt5, common_rating, numbers_reportcard]

def grafik(value):
    arr1, arr2, arr3 = [], [], []
    if value == 5:
        for i in Show_Rating(26)[value]:
            if i:
                arr1.append(i[0])
            else:
                arr1.append(0)
    elif Show_Rating(26)[value][0]:
        for i in Show_Rating(26)[value]:

            arr1.append(i[0])
            arr2.append(i[1])
            arr3.append(i[2])
    if arr1 and arr2 and arr3:
        return [arr1, arr2, arr3]
    elif arr1:
        return arr1
    else:
        return []

numbers_reportcards = Show_Rating(26)[-1]
for i in range(len(numbers_reportcards)):
    numbers_reportcards[i] = int(numbers_reportcards[i])
print(" 1. График 1 контрольной точки", '\n', "2. График 2 контрольной точки", '\n', "3. График 3 контрольной точки", '\n', "4. График 4 контрольной точки", '\n'
      " 5. График 5 контрольной точки", '\n', "6. Общий рейтинг", '\n', "0. Выход из программы")
Pin = int(input("Выберите номер точки: "))
if Pin != 6:
    print(" 1. График по видам занятий рейтинга дисциплины", '\n', "2. График общего рейтинга дисциплины",
          '\n', "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
    Pin_choice = int(input("Выберите график для рассмотрения:"))
else:
    print(" 1. График общего рейтинга дисциплины", '\n', "2. График распределения оценок", '\n', "0. Выход из подпрограммы")
    Pin_choice = int(input("Выберите график для рассмотрения:"))
while Pin in (0, 1, 2, 3, 4, 5, 6):
    if Pin_choice not in (1, 2, 3):
        print(" 1. График по видам занятий рейтинга дисциплины", '\n', "2. График общего рейтинга дициплины", '\n',
              "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
        Pin_choice = int(input("Выберите график для рассмотрения:"))
    match Pin:
        case 1:
            if not grafik(0):
                print("Ещё не выставили рейтинг за эту контрольную точку")
            else:
                while Pin_choice in (0, 1, 2, 3):
                    match Pin_choice:
                        case 1:
                            arrays = grafik(0)
                            if arrays:
                                fig, ax = plt.subplots()
                                fig.set_size_inches(18, 7)
                                y_pos1 = np.arange(26) - 0.2
                                y_pos2 = np.arange(26) + 0.2
                                plt.suptitle('Рейтинг 1 контрольной точки по видам занятий.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax.bar(y_pos1, arrays[0], align='center', alpha=0.5, width=0.4, label='Лекции')
                                ax.bar(y_pos2, arrays[1], align='center', alpha=0.5, width=0.4, label='Практики')
                                ax.set(xticks=y_pos1 + 0.2, xticklabels=numbers_reportcards)
                                ax.set_ylabel('Значение', fontsize=18)
                                ax.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax.legend(bbox_to_anchor=(-0.05, 0.25), title='Вид занятий')
                                plt.show()
                        case 2:
                            arrays = grafik(0)
                            if arrays:
                                fig, ax = plt.subplots()
                                fig.set_size_inches(18, 7)
                                y_pos = np.arange(26)
                                plt.suptitle('Общий рейтинг 1 контрольной точки.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax.bar(y_pos, arrays[2], align='center', alpha=0.5, width=0.4)
                                ax.set(xticks=y_pos, xticklabels=numbers_reportcards,
                                          xlabel='Последние 3 цифры зачётки')
                                ax.set_ylabel('Значение', fontsize=18)
                                ax.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax.hlines(60, -1, 25.5, color='red', label='Удовлетворительно')
                                ax.hlines(75, -1, 25.5, color='orange', label='Хорошо')
                                ax.hlines(85, -1, 25.5, color='green', label='Отлично')
                                ax.legend(bbox_to_anchor=(-0.015, 0.3), title='Отметка')
                                plt.show()
                        case 3:
                            arrays = grafik(0)[2]
                            if arrays:
                                colors = ['tab:gray', 'tab:red', 'tab:orange', 'tab:green']
                                Notes = [0, 0, 0, 0]
                                Names = ['Неудовлетворительно', 'Удовлетворительно', 'Хорошо', 'Отлично']
                                y_pos3 = np.arange(4)
                                for i in arrays:
                                    if i < 60:
                                        Notes[0] += 1
                                    elif i < 75 and i >= 60:
                                        Notes[1] += 1
                                    elif i >= 75 and i < 85:
                                        Notes[2] += 1
                                    else:
                                        Notes[3] += 1
                                fig, ax = plt.subplots()
                                fig.set_size_inches(12, 7)
                                plt.suptitle('График распределения оценок.\n Курс "Алгоритмизация и программирование"')
                                wedges, texts, autotexts = ax.pie(Notes, labels=Names, autopct='%1.2f%%', colors=colors)
                                ax.axis('equal')
                                plt.show()
                        case 0:
                            break
                    print(" 1. График по видам занятий рейтинга дисциплины", '\n', "2. График общего рейтинга диcциплины",
                          '\n', "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
                    Pin_choice = int(input("Выберите график для рассмотрения:"))
        case 2:
            if not grafik(1):
                print("Ещё не выставили рейтинг за эту контрольную точку")
            else:
                while Pin_choice in (0, 1, 2, 3):
                    match Pin_choice:
                        case 1:
                            arrays = grafik(1)
                            if arrays:
                                fig1, ax1 = plt.subplots()
                                fig1.set_size_inches(18, 7)
                                y_pos1 = np.arange(26) - 0.2
                                y_pos2 = np.arange(26) + 0.2
                                plt.suptitle('Рейтинг 2 контрольной точки по видам занятий.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax1.bar(y_pos1, arrays[0], align='center', alpha=0.5, width=0.4, label='Лекции')
                                ax1.bar(y_pos2, arrays[1], align='center', alpha=0.5, width=0.4, label='Практики')
                                ax1.set(xticks=y_pos1 + 0.2, xticklabels=numbers_reportcards)
                                ax1.set_ylabel('Значение', fontsize=18)
                                ax1.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax1.legend(bbox_to_anchor=(-0.05, 0.25), title='Вид занятий')
                                plt.show()
                        case 2:
                            arrays = grafik(1)
                            if arrays:
                                fig1, ax1 = plt.subplots()
                                fig1.set_size_inches(18, 7)
                                y_pos = np.arange(26)
                                plt.suptitle('Общий рейтинг 2 контрольной точки.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax1.bar(y_pos, arrays[2], align='center', alpha=0.5, width=0.4)
                                ax1.set(xticks=y_pos, xticklabels=numbers_reportcards,
                                          xlabel='Последние 3 цифры зачётки')
                                ax1.set_ylabel('Значение', fontsize=18)
                                ax1.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax1.hlines(60, -1, 25.5, color='red', label='Удовлетворительно')
                                ax1.hlines(75, -1, 25.5, color='yellow', label='Хорошо')
                                ax1.hlines(85, -1, 25.5, color='green', label='Отлично')
                                ax1.legend(bbox_to_anchor=(-0.015, 0.3), title='Отметка')
                                plt.show()
                        case 3:
                            arrays = grafik(1)[2]
                            if arrays:
                                Notes = [0 ,0 ,0, 0]
                                Names = ['Неудовлетворительно', 'Удовлетворительно', 'Хорошо', 'Отлично']
                                y_pos3 = np.arange(4)
                                for i in arrays:
                                    if i < 60:
                                        Notes[0] += 1
                                    elif i < 75 and i >= 60:
                                        Notes[1] += 1
                                    elif i >= 75 and i < 85:
                                        Notes[2] += 1
                                    else:
                                        Notes[3] += 1
                                fig1, ax1 = plt.subplots()
                                fig1.set_size_inches(12, 7)
                                plt.suptitle('График распределения оценок.\n Курс "Алгоритмизация и программирование"')
                                wedges, texts, autotexts = ax1.pie(Notes, labels=Names, autopct='%1.2f%%')
                                ax1.axis('equal')
                                plt.show()
                        case 0:
                            break
                    print(" 1. График по видам занятий рейтинга дисциплины", '\n', "2. График общего рейтинга диcциплины",
                          '\n', "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
                    Pin_choice = int(input("Выберите график для рассмотрения:"))
        case 3:
            if not grafik(2):
                print("Ещё не выставили рейтинг за эту контрольную точку")
            else:
                while Pin_choice in (0, 1, 2, 3):
                    match Pin_choice:
                        case 1:
                            arrays = grafik(2)
                            if arrays:
                                fig2, ax2 = plt.subplots()
                                fig2.set_size_inches(18, 7)
                                y_pos1 = np.arange(26) - 02.
                                y_pos2 = np.arange(26) + 0.2
                                plt.suptitle(
                                    'Рейтинг 3 контрольной точки по видам занятий.\n Курс "Алгоритмизация и программирование"',
                                    fontsize=20)
                                ax2.bar(y_pos1, arrays[0], align='center', alpha=0.5, width=0.4, label='Лекции')
                                ax2.bar(y_pos2, arrays[1], align='center', alpha=0.5, width=0.4, label='Практики')
                                ax2.set(xticks=y_pos1 + 0.2, xticklabels=numbers_reportcards)
                                ax2.set_ylabel('Значение', fontsize=18)
                                ax2.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax2.legend(bbox_to_anchor=(-0.05, 0.25), title='Вид занятий')
                                plt.show()
                        case 2:
                            arrays = grafik(2)
                            if arrays:
                                fig2, ax2 = plt.subplots()
                                fig2.set_size_inches(18, 7)
                                y_pos = np.arange(26)
                                plt.suptitle('Общий рейтинг 3 контрольной точки.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax2.bar(y_pos, arrays[2], align='center', alpha=0.5, width=0.4)
                                ax2.set(xticks=y_pos, xticklabels=numbers_reportcards,
                                        xlabel='Последние 3 цифры зачётки')
                                ax2.set_ylabel('Значение', fontsize=18)
                                ax2.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax2.hlines(60, -1, 25.5, color='red', label='Удовлетворительно')
                                ax2.hlines(75, -1, 25.5, color='yellow', label='Хорошо')
                                ax2.hlines(85, -1, 25.5, color='green', label='Отлично')
                                ax2.legend(bbox_to_anchor=(-0.015, 0.3), title='Отметка')
                                plt.show()
                        case 3:
                            arrays = grafik(2)[2]
                            if arrays:
                                Notes = [0, 0, 0, 0]
                                Names = ['Неудовлетворительно', 'Удовлетворительно', 'Хорошо', 'Отлично']
                                y_pos3 = np.arange(4)
                                for i in arrays:
                                    if i < 60:
                                        Notes[0] += 1
                                    elif i < 75 and i >= 60:
                                        Notes[1] += 1
                                    elif i >= 75 and i < 85:
                                        Notes[2] += 1
                                    else:
                                        Notes[3] += 1
                                fig2, ax2 = plt.subplots()
                                fig2.set_size_inches(12, 7)
                                plt.suptitle('График распределения оценок.\n Курс "Алгоритмизация и программирование"')
                                wedges, texts, autotexts = ax2.pie(Notes, labels=Names, autopct='%1.2f%%')
                                ax2.axis('equal')
                                plt.show()
                        case 0:
                            break
                    print(" 1. График по видам занятий рейтинга дисциплины", '\n',
                          "2. График общего рейтинга диcциплины",
                          '\n', "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
                    Pin_choice = int(input("Выберите график для рассмотрения:"))
        case 4:
            if not grafik(3):
                print("Ещё не выставили рейтинг за эту контрольную точку")
            else:
                while Pin_choice in (0, 1, 2, 3):
                    match Pin_choice:
                        case 1:
                            arrays = grafik(3)
                            if arrays:
                                fig3, ax3 = plt.subplots()
                                fig3.set_size_inches(18, 7)
                                y_pos1 = np.arange(26) - 0.2
                                y_pos2 = np.arange(26) + 0.2
                                plt.suptitle(
                                    'Рейтинг 4 контрольной точки по видам занятий.\n Курс "Алгоритмизация и программирование"',
                                    fontsize=20)
                                ax3.bar(y_pos1, arrays[0], align='center', alpha=0.5, width=0.4, label='Лекции')
                                ax3.bar(y_pos2, arrays[1], align='center', alpha=0.5, width=0.4, label='Практики')
                                ax3.set(xticks=y_pos1 + 0.2, xticklabels=numbers_reportcards)
                                ax3.set_ylabel('Значение', fontsize=18)
                                ax3.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax3.legend(bbox_to_anchor=(-0.05, 0.25), title='Вид занятий')
                                plt.show()
                        case 2:
                            arrays = grafik(3)
                            if arrays:
                                fig3, ax3 = plt.subplots()
                                fig3.set_size_inches(18, 7)
                                y_pos = np.arange(26)
                                plt.suptitle('Общий рейтинг 4 контрольной точки.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax3.bar(y_pos, arrays[2], align='center', alpha=0.5, width=0.4)
                                ax3.set(xticks=y_pos, xticklabels=numbers_reportcards,
                                        xlabel='Последние 3 цифры зачётки')
                                ax3.set_ylabel('Значение', fontsize=18)
                                ax3.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax3.hlines(60, -1, 25.5, color='red', label='Удовлетворительно')
                                ax3.hlines(75, -1, 25.5, color='yellow', label='Хорошо')
                                ax3.hlines(85, -1, 25.5, color='green', label='Отлично')
                                ax3.legend(bbox_to_anchor=(-0.015, 0.3), title='Отметка')
                                plt.show()
                        case 3:
                            arrays = grafik(3)[2]
                            if arrays:
                                Notes = [0, 0, 0, 0]
                                Names = ['Неудовлетворительно', 'Удовлетворительно', 'Хорошо', 'Отлично']
                                y_pos3 = np.arange(4)
                                for i in arrays:
                                    if i < 60:
                                        Notes[0] += 1
                                    elif i < 75 and i >= 60:
                                        Notes[1] += 1
                                    elif i >= 75 and i < 85:
                                        Notes[2] += 1
                                    else:
                                        Notes[3] += 1
                                fig3, ax3 = plt.subplots()
                                fig3.set_size_inches(12, 7)
                                plt.suptitle('График распределения оценок.\n Курс "Алгоритмизация и программирование"')
                                wedges, texts, autotexts = ax3.pie(Notes, labels=Names, autopct='%1.2f%%')
                                ax3.axis('equal')
                                plt.show()
                        case 0:
                            break
                    print(" 1. График по видам занятий рейтинга дисциплины", '\n',
                          "2. График общего рейтинга диcциплины",
                          '\n', "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
                    Pin_choice = int(input("Выберите график для рассмотрения:"))
        case 5:
            if not grafik(4):
                print("Ещё не выставили рейтинг за эту контрольную точку")
            else:
                while Pin_choice in (0, 1, 2, 3):
                    match Pin_choice:
                        case 1:
                            arrays = grafik(4)
                            if arrays:
                                fig4, ax4 = plt.subplots()
                                fig4.set_size_inches(18, 7)
                                y_pos1 = np.arange(26) - 0.2
                                y_pos2 = np.arange(26) + 0.2
                                plt.suptitle(
                                    'Рейтинг 5 контрольной точки по видам занятий.\n Курс "Алгоритмизация и программирование"',
                                    fontsize=20)
                                ax4.bar(y_pos1, arrays[0], align='center', alpha=0.5, width=0.4, label='Лекции')
                                ax4.bar(y_pos2, arrays[1], align='center', alpha=0.5, width=0.4, label='Практики')
                                ax4.set(xticks=y_pos1 + 0.2, xticklabels=numbers_reportcards)
                                ax4.set_ylabel('Значение', fontsize=18)
                                ax4.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax4.legend(bbox_to_anchor=(-0.05, 0.25), title='Вид занятий')
                                plt.show()
                        case 2:
                            arrays = grafik(4)
                            if arrays:
                                fig4, ax4 = plt.subplots()
                                fig4.set_size_inches(18, 7)
                                y_pos = np.arange(26)
                                plt.suptitle('Общий рейтинг 5 контрольной точки.\n Курс "Алгоритмизация и программирование"', fontsize=20)
                                ax4.bar(y_pos, arrays[2], align='center', alpha=0.5, width=0.4)
                                ax4.set(xticks=y_pos, xticklabels=numbers_reportcards,
                                        xlabel='Последние 3 цифры зачётки')
                                ax4.set_ylabel('Значение', fontsize=18)
                                ax4.set_xlabel('Последние 3 цифры зачётки', loc='right')
                                ax4.hlines(60, -1, 25.5, color='red', label='Удовлетворительно')
                                ax4.hlines(75, -1, 25.5, color='yellow', label='Хорошо')
                                ax4.hlines(85, -1, 25.5, color='green', label='Отлично')
                                ax4.legend(bbox_to_anchor=(-0.015, 0.3), title='Отметка')
                                plt.show()
                        case 3:
                            arrays = grafik(4)[2]
                            if arrays:
                                Notes = [0, 0, 0, 0]
                                Names = ['Неудовлетворительно', 'Удовлетворительно', 'Хорошо', 'Отлично']
                                y_pos3 = np.arange(4)
                                for i in arrays:
                                    if i < 60:
                                        Notes[0] += 1
                                    elif i < 75 and i >= 60:
                                        Notes[1] += 1
                                    elif i >= 75 and i < 85:
                                        Notes[2] += 1
                                    else:
                                        Notes[3] += 1
                                fig4, ax4 = plt.subplots()
                                fig4.set_size_inches(12, 7)
                                plt.suptitle('График распределения оценок.\n Курс "Алгоритмизация и программирование"')
                                wedges, texts, autotexts = ax4.pie(Notes, labels=Names, autopct='%1.2f%%')
                                ax4.axis('equal')
                                plt.show()
                        case 0:
                            break
                    print(" 1. График по видам занятий рейтинга дисциплины", '\n',
                          "2. График общего рейтинга диcциплины",
                          '\n', "3. График распределения оценок", '\n', "0. Выход из подпрограммы")
                    Pin_choice = int(input("Выберите график для рассмотрения:"))
        case 6:
            while Pin_choice in (0, 1, 2):
                match Pin_choice:
                    case 1:
                        arrays = grafik(5)
                        if arrays:
                            fig5, ax5 = plt.subplots()
                            fig5.set_size_inches(18, 7)
                            y_pos = np.arange(26)
                            plt.suptitle('Общий рейтинг студентов по курсу "Алгоритмизация и программирование"', fontsize=20)
                            ax5.bar(y_pos, arrays, align='center', alpha=0.5, width=0.4)
                            ax5.set(xticks=y_pos, xticklabels=numbers_reportcards,
                                xlabel='Последние 3 цифры зачётки')
                            ax5.set_ylabel('Значение', fontsize=18)
                            ax5.set_xlabel('Последние 3 цифры зачётки', loc='right')
                            ax5.hlines(60, -1, 25.5, color='red', label='Удовлетворительно')
                            ax5.hlines(75, -1, 25.5, color='yellow', label='Хорошо')
                            ax5.hlines(85, -1, 25.5, color='green', label='Отлично')
                            ax5.legend(bbox_to_anchor=(-0.015, 0.3), title='Отметка')
                            plt.show()
                    case 2:
                        arrays = grafik(5)
                        if arrays:
                            Notes = [0, 0, 0, 0]
                            Names = ['Неудовлетворительно', 'Удовлетворительно', 'Хорошо', 'Отлично']
                            y_pos3 = np.arange(4)
                            for i in arrays:
                                if i < 60:
                                    Notes[0] += 1
                                elif i < 75 and i >= 60:
                                    Notes[1] += 1
                                elif i >= 75 and i < 85:
                                    Notes[2] += 1
                                else:
                                    Notes[3] += 1
                            fig5, ax5 = plt.subplots()
                            fig5.set_size_inches(12, 7)
                            plt.suptitle('График распределения оценок.\n Курс "Алгоритмизация и программирование"')
                            wedges, texts, autotexts = ax5.pie(Notes, labels=Names, autopct='%1.2f%%')
                            ax5.axis('equal')
                            plt.show()
                    case 0:
                        break
                print(" 1. График общего рейтинга диcциплины",
                      '\n', "2. График распределения оценок", '\n', "0. Выход из подпрограммы")
                Pin_choice = int(input("Выберите график для рассмотрения:"))
    print(" 1. График 1 контрольной точки", '\n', "2. График 2 контрольной точки", '\n',
          "3. График 3 контрольной точки",
          '\n', "4. График 4 контрольной точки", '\n', "5. График 5 контрольной точки",
          '\n', "6. Общий рейтинг", '\n', "0. Выйти из программы")
    Pin = int(input("Выберите номер точки: "))