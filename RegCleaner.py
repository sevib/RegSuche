# Clean the files with registration inside
import os
import re
from datetime import datetime

class RegCleaner:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        

    def get_files_in_folder(self):
        file_list = []
        for file in os.listdir(self.folder_path):
            file_list.append(self.folder_path + "/" + file)
        return file_list


    def read_file(self, file_path):
        content = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    content.append(line)
                return content
                #print(content)  # This will display the content of the file
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def clean_skystef(self, flight):
        flight = flight.split()
        if len(flight) == 8:
            try:
                date_obj = datetime.strptime(flight[-1], '%H:%M:%S').time(),
                flight_dict = {
                    'code' : flight[0],
                    'callsing' : flight[1],
                    'reg' : flight[2],
                    'icao' : flight[3],
                    'falt' : flight[4],
                    'lalt' : flight[5],
                    'date' : datetime.strptime(flight[-1], '%H:%M:%S').time(),
                    'time' : datetime.strptime(flight[-2], '%d/%m/%Y').date(),
                }
                return flight_dict

            except:
                print(f"{flight} konnte nicht konvertiert werden")
                pass
                pass
 