import requests
import json

def send_message( text="텍스트 영역입니다. 최대 200자 표시 가능합니다."):
    with open('token.json' ,'r')as f:
        token_data = json.load(f)
    access_token= token_data['access_token']
    
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {access_token}"
    }

    template_object = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://naver.com",
            "mobile_web_url": "https://naver.com"
        },
        "button_title": "바로 확인"
    }

    data = {
        'template_object': json.dumps(template_object)
    }

    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return False

if __name__ == "__main__":
    # token.json에서 가져온 access token 사용
    result = send_message("카카오 메시지 테스트입니다!")
    print("메시지 전송 성공" if result else "메시지 전송 실패")
