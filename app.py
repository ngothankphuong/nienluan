from flask import Flask, Response, session, request
from flask import Flask, render_template 
import numpy as np
import requests
import mysql.connector
from flask import Flask, request, redirect, url_for
import qrcode, cv2, os
from pyzbar.pyzbar import decode
from simhash import Simhash
import threading, time
from PIL import Image
import webbrowser
from flask import g 
from flask import current_app, flash, jsonify, make_response
from selenium import webdriver
import time
import subprocess
import pkg_resources
import httpx

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

url_scanned = set()
reset_lock = threading.Lock()

camera = cv2.VideoCapture(0)  

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="qr_python",
    port=3306,
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=['POST'])
def webhook():
    data = request.json
    userMess = data.get('message')
    print(userMess)
    rasa_response = requests.post(RASA_API_URL, json={'message': userMess})
    rasa_response.raise_for_status()
    rasa_response_json = rasa_response.json()
    print('Bot Response:', rasa_response_json[0]['text'])  # In ra phản hồi từ máy chủ RASA API
    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I didn\'t understand that.'
    # print(type(bot_response))
    return bot_response

@app.route("/create_page")
def viewCreate():
    return render_template("create.html")

@app.route("/login")
def login():
    return render_template("login.html")

# authentication & authorization
@app.route("/handleLogin", methods=['POST'])
def handleLogin():
    data = request.json
    inputEmail = data.get('inputEmail')
    inputPassword = data.get('inputPassword')
    mycursor = db.cursor()
    sql = "SELECT * FROM user WHERE email=%s"
    mycursor.execute(sql,(inputEmail,))
    myrs = mycursor.fetchall()
    print(myrs)
    print("TEN QUAN TRI LA", myrs[0][1])
    if(len(myrs) > 0 ):
        #dang nhap thanh cong
        if(inputEmail==myrs[0][2] and inputPassword==myrs[0][3]):
            #save session
            session['username'] = myrs[0][1]
            #in session
            username = session.get('username')
            print("NAME GET FROM SESSION ", username)
            return jsonify({'redirect_url': '/manage?name=' + username})
        #sai mat khau
        elif(inputEmail==myrs[0][2] and inputPassword!=myrs[0][3]):
            return jsonify({'redirect_url': '/login', 'mess': 'error_pass'})
    #khong ton tai email
    else:
        return jsonify({'redirect_url': '/login', 'mess':'no_user'})

@app.route("/forgotpassword")
def view_forgot_password():
    return render_template("forgotpassword.html")

#tim kiem ma QR
@app.route("/search")
def search_qr():
    mycursor = db.cursor()
    input_search = request.args.get('data')
    #
    sql = "SELECT * FROM diadiem WHERE ten LIKE %s"
    mycursor.execute(sql, ('%' + input_search + '%',))
    myrs = mycursor.fetchall()
    print(len(myrs))
    if(len(myrs) == 0):
        return render_template("search.html")
    else:
        return render_template("search.html", data_search=myrs)

#trang list ma qr
@app.route("/manage")
@app.route("/manage/<path:subpath>")
def viewManage(subpath=None):
    mycursor = db.cursor()
    sql = "SELECT * FROM diadiem"
    mycursor.execute(sql,)
    myrs = mycursor.fetchall()
    return render_template("manage.html", data_list = myrs)
    
#lay ra thong tin can chinh sua
@app.route("/getQR", methods=['POST'])
def editQR():
    mycursor = db.cursor()
    data = request.json
    #print(data)
    sql = "SELECT * FROM diadiem WHERE id=%s"
    mycursor.execute(sql, (data,))
    myresult = mycursor.fetchall()
    #print(myresult)
    return myresult
    
#chinh sua
@app.route("/saveUpdate", methods=['POST'])
def saveEdit():
    mycursor = db.cursor()
    data = request.json
    ten = data.get('ten_input')
    url_qr = data.get('url_input')
    str_id_qr = data.get('id_input')
    id_qr = int(str_id_qr)
    sql = "UPDATE diadiem SET ten=%s, url_google_map=%s WHERE id=%s"
    mycursor.execute(sql, (ten, url_qr, id_qr),)
    db.commit()
    return "OK"

def find_name_img(id):
    mycursor = db.cursor()
    data = (id,)
    sql = "SELECT ten_anh from diadiem WHERE id=%s"
    mycursor.execute(sql, data)
    myresult = mycursor.fetchall()
    return myresult[0][0]

@app.route("/del_item", methods=['POST'])
def del_item():
    mycursor = db.cursor()
    data = request.json
    id_item  = data.get('id_del')
    print(id_item)
    img_name = find_name_img(id_item) + ".png"

    #xoa luon hinh anh khi delete trong db
    if img_name:
        img_path = os.path.join(app.static_folder, 'QRCODE', img_name)
        if os.path.exists(img_path):
            os.remove(img_path)
            print("Đã xóa tệp ảnh:", img_path)
        else:
            print("Tệp ảnh không tồn tại:", img_path)
    #xoa trong db
    sql = "DELETE FROM diadiem WHERE id = %s"
    i = (id_item,)
    mycursor.execute(sql, i)
    db.commit()
    return "OK"
    
def reset_url_scanned():
    global url_scanned
    while True:
        time.sleep(10)
        with reset_lock:
            url_scanned.clear()
reset_thread = threading.Thread(target=reset_url_scanned)
reset_thread.daemon = True
reset_thread.start()

#QUET MA BANG CAMERA
def generate_frames():
    global url_scanned
    result_scan= ""
    while True:
        success, frame = camera.read() 
        if not success:
            break
        else:
            decoded_objects = decode(frame)
            for obj in decoded_objects:
                result_scan = obj.data.decode('utf-8')
                if result_scan not in url_scanned:
                    print("KET QUA SCAN LA", result_scan)
                    getURL(result_scan)
                    url_scanned.add(result_scan)
                    #alert code in html
                    #alert_code = "<script>alert('SCAN SUCCESS');</script>"
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'  b'Content-Type: image/jpeg\r\n\r\n' + frame )
@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame') 

#lay ma qr tu db
def getURL(code):
    mycursor = db.cursor()
    sql = "SELECT url_google_map FROM diadiem WHERE code = %s"
    mycursor.execute(sql, (code, ))
    myresult = mycursor.fetchall()
    if (myresult == []):
        return "CODE INVALID"
    else :
        data= myresult[0][0]
        webbrowser.open_new(data)
        return "SCAN SUCCESS"

#bat camera
@app.route("/on_cam", methods=["POST"])
def start_camera():
    global camera
    camera = cv2.VideoCapture(0)
    return "start"

#tat camera
@app.route("/off_cam", methods=["POST"])
def stop_camera():
    global camera
    if camera:
        camera.release()  
        cv2.destroyAllWindows() 
    return "stop"

@app.before_request
def before_request():
    g.message = None

#tao ma qr
@app.route("/create", methods=["POST"])
def createQRCode():
    name = request.form.get("input_name")
    location = request.form.get("input_location")
    img_name = request.form.get("input_name_img")
    #print("Ten hinh"+ img_name)
    code = Simhash(location).value
    #print("code la " + str(code) )
    if(checkExist(code) == False):
        data = code
        img = qrcode.make(data)
        print("IMG TRONG TAO MA QR ",img)
        path_save = "static/QRCODE/" + img_name
        img.save(path_save+'.png')
        mycursor = db.cursor()
        sql = "INSERT INTO diadiem (ten, url_google_map, code, ten_anh)  VALUES (%s, %s, %s, %s)"
        val = (name, location, code, img_name)
        mycursor.execute(sql, val)
        db.commit()
        message_success = "Thành công"
        return render_template("create.html", message_success = message_success)
    else : 
        print("Khong them vao db")
        message_exist = "Đã tồn tại"
        return render_template("create.html", message_exist = message_exist)
    
def checkExist(code):
    mycursor = db.cursor()
    sql = "SELECT * FROM diadiem WHERE code=%s"
    mycursor.execute(sql, (code, ))
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else :
        return False
    
def allowed_file(filename):
    # Kiểm tra tệp có phải là hình ảnh hay ko 
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

#quet ma bang hinh anh
# @app.route("/scanimage", methods=["POST"])
# def scan_img():
#     file = request.files['scan_img']
#     if file.filename == '':
#         return 'No selected file'
#     if file and allowed_file(file.filename):
#         # lưu hình vào static/scan_img
#         file_path = 'static/scan_img/' + file.filename
#         file.save(file_path)
        
#         img = cv2.imread(file_path)
#         detect = cv2.QRCodeDetector()
        
#         #value cua ma qr quet duoc
#         value, points, straight_qrcode = detect.detectAndDecode(img)
#         print("VALUE TU MA QR",value)
#         if value != "":
#             print("Day la ma QR")
#         # if value != None:
#         #     sql = "SELECT url_google_map FROM diadiem WHERE code=%s"
#         #     mycursor = db.cursor()
#         #     mycursor.execute(sql, (value,))
#         #     myresult = mycursor.fetchall()
#         #     print(myresult)
#         #     data = myresult[0][0]
#         #     print(data)
#         #     webbrowser.open_new(data)
#     return redirect("/")
    #return render_template("create.html", data=value)
    
    
from io import BytesIO
import cv2

@app.route("/scanimage", methods=["POST"])
def scan_img():
    file = request.files['scan_img']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        # Đọc dữ liệu hình ảnh từ request
        img_bytes = file.read()
        # Tạo buffer từ dữ liệu hình ảnh
        buffer_img = BytesIO(img_bytes)
        # Đọc hình ảnh từ buffer
        img = cv2.imdecode(np.frombuffer(buffer_img.read(), np.uint8), cv2.IMREAD_COLOR)
        
        detect = cv2.QRCodeDetector()
        
        # Giải mã mã QR từ hình ảnh
        value, points, straight_qrcode = detect.detectAndDecode(img)
        print("VALUE TU MA QR:", value)
        #la ma QR
        if value != "":
            print("Đây là mã QR", value)
            # truy xuat csdl ma QR
            sql = "SELECT url_google_map FROM diadiem WHERE code=%s"
            mycursor = db.cursor()
            mycursor.execute(sql, (value,))
            myresult = mycursor.fetchall()
           
            #print("KET QUA TRUY XUAT LA",myresult)
            if(myresult == []):
                print("TRUY XUAT DU LIEU KO CO")
            else :
                #va co trong csdl
                print("TRUY XUAT DU LIEU THANH CONG")
                data = myresult[0][0]
                webbrowser.open_new(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
