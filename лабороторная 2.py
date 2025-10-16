'''
#1
password = input ("введите пооль: ")
if len ( password ) < 8 : # сли проль меньше 8
    print (" слишом коротки пороль ")
if len (password ) >= 8: #проь равн или больше 8
    print (" пороль принят")
'''
''''
#2
status = input (" ведите статус сервера (online/offline):")
if status == "online":
    print (" вязь установлна")
else:
    print ("связь потеряна ")
'''
#3
'''
try:
    threat_level = int (input( "дите уровень угрозы (1-100): "))
    if 1 <= threat_level <= 30:
        print( " низкий уровень угрозы ")
    elif 31 <= threat_level <= 70 :
        print ("срдний уровень угрозы")
    elif 71 <= threat_level <= 100:
        print (" кретичский уровнь угрозы")
    else:
        print ("оибка ввода")
except ValueError:
        print (" лееееее, надо от 1-100")
'''
'''
#4
checksum_original ="a1b2c3d4"
checksum_current ="a1b2c3d4"
status = "файл не изменен" if checksum_original == checksum_current else "файл поврежден"
print ("status")
#5
'''
'''
event_code = input ("ведие код события (ERR/ WRN/ INF): ")
match event_code:
    case "ERR":
         print ("ошибка системы")
    case "WRN":
        print (" предупреждение")
    case "INF":
        print (" инфо сооб")
    case _:
        print ("еизвестный код события")
'''