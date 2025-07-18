from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 仮の収入データ保存用（本来はDB）
incomes = []

@app.route('/')
def index():
    return redirect(url_for('income_form'))

@app.route('/income', methods=['GET', 'POST'])
def income_form():
    if request.method == 'POST':
        income_name = request.form.get('income_name')
        income_amount = request.form.get('income_amount')

        # ここでDB登録の処理を入れる予定
        incomes.append({'name': income_name, 'amount': income_amount})
        return redirect(url_for('income_form'))

    return render_template('income_form.html', incomes=incomes)

if __name__ == '__main__':
    app.run(port = 2022)
