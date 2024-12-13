from flask import Flask, render_template
from get_Data_from_hbase import get_last_record_from_hbase


app = Flask(__name__)


@app.route('/')
def index():
    last_record = get_last_record_from_hbase()
    return render_template('index.html',last_record=last_record)

@app.template_filter('format_currency')
def format_currency(value):
    try:
        # Chuyển float về int nếu có, để tránh số dư thập phân không mong muốn
        value = int(float(value))
        # Định dạng giá trị thành số với dấu `.`
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value


if __name__ == '__main__':
    app.run(debug=True)