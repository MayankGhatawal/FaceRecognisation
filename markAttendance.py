# markAttendance.py

from datetime import datetime, timedelta

# Dictionary to store last attendance times
lastAttendanceTime = {}

def markAttendance(name):
    global lastAttendanceTime
    
    # Load lastAttendanceTime from a persistent storage (e.g., database) if needed
    
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0].strip())
        
        if name not in nameList:
            if name in lastAttendanceTime:
                last_attendance_time = lastAttendanceTime[name]
                time_diff = datetime.now() - last_attendance_time
                if time_diff < timedelta(hours=20):
                    print(f"{name} already marked attendance within the last 20 hours.")
                    return
            
            # Mark attendance
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tString},{dString}')
            
            # Update lastAttendanceTime
            lastAttendanceTime[name] = time_now
            
            # Persist lastAttendanceTime to a persistent storage (e.g., database) if needed
