@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@fapp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if User.query.filter_by(email=email).first():
            flash('Email 已被註冊!', 'danger')
            return redirect(url_for('register'))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('註冊成功，請登入!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('無效的帳號或密碼!', 'danger')
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return f'歡迎 {current_user.username}! 這是您的個人頁面。'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('已成功登出!', 'success')
    return redirect(url_for('login'))

//app log connec wix.com 
