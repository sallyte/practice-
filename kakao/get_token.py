##토큰 만들기
import requests

def get_kakao_token(code):
    url ="https://kauth.kakao.com/oauth/token"

    data ={
        "grant_type": "authorization_code",
        "client_id":"ee7ae1a75fc33c5c2809a6c0730434ff",
        "redirect_uri":"https://localhost.com",
        "code":code
    }
    headers = {
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    
    response = requests.post(url, data=data, headers=headers)
    # print(response.json())
    
    if response.status_code == 200:
        token_json = response.json()
        return token_json
    else:
        return None


if __name__ == "__main__":
    # context에서 확인한 실제 인증 코드 사용
    auth_code = "VDiuUl0Z0nkGTqXU8SMVSAJssnCgNFz4492tpTyW3HJ_gSMlqQ6c3gAAAAQKPXKYAAABkyVIVodb9Pmr5eg_ZA"
    token_info = get_kakao_token(auth_code)
    print(token_info)
