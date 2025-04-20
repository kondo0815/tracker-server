from flask import Flask, request, redirect
from datetime import datetime
import csv
import os
from urllib.parse import unquote

app = Flask(__name__)
LOG_FILE = "click_log.csv"

@app.route("/")
def track():
    tracking_id = request.args.get("id", "unknown")
    tracking_type = request.args.get("type", "unknown")
    target_url = request.args.get("target", "")

    # target_url をデコード（URLエンコードされた文字列を元に戻す）
    target_url = unquote(target_url)

    # ログファイルがなければ作成
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("timestamp,id,type,target\n")

    # CSVに書き込み
    with open(LOG_FILE, "a") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), tracking_id, tracking_type, target_url])

    # 安全なリダイレクト
    if target_url.startswith("http://") or target_url.startswith("https://"):
        return redirect(target_url)
    else:
        return "Invalid redirect URL", 400

# Render用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
