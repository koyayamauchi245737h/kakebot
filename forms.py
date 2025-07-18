from wtforms import Form
from wtforms.fields import (
    StringField, IntegerField, DateField, SelectField, TextAreaField, SubmitField
)
from wtforms.validators import DataRequired, NumberRange, Optional

# 収入登録フォーム
class IncomeForm(Form):
    # 収入の種類（固定 or 変動）
    income_type = SelectField(
        '収入の種類',
        choices=[('fixed', '固定収入'), ('variable', '変動収入')],
        validators=[DataRequired()]
    )
    # 収入名（例：給与、奨学金）
    name = StringField('収入名', validators=[DataRequired()])
    # 金額
    amount = IntegerField('金額', validators=[DataRequired(), NumberRange(min=0, message='0以上の数値を入力してください')])
    # 収入日付（変動収入の場合は必須、固定収入は自動登録想定なので任意）
    date = DateField('日付', format='%Y-%m-%d', validators=[Optional()], render_kw={"placeholder": "yyyy-mm-dd"})
    # メモ（任意）
    note = TextAreaField('メモ', validators=[Optional()])
    # 送信ボタン
    submit = SubmitField('登録')

# 支出登録フォーム
class ExpenseForm(Form):
    # 支出の種類（固定 or 変動）
    expense_type = SelectField(
        '支出の種類',
        choices=[('fixed', '固定支出'), ('variable', '変動支出')],
        validators=[DataRequired()]
    )
    # 支出名（例：家賃、食費）
    name = StringField('支出名', validators=[DataRequired()])
    # 金額
    amount = IntegerField('金額', validators=[DataRequired(), NumberRange(min=0, message='0以上の数値を入力してください')])
    # 支出日付（変動支出は必須、固定支出は任意）
    date = DateField('日付', format='%Y-%m-%d', validators=[Optional()], render_kw={"placeholder": "yyyy-mm-dd"})
    # メモ（任意）
    note = TextAreaField('メモ', validators=[Optional()])
    # 送信ボタン
    submit = SubmitField('登録')
