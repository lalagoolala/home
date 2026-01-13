from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from dotenv import load_dotenv
import pyrebase
import re
import os
from datetime import datetime

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
# 보안을 위해 환경 변수에서 키를 가져오거나, 없을 경우 기본값을 사용합니다.
app.secret_key = os.environ.get('SECRET_KEY', 'health_class_secret_key')

# 정적 파일 캐시 무효화 설정 (프로덕션에서도 캐시 비활성화)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True  # 템플릿 자동 새로고침

# HTTP 캐시 헤더 설정 - 무조건 새로 로드하도록 강제
@app.after_request
def set_no_cache(response):
    """브라우저 캐시 비활성화 - 항상 서버에서 최신 버전을 받도록"""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, public, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Last-Modified'] = datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')
    response.headers['ETag'] = None  # ETag 비활성화
    return response

# 캐시 무효화를 위한 버전 추가
app.version = datetime.now().strftime('%Y%m%d%H%M%S')

@app.context_processor
def inject_version():
    """모든 템플릿에서 사용할 수 있는 버전 정보 제공"""
    return {'version': app.version}

# Firebase 설정 (환경 변수에서 로드)
firebaseConfig = {
  "apiKey": os.environ.get('FIREBASE_API_KEY'),
  "authDomain": os.environ.get('FIREBASE_AUTH_DOMAIN'),
  "projectId": os.environ.get('FIREBASE_PROJECT_ID'),
  "storageBucket": os.environ.get('FIREBASE_STORAGE_BUCKET'),
  "messagingSenderId": os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
  "appId": os.environ.get('FIREBASE_APP_ID'),
  "databaseURL": os.environ.get('FIREBASE_DATABASE_URL')
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# 이메일 형식 검증
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 이메일로 사용자 조회
def find_user_by_email(email):
    try:
        users = db.child("users").get()
        if users.val():
            for user in users.each():
                if user.val().get("email") == email:
                    return user.val(), user.key()
    except Exception as e:
        print(f"사용자 조회 오류: {e}")
    return None, None

# 관리자 계정 확인 및 생성 함수
def create_admin():
    try:
        admin_email = "admin@health-class.com"
        user, _ = find_user_by_email(admin_email)
        
        if not user:
            print("관리자 계정을 생성합니다.")
            db.child("users").push({
                "name": "관리자",
                "email": admin_email,
                "password": "admin1234",
                "student_id": "관리자",
                "login_method": "email"
            })
    except Exception as e:
        print(f"관리자 계정 생성 중 오류: {e}")

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# Firebase 설정 정보 제공 (클라이언트에서 사용)
@app.route('/api/firebase-config')
def firebase_config():
    config = {
        "apiKey": os.environ.get('FIREBASE_API_KEY'),
        "authDomain": os.environ.get('FIREBASE_AUTH_DOMAIN'),
        "projectId": os.environ.get('FIREBASE_PROJECT_ID'),
        "storageBucket": os.environ.get('FIREBASE_STORAGE_BUCKET'),
        "messagingSenderId": os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
        "appId": os.environ.get('FIREBASE_APP_ID')
    }
    return jsonify(config)

# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()
            student_id = request.form.get('student_id', '').strip()
            
            # 입력값 검증
            if not name or not email or not password or not student_id:
                return render_template('signup.html', error="모든 필드를 입력해주세요.")
            
            if not is_valid_email(email):
                return render_template('signup.html', error="올바른 이메일 형식을 입력해주세요.")
            
            if len(password) < 6:
                return render_template('signup.html', error="비밀번호는 6자 이상이어야 합니다.")
            
            # 중복 이메일 확인
            existing_user, _ = find_user_by_email(email)
            if existing_user:
                return render_template('signup.html', error="이미 가입된 이메일입니다.")
            
            # 새 사용자 추가
            data = {
                "name": name,
                "email": email,
                "password": password,
                "student_id": student_id,
                "login_method": "email"
            }
            db.child("users").push(data)
            return redirect(url_for('login'))
        except Exception as e:
            print(f"회원가입 오류: {e}")
            return render_template('signup.html', error="회원가입 중 오류가 발생했습니다.")
    
    return render_template('signup.html')

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()
            
            if not email or not password:
                return render_template('login.html', error="이메일과 비밀번호를 입력해주세요.")
            
            # Firebase에서 사용자 조회
            user, _ = find_user_by_email(email)
            
            if user and user.get('password') == password:
                session['user_email'] = email
                session['user_name'] = user.get('name', '사용자')
                return redirect(url_for('index'))
            
            return render_template('login.html', error="이메일 또는 비밀번호가 틀렸습니다.")
        except Exception as e:
            print(f"로그인 오류: {e}")
            return render_template('login.html', error="로그인 중 오류가 발생했습니다.")
    
    return render_template('login.html')

# 구글 로그인 처리 (자바스크립트에서 호출)
@app.route('/google_login', methods=['POST'])
def google_login():
    try:
        data = request.json
        user_name = data.get('username')
        email = data.get('email')
        
        if not email:
            return jsonify({"error": "Invalid email"}), 400
        
        # DB에 사용자가 있는지 확인 (이메일 기준)
        user, _ = find_user_by_email(email)
        
        if not user:
            # 구글 로그인으로 처음 접속한 경우 DB에 자동 저장
            new_user = {
                "name": user_name,
                "email": email,
                "password": "google_oauth_user",
                "student_id": "구글계정",
                "login_method": "google"
            }
            db.child("users").push(new_user)
        
        session['user_email'] = email
        session['user_name'] = user_name
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"구글 로그인 오류: {e}")
        return jsonify({"error": "Login failed"}), 500

# 로그아웃
@app.route('/logout')
def logout():
    session.pop('user_email', None)
    session.pop('user_name', None)
    return redirect(url_for('index'))

# 게시판 (공지사항 및 질의응답)
@app.route('/board/<board_type>')
def board(board_type):
    if board_type not in ['notice', 'qna']:
        return redirect(url_for('index'))
    
    board_name = "공지사항" if board_type == 'notice' else "질의응답"
    
    try:
        # Firebase에서 데이터 가져오기
        posts_data = db.child("posts").get()
        posts = []
        
        if posts_data.val():
            for item in posts_data.each():
                val = item.val()
                if val.get("type") == board_type:
                    # 템플릿 호환을 위해 튜플 형태로 변환 (제목, 작성자, 내용)
                    posts.append((val.get("title"), val.get("author"), val.get("content")))
        
        return render_template('board.html', board_name=board_name, posts=posts, board_type=board_type)
    except Exception as e:
        print(f"게시판 오류: {e}")
        return render_template('board.html', board_name=board_name, posts=[], board_type=board_type, error="게시판을 불러올 수 없습니다.")

if __name__ == '__main__':
    create_admin() # 앱 시작 시 관리자 계정 확인/생성
    
    # 포트 설정 (로컬 개발용)
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)