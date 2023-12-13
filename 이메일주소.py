import re

def check_email(email):
    #raw string notation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.search(pattern, email):
        return True
    else:
        return False

# 10개의 샘플 이메일 주소
sample_emails = [
    'user@example.com',
    'example@email.co.uk',
    'my.email123@test.org',
    'test+spam@gmail.com',
    'invalid-email.com',
    'invalid@.com',
    'invalid@domain.',
    'invalid@.email.',
    'email_without_at.com',
    '@domain.com',
]

# 각 이메일 주소에 대한 검증 결과 출력
for email in sample_emails:
    if check_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")
