import serial
import csv
import os
import time
from datetime import datetime

def serial_ports():
    ports = ['COM%s' % (i + 1) for i in range(256)]
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

my_serials = serial_ports()
def available_port():
    while True:
        print(f'Доступные порты: {my_serials}')
        comport = input('Введите название порта: ')
        
        if comport not in my_serials:
            print('Неверно выбран порт! Попробуйте снова.')
            continue
            
        try:
            ser = serial.Serial(comport, 9600, timeout=1)
            ser.close()
            return comport
        except (OSError, serial.SerialException):
            print('Ошибка подключения к порту. Попробуйте другой порт.')

ser = serial.Serial(available_port(), 9600)


def get_filename():
    while True:
        filename = input("Введите название файла (без расширения .csv): ").strip()
        if not filename:
            print("Название файла не может быть пустым!")
            continue
        
        filename += ".csv"
        
        if os.path.exists(filename):
            save = input(f"Файл '{filename}' уже существует. Перезаписать? (yes/no): ").lower()
            if save != 'yes':
                continue
        
        return filename


while True:
    # data = input('Vvedite znachenie datchika:\n')
    data = ser.readline().decode('utf-8').strip()
    isRead = False

    if data == 'start':
        print('started')
        isRead = True
        data_arr = []
        data_records = [] 
        start_time = time.time()
    
    while isRead:
        data = ser.readline().decode('utf-8').strip()

        if data == 'end':
            isRead = False
            print(data_arr)
            if data_records:
                file_name = get_filename()
                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Time', 'Value'])
                    writer.writerows(data_records)
        else:
            val = int(data)
            timestamp = time.strftime('%H:%M:%S')
            data_records.append([timestamp, val])
            data_arr.append(val)

    