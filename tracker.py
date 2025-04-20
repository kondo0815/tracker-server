from flask import Flask, request, redirect
from datetime import datetime
import csv
import os

app = Flask(__name__)
LOG_FILE = "click_log.csv"

@app.route("/")
def track():
    tracking_id = request.args.get("id", "unknown")
    tracking_type = request.args.get("type", "unknown")
    target_url = request.args.get("target", "")

    # 保存先がなければ作成
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("timestamp,id,type,target\n")

    with open(LOG_FILE, "a") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().isoformat(), tracking_id, tracking_type, target_url])

    return redirect(target_url)

# 🚀 これがないとサーバーが起動しない！
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
