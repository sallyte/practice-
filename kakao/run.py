import json
import time
from datetime import datetime
from send_message import send_message

def run():
    while True:
        # 현재 시각의 초
        current_second = datetime.now().second
        print(f"현재 시각: {current_second}초")
        
        try:
            # schedule.json 파일 읽기
            with open("schedule.json", "r", encoding="utf-8") as f:
                schedules = json.load(f)
                
            # 현재 시각에 해당하는 알림 찾기
            for schedule in schedules:
                schedule_time = schedule["time"]
                
                # time이 현재 초보다 크거나 같고, 현재 초+5보다 작은 경우
                if (current_second <= schedule_time < current_second + 5) or \
                   (current_second >= 55 and schedule_time < (current_second + 5) % 60):
                    message = schedule['description']
                    send_message(message)
                    
        except Exception as e:
            print(f"오류 발생: {str(e)}")
            
        # 5초 대기
        time.sleep(5)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n프로그램이 종료되었습니다.")
