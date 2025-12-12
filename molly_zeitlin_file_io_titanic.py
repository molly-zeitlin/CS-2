def load_and_display(file):
    try:
        with open("display_titanic_data.csv", "w") as output:
            counter = -1
            for line in file:
                if counter < 10:
                    print(line)
                    output.write(line)
                counter += 1
            print(f"Total passengers: {counter}")
            output.write(f"Total passengers: {counter}")
    except:
        print("FILE NOT FOUND")
    
def survival_counter(file):
    try:
        with open("total_survival_counter.csv", "w") as output:
                survive = 0
                l_count = -1
                for l in file:
                    data = l.strip().split(",")
                    l_count += 1
                    if data[1] == "1":
                        survive += 1
                s_percent = str(round((survive / l_count)*100)).lstrip("0")
                print(f"Total survival rate: {s_percent}%")
                output.write(f"Total survival rate: {s_percent}%")
    except:
        print("FILE NOT FOUND")

def survival_by_gender(file):
    try:
        with open("survival_by_gender.csv", "w") as output:
            m_survive = 0
            m_count = 0
            f_survive = 0
            f_count = 0
            for l in file:
                data = l.strip().split(",")
                if data[5] == "male":
                    m_count +=1
                    if data[1] == "1":
                        m_survive +=1
                elif data[5] == "female":
                    f_count +=1
                    if data[1] =="1":
                        f_survive +=1
                else:
                    continue
            ms_percent = str(round((m_survive / m_count)*100)).lstrip("0")
            print(f"Male passenger survival rate: {ms_percent}%")
            output.write(f"Male passenger survival rate: {ms_percent}%\n")
            fs_percent = str(round((f_survive / f_count)*100)).lstrip("0")
            print(f"Female passenger surival rate: {fs_percent}%")
            output.write(f"Female passenger surival rate: {fs_percent}%\n")
            if ms_percent > fs_percent:
                print("Males had a higher survival rate than the females")
                output.write("Males had a higher survival rate than the females\n")
            elif fs_percent > ms_percent:
                print("Females had a higher survival rate than the males")
                output.write("Females had a higher survival rate than the males\n")
            else:
                print("Males and females had the same survival rate")
                output.write("Males and females had the same survival rate\n")
    except:
        print("FILE NOT FOUND")

def average_age(file):
    try:
        with open("age_analysis.csv", "w") as output:
            ages_list = []
            s_ages_list = []
            d_ages_list = []
            next(file)
            for l in file:
                data = l.strip().split(",")
                try:
                    ages_list.append(float(data[6]))
                except:
                    continue
                if data[1] == "1":
                    try:
                        s_ages_list.append(float(data[6]))
                    except:
                        continue
                else:
                    try:
                        d_ages_list.append(float(data[6]))
                    except:
                        continue
            t_age = sum(ages_list)
            a_age = round((t_age)/(len(ages_list)))
            print(f"Average age of passengers: {a_age}")
            output.write(f"Average age of passengers: {a_age}\n")
            t_s_age = sum(s_ages_list)
            a_s_age = round((t_s_age)/(len(s_ages_list)))
            print(f"Average age of survivors: {a_s_age}")
            output.write(f"Average age of survivors: {a_s_age}\n")
            t_d_age = sum(d_ages_list)
            a_d_age = round((t_d_age)/(len(d_ages_list)))
            print(f"Average age of non-survivors: {a_d_age}")
            output.write(f"Average age of non-survivors: {a_d_age}\n")
            youngest = min(ages_list)
            print(f"Age of youngest passenger: {youngest}")
            output.write(f"Age of youngest passenger: {youngest}\n")
            oldest = max(ages_list)
            print(f"Age of oldest passenger: {oldest}")
            output.write(f"Age of oldest passenger: {oldest}")
    except:
        print("FILE NOT FOUND")

def class_based_analysis(file):
    try:
        with open("class_based_analysis.csv", "w") as output:
            next(file)
            class1 = 0
            class2 = 0
            class3 = 0
            fare_total1 = []
            fare_total2 = []
            fare_total3 = []
            survivors1 = 0
            survivors2 = 0
            survivors3 = 0
            for l in file:
                data = l.strip().split(",")
                if data[2] == "1":
                    class1+=1
                    fare_total1.append(float(data[10]))
                    if data[1] == "1":
                        survivors1+=1
                elif data[2] == "2":
                    class2+=1
                    fare_total2.append(float(data[10]))
                    if data[1] == "1":
                        survivors2+=1
                else:
                    class3+=1
                    fare_total3.append(float(data[10]))
                    if data[1] == "1":
                        survivors3+=1
            s_rate1 = str(round((survivors1/class1)*100)).lstrip("0")
            print(f"{s_rate1}% of 1st class passengers survived")
            output.write(f"{s_rate1}% of 1st class passengers survived\n")
            s_rate2 = str(round((survivors2/class2)*100)).lstrip("0")
            print(f"{s_rate2}% of 2nd class passengers survived")
            output.write(f"{s_rate2}% of 2nd class passengers survived\n")
            s_rate3 = str(round((survivors3/class3)*100)).lstrip("0")
            print(f"{s_rate3}% of 3rd class passengers survived")
            output.write(f"{s_rate3}% of 3rd class passengers survived\n")
            a_fare1 = round(sum(fare_total1)/len(fare_total1))
            print(f"Average fare paid for 1st class: ${a_fare1}")
            output.write(f"Average fare paid for 1st class: ${a_fare1}\n")
            a_fare2 = round(sum(fare_total2)/len(fare_total2))
            print(f"Average fare paid for 2nd class: ${a_fare2}")
            output.write(f"Average fare paid for 2nd class: ${a_fare2}\n")
            a_fare3 = round(sum(fare_total3)/len(fare_total3))
            print(f"Average fare paid for 3rd class: ${a_fare3}")
            output.write(f"Average fare paid for 3rd class: ${a_fare3}\n")
            if s_rate1 > s_rate2 and s_rate1 > s_rate3:
                print("1st class had the highest chance of survival")
                output.write("1st class had the highest chance of survival")
            elif s_rate2 > s_rate1 and s_rate2 > s_rate3:
                print("2nd class had the highest chance of survival")
                output.write("2nd class had the highest chance of survival")
            else:
                print("3rd class had the highest chance of survival")
                output.write("3rd class had the highest chance of survival")
    except:
        print("FILE NOT FOUND")


def fam_survival_patterns(file):
    try:
        with open("fam_survival_patterns.csv", "w") as output:
            next(file)
            surv_fam = 0
            surv_alone = 0
            fam_total = 0
            alone_total = 0
            for l in file:
                data = l.strip().split(",")
                SibSp = float(data[7])
                Parch = float(data[8])
                FamilySize = SibSp + Parch + 1
                if FamilySize > 1:
                    fam_total += 1
                    if data[1] == "1":
                        surv_fam += 1
                else:
                    alone_total += 1
                    if data[1] == "1":
                        surv_alone +=1
            fam_surv_rate = round((surv_fam/fam_total)*100)
            alone_surv_rate = round((surv_alone/alone_total)*100)
            print(f"Family Survival Rate: {fam_surv_rate}%")
            output.write(f"Family Survival Rate: {fam_surv_rate}%\n")
            print(f"Alone Survival Rate: {alone_surv_rate}%")
            output.write(f"Alone Survival Rate: {alone_surv_rate}%\n")
            if fam_surv_rate > alone_surv_rate:
                print("Those travelling with family had a higher chance of survival than those travelling alone")
                output.write("Those travelling with family had a higher chance of survival than those travelling alone")
            else:
                print("Those travelling alone had a higher chance of survival than those travelling with family")
                output.write("Those travelling alone had a higher chance of survival than those travelling with family")
    except:
        print("FILE NOT FOUND")

def data_visualzaion(file):
    try:
        with open("data_visualization.csv") as output:
            output.write("Female", + "Male\n")
            m_survive = 0
            m_count = 0
            f_survive = 0
            f_count = 0
            for l in file:
                data = l.strip().split(",")
                if data[5] == "male":
                    m_count +=1
                    if data[1] == "1":
                        m_survive +=1
                elif data[5] == "female":
                    f_count +=1
                    if data[1] =="1":
                        f_survive +=1
                else:
                    continue
            ms_percent = str(round((m_survive / m_count)*100)).lstrip("0")
            fs_percent = str(round((f_survive / f_count)*100)).lstrip("0")
            output.write(f"{ms_percent}%", + f"{fs_percent}%")
    except:
        print("FILE NOT FOUND")

def main():
    try:
        file = open("titanic.csv", "r")
        i = 0
        while i < 10:
            user_response = input("What would you like to do?\n1. Load and Display Data from the Titanic to a CSV file\n2. Count the survivors from the Titanic and write to a CSV file\n3. Calculate the survival rates of each gender of passengers from the Titanic and write to a CSV file\n4. Calculate the average age of passengers and write to a CSV file\n5. Analyze data from Titanic based on passenger classes\n6. Analyze family survival rates\n7. Visualize data\n8. End program\nEnter the number corresponding to your choice: ")
            if user_response == "1":
                load_and_display(file)
                file.seek(1)
                i+=1
            elif user_response == "2":
                survival_counter(file)
                file.seek(1)
                i+=1
            elif user_response == "3":
                survival_by_gender(file)
                file.seek(1)
                i+=1
            elif user_response == "4":
                average_age(file)
                file.seek(1)
                i+=1
            elif user_response == "5":
                class_based_analysis(file)
                file.seek(1)
                i+=1
            elif user_response == "6":
                fam_survival_patterns(file)
                file.seek(1)
                i+=1
            elif user_response == "7":
                #data_visualzaion(file)
                file.seek(1)
                i+=1
            elif user_response == "8":
                quit()
            else:
                print("INVALID RESPONSE!")

    except FileNotFoundError:
        print("Error: 'titanic.csv' file not found.")

main()