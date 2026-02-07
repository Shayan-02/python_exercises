import time
from datetime import datetime

# کلاس برای ذخیره اطلاعات کاربر و وضعیت نشست‌ها
class ATM:
    def __init__(self):
        self.users = {}  # ذخیره کاربران به صورت {username: {password, role, balance, session}}
        self.sessions = {}  # ذخیره نشست‌ها به صورت {session_id: {username, timestamp}}
        self.session_counter = 1  # شناسه نشست‌ها
        self.logs = []  # ذخیره لاگ‌ها

    def log(self, level, message, timestamp):
        self.logs.append({
            'level': level,
            'message': message,
            'timestamp': timestamp
        })
        print(f"[{level}] {message}")

    def register(self, username, password, role, timestamp):
        if username in self.users:
            self.log("ERROR", "user already registered", timestamp)
        else:
            self.users[username] = {
                'password': password,
                'role': role,
                'balance': 0,
                'session': None,
                'last_login': timestamp
            }
            self.log("INFO", "user registered successfully", timestamp)

    def login(self, username, password, timestamp):
        if username not in self.users:
            self.log("ERROR", "invalid credentials", timestamp)
            return
        user = self.users[username]
        if user['password'] != password:
            self.log("ERROR", "invalid credentials", timestamp)
            return
        # اگر کاربر قبلاً وارد شده باشد، چک می‌کنیم که نشست قبلی منقضی شده یا خیر
        if user['session'] is not None:
            last_login_time = datetime.strptime(user['last_login'], "%Y/%m/%d:%H:%M:%S")
            time_diff = (datetime.strptime(timestamp, "%Y/%m/%d:%H:%M:%S") - last_login_time).seconds
            if time_diff <= 600:
                self.log("INFO", "already logged in", timestamp)
                return
            else:
                # نشست قبلی منقضی شده و باید حذف شود
                self.logout(user['session'], timestamp)
        
        # ایجاد نشست جدید
        session_id = self.session_counter
        self.session_counter += 1
        user['session'] = session_id
        user['last_login'] = timestamp
        self.sessions[session_id] = {
            'username': username,
            'timestamp': timestamp
        }
        self.log("INFO", "user logged in successfully", timestamp)

    def logout(self, session_id, timestamp):
        if session_id not in self.sessions:
            self.log("ERROR", "session expired or invalid", timestamp)
            return
        username = self.sessions[session_id]['username']
        del self.sessions[session_id]
        self.users[username]['session'] = None
        self.log("INFO", "user logged out", timestamp)

    def withdraw(self, session_id, amount, timestamp):
        if session_id not in self.sessions:
            self.log("ERROR", "session expired", timestamp)
            return
        username = self.sessions[session_id]['username']
        user = self.users[username]
        last_login_time = datetime.strptime(user['last_login'], "%Y/%m/%d:%H:%M:%S")
        time_diff = (datetime.strptime(timestamp, "%Y/%m/%d:%H:%M:%S") - last_login_time).seconds
        if time_diff > 600:
            self.log("ERROR", "session expired", timestamp)
            return
        if user['balance'] < amount:
            self.log("ERROR", "insufficient funds", timestamp)
            return
        user['balance'] -= amount
        self.log("INFO", "amount withdrawn successfully", timestamp)

    def deposit(self, session_id, amount, timestamp):
        if session_id not in self.sessions:
            self.log("ERROR", "session expired", timestamp)
            return
        username = self.sessions[session_id]['username']
        user = self.users[username]
        last_login_time = datetime.strptime(user['last_login'], "%Y/%m/%d:%H:%M:%S")
        time_diff = (datetime.strptime(timestamp, "%Y/%m/%d:%H:%M:%S") - last_login_time).seconds
        if time_diff > 600:
            self.log("ERROR", "session expired", timestamp)
            return
        user['balance'] += amount
        self.log("INFO", "amount deposited successfully", timestamp)

    def transfer(self, session_id, target_user, amount, timestamp):
        if session_id not in self.sessions:
            self.log("ERROR", "session expired", timestamp)
            return
        username = self.sessions[session_id]['username']
        user = self.users[username]
        last_login_time = datetime.strptime(user['last_login'], "%Y/%m/%d:%H:%M:%S")
        time_diff = (datetime.strptime(timestamp, "%Y/%m/%d:%H:%M:%S") - last_login_time).seconds
        if time_diff > 600:
            self.log("ERROR", "session expired", timestamp)
            return
        if target_user not in self.users:
            self.log("ERROR", "target user not found", timestamp)
            return
        if user['balance'] < amount:
            self.log("ERROR", "insufficient funds", timestamp)
            return
        user['balance'] -= amount
        self.users[target_user]['balance'] += amount
        self.log("INFO", "amount transferred successfully", timestamp)

    def log_query(self, level, start_time, end_time, timestamp):
        self.log("DEBUG", f"get log {level} {start_time} {end_time} {timestamp}", timestamp)
        logs_to_show = [log for log in self.logs if log['level'] == level]
        if start_time and end_time:
            start_time = datetime.strptime(start_time, "%Y/%m/%d:%H:%M:%S")
            end_time = datetime.strptime(end_time, "%Y/%m/%d:%H:%M:%S")
            logs_to_show = [log for log in logs_to_show if start_time <= datetime.strptime(log['timestamp'], "%Y/%m/%d:%H:%M:%S") <= end_time]
        if not logs_to_show:
            print("no logs found")
        else:
            for log in logs_to_show:
                print(f"{log['timestamp']} {log['level']} {log['message']}")

# تابع اصلی برای پردازش دستورات
def main():
    n = int(input())
    atm = ATM()

    for _ in range(n):
        line = input().strip().split()
        timestamp = line[-1]
        command = line[0]

        if command == 'register':
            _, username, password, role = line[1:5]
            atm.register(username, password, role, timestamp)
        elif command == 'login':
            _, username, password = line[1:4]
            atm.login(username, password, timestamp)
        elif command == 'logout':
            _, session_id = line[1:3]
            atm.logout(int(session_id), timestamp)
        elif command == 'withdraw':
            _, session_id, amount = line[1:4]
            atm.withdraw(int(session_id), int(amount), timestamp)
        elif command == 'deposit':
            _, session_id, amount = line[1:4]
            atm.deposit(int(session_id), int(amount), timestamp)
        elif command == 'transfer':
            _, session_id, target_user, amount = line[1:5]
            atm.transfer(int(session_id), target_user, int(amount), timestamp)
        elif command == 'log':
            level = line[1]
            if len(line) > 2:
                start_time, end_time = line[2:4]
                atm.log_query(level, start_time, end_time, timestamp)
            else:
                atm.log_query(level, None, None, timestamp)

if __name__ == "__main__":
    main()
