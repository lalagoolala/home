"""
WSGI entry point for production deployment.
This file is used by Heroku, Railway, and other PaaS platforms.
"""

import os
from app import app

if __name__ == "__main__":
    # 포트 설정 (Heroku는 PORT 환경 변수로 포트를 전달)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
