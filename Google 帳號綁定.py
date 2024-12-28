@app.route('/google_login')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get("/oauth2/v1/userinfo")
    if resp.ok:
        info = resp.json()
        email = info["email"]
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email, username=email.split('@')[0], google_id=info["id"])
            db.session.add(user)
            db.session.commit()
        login_user(user)
        flash('成功透過 Google 登入!', 'success')
        return redirect(url_for('dashboard'))
    flash('Google 登入失敗!', 'danger')
    return redirect(url_for('login'))
