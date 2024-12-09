from flask import render_template, request, redirect, url_for, flash, Blueprint
from . import email_bp


@email_bp.route('/interface', methods=['GET', 'POST'])
def interface():
    form_data = {}
    if request.method == 'POST':
        form_data['name'] = request.form.get('name')
        form_data['email'] = request.form.get('email')
        form_data['message'] = request.form.get('message')

        # 验证表单数据
        errors = []
        if not form_data['name']:
            errors.append('姓名不能为空')
        if not form_data['email']:
            errors.append('邮箱不能为空')
        if not form_data['message']:
            errors.append('留言不能为空')

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('interface.html', form=form_data)
        else:
            # 在这里可以进行数据存储操作，例如存入数据库
            flash('表单提交成功！', 'success')
            return redirect(url_for('email.success'))
    return render_template('interface.html', form=form_data)

@email_bp.route('/success')
def success():
    return render_template('success.html')