import sys
from collections import defaultdict
import re

def parse_log_line(line: str) -> dict:
    ''' парсить стрічку логу по пробілам, перед парсінгом перевіряє патерн по регулярному виразу '''
    if not re.match(r'(\d{4}(?:-\d{2}){2} \d{2}(?::\d{2}){2}) (DEBUG|ERROR|INFO|WARNING) (.*)',line):
        return None
    date,time,level,*message = line.split(' ')
    return {'date':date,'time':time,'level':level,"message":' '.join(message)}

def load_logs(file_path: str) -> list:
    ''' читає файл і зразу передає кожну стрічку парсеру, повертає розпарсений список логу '''
    with open(file_path,"r+") as logfile:
        lines=list(filter(lambda x: x is not None,(map(parse_log_line,logfile.readlines()))))
    return lines

def filter_logs_by_level(logs: list, level: str) -> list:
    ''' фільтрує стрічки списку по полю level і повертає відфільтрований список '''
    return list(filter(lambda x: x['level']==level,logs))

def count_logs_by_level(logs: list) -> dict:
    ''' рахує стрічки логу у списку по кількості значень у полі level, повертає словник з підрахованими значеннями счетчика'''
    cntr=defaultdict()
    cntr.default_factory=int  
    for log in logs:
        cntr[log['level']]+=1
    return dict(cntr)

def display_log_counts(counts: dict):
    ''' друкує статистику по логу по рівням логування (полю level) '''
    print(f"{'Рівень логування ':20}| Кількість ")
    print(f"{'-'*20}|{'-'*10}")
    print("\n".join(list(map(lambda x:f"{x:20}| {counts[x]}",counts))))

if __name__=="__main__":
    ''' Головна програма, читає файл, перевіряє на формат, парсить, виводить статистику по рівням логування розпарсеного логу, 
    додатково показує деталі для обраного в параметрах рівня, якщо він вказаний в параметрах запуску'''
    logs=load_logs(file_path=sys.argv[1])
    display_log_counts(count_logs_by_level(logs))
    if len(sys.argv)==3:
        print()
        print(f"Деталі логів для рівня '{sys.argv[2]}':")
        print(''.join(map(lambda x:f"{x['date']} {x['time']} - {x['message']}",filter_logs_by_level(logs,sys.argv[2]))))
    