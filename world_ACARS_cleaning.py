# Bereinigt world_ACARS_reports_ .txt Dateien
# Muster .txt Datei in world_ACARS Ordner
# Bereinigte Muster .csv Datei in world_ACARS Ordner

import os
import re
import datetime
import time

# Gib den Pfad zu den .txt Dateien an
path = "C:/Users/Regs/world_ACARS_reports"

# Gib den Pfad für die bereinigten .csv Dateien an
save_path = "C:/Users/Regs/"



def get_all_files(path):
    file_list = []
    for file in os.listdir(path):
        if file.endswith('txt'):
            file_list.append(os.path.join(path + "/" + file))

        else:
            continue

    return file_list


def make_txt_pretty(file_list, save_path):
    corrupt_files = []
    for path in file_list:
        try:
            new_filename = path.replace('.txt', "")[-8:]
            with open(path, "r", encoding="ANSI") as f_org,\
                open(save_path + "ACARS_" + new_filename + ".csv", "w", encoding="utf-8") as f_cop:
                lines = f_org.readlines()
                lendoc = len(lines)
                source = lines[9].replace(")", "")
                reg_lines = lines[14:lendoc]
                f_cop.write("Reg;Type;Airline;Time;Date;Flight;From;Found;Source\n")

                for new_line in reg_lines:
                    new_line = new_line.lstrip().split()
                    # Kontrolle für Datum an Pos. 5 (4)
                    result_date = re.search(r'[0-9]{8}', new_line[4])
                    if result_date:
                        pass
                    else:
                        new_line[1:3] = [' '.join(new_line[1:3])]

                    # Kontrolle für Zeit an Pos 4 (3)
                    result_time = re.search(r'[0-9]{4}', new_line[3])
                    if result_time:
                        pass
                    else:
                        new_line[1:3] = [' '.join(new_line[1:3])]


                    new_line[7:] = [' '.join(new_line[7:])]
                    new_line[4] = datetime.datetime.strptime(new_line[4], "%Y%m%d").strftime("%Y.%m.%d")
                    new_line[3] = datetime.datetime.strptime(new_line[3], "%H%M").strftime("%H:%M")
                    new_line.append(source)
                    new_line = ";".join(str(elem) for elem in new_line)
                    new_line = new_line.replace('(', "")
                    new_line = new_line.replace(')', "")
                    new_line = new_line.replace('[', "")
                    new_line = new_line.replace(']', "")
                    f_cop.write(new_line)

        except Exception as e:
            print(e)
            corrupt_files.append(path)

        with open(save_path + "Corrupt_files.csv", "w") as f_corrupt:
            for c_file in corrupt_files:
                f_corrupt.write(c_file + "\n")

    return corrupt_files


# Jahr(e) + Ordner + Name der zu bereinigenden Dateien
def main():
    start_time = time.time()
    for year in range(2007, 2015):
        file_list = get_all_files(path)
        corrupt_files = make_txt_pretty(file_list, save_path)
        print(f"{year} bereinigt")
        print(corrupt_files)
        print("---Fertig in %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
