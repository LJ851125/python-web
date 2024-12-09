from flask import Flask

from unwrap import app
from unwrap.email import email_bp
from unwrap.user.routes import user_bp
from unwrap.admin.routes import admin_bp





app.register_blueprint(user_bp)
app.register_blueprint(admin_bp,url_prefix="/admin")
app.register_blueprint(email_bp)
if __name__ == '__main__':
    app.run(debug=True)