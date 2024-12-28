@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            token = serializer.dumps(email, salt='reset-password')
            reset_link = url_for('reset_password', token=token, _external=True)
            msg = Message('重設密碼連結', recipients=[email])
            msg.body = f'點擊以下連結重設密碼: {reset_link}'
            mail.send(msg)
            flash('重設密碼連結已發送至您的 Email!', 'info')
        else:
            flash('Email 不存在!', 'danger')
        return redirect(url_for('login'))
    return render_template('forgot_password.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = serializer.loads(token, salt='reset-password', max_age=3600)
    except SignatureExpired:
        flash('連結已過期!', 'danger')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        user = User.query.filter_by(email=email).first()
        new_password = request.form['password']
        user.password = new_password
        db.session.commit()
        flash('密碼重設成功!', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html')
