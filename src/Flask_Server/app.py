import sqlite3
import flask
from flask import request, jsonify
import json
from datetime import date, time, datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/select_mois_data', methods=['POST'])
def select_mois_data():
	data = request.data.decode("utf-8")
	cur_data = json.loads(data)
	print(cur_data)
	conn = sqlite3.connect('aiscmm.db')
	sql1 = conn.execute("SELECT raspberry_id from user_login where email=?",(cur_data['email'],))
	email = []
	for x in sql1:
		email = x[0]
	cursor = conn.execute("SELECT * from current_status where raspberry_id=?",(email,))
	mois_data = []
	for row in cursor:
		mois_data.append(row[2])
	print(mois_data)
	json_obj = {"mois_data":mois_data}
	cursor = conn.execute("SELECT * from current_status")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], "\n")
	conn.close()

	return jsonify(json_obj)

@app.route('/update_mois_data', methods=['GET'])
def update_mois_data():
	data = request.json
	cur_data = json.loads(data)
	print(cur_data)
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("UPDATE current_status set moisture_avg=? where raspberry_id=? and pump_id=?",(cur_data['mois'], cur_data['raspberry_id'], cur_data['pump_id']))
	conn.commit()
	cursor = conn.execute("SELECT * from current_status")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], "\n")
	conn.close()

	return "Data updated"

@app.route('/select_ip', methods=['POST'])
def select_ip():
	today = str(date.today())
	data = request.data.decode("utf-8")
	mcu_data = json.loads(data)
	print(mcu_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("SELECT * from node_status_faulty where email=? and today_date=? ORDER BY today_date", (mcu_data["email"],today))
	print(result)
	mcu_list = []
	for row in result:
		mcu_list.append(row[2])
	json_obj = {"mcu_list":mcu_list}
	# for row in result:
	#    print("message = ", row[0], row[1], row[2], row[3], "\n")
	conn.close()
	return jsonify(json_obj)

@app.route('/delete_ip', methods=['GET'])
def delete_ip():
	today = str(date.today())
	data = request.json
	mcu_data = json.loads(data)
	#print(mcu_data)
	conn = sqlite3.connect('aiscmm.db')
	change = conn.execute("DELETE from node_status_faulty where email=?",(mcu_data["email"],))
	conn.commit();
	cursor = conn.execute("SELECT * from node_status_faulty")
	print(cursor)
	# for row in cursor:
	#    print("message = ", row[0], row[1], row[2], row[3], "\n")
	conn.close()

	return "Success"

@app.route('/insert_ip', methods=['GET'])
def insert_ip():
	today = str(date.today())
	data = request.json
	mcu_data = json.loads(data)
	print(mcu_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("INSERT INTO node_status_faulty VALUES(?, ?, ?, ?, ?, ?)", (mcu_data["email"],mcu_data["raspberry_id"],mcu_data["nodemcu_id"],mcu_data["raspberry_ip"],mcu_data["nodemcu_ip"], today))
	conn.commit()
	cursor = conn.execute("SELECT * from node_status_faulty")
	print(cursor)
	# for row in cursor:
	#    print("message = ", row[0], row[1], row[2], row[3], "\n")
	conn.close()

	return "Success"

@app.route('/update_gcm_token', methods=['GET'])
def update_gcm_token():
	today = str(date.today())
	data = request.json
	gcm_data = json.loads(data)
	print(gcm_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("UPDATE user_gcm_token set gcm_token=? where user_email=?", (gcm_data["email"], gcm_data["token"]))
	conn.commit()
	cursor = conn.execute("SELECT * from user_gcm_token")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], row[3], "\n")
	conn.close()

	return "Success"

@app.route('/predict_crops', methods=['POST'])
def predict_crops():
	data = request.data.decode("utf-8")
	user_data = json.loads(data)
	print(user_data)
	today = str(date.today())
	month = date.today().month
	if (month >= 6 and month <= 10):
		season = "Kharif"
	if (month >= 11 or month <= 3):
		season = "Rabi"
	if (month >= 4 and month <= 6):
		season = "Summer"
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("select * from farm_data where user_email=?",(user_data["email"],))
	soil_ph = ""
	districtid = ""
	for x in cursor:
		districtid = x[1]
	cursor2 = conn.execute("select * from District where districtid=?", (districtid,))
	soilid = ""
	for x in cursor2:
		soilid = x[2]
	print(soilid)
	cursor3 = conn.execute("select c.Cropid,c.Cropname from CropsBasics c,cropmap cm,CropReqQualities cr,prev_year_need pcn where cm.DistrictId=? and cr.SuitableSoilId=? and c.CropId=cm.CropId and cm.CropId=cr.CropId and pcn.CropId=c.CropId and prev_need>(select SUM(approximate_production) from user_crop_data ucd where ucd.CropId=cr.CropId and ucd.crop_sold=0)",(districtid, soilid))
	cropid = []
	cropname = []
	for x in cursor3:
		cropid.append(x[0])
		cropname.append(x[1])
	json_obj = {"cropid":cropid, "cropname":cropname}
	print(json_obj)
	return jsonify(json_obj)

@app.route('/add_manufacturing_company_details', methods=['POST'])
def add_manufacturing_company_details():
	today = str(date.today())
	data = request.data.decode("utf-8")
	m_data = json.loads(data)
	print(m_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("SELECT * from District where districtname=?", (m_data["region"],))
	district = ""
	for x in result:
		district = x[0]
	result2 = conn.execute("INSERT into manufacturing_company(user_email,company_name,districtid,company_address,contact_deails) values(?,?,?,?,?)", (m_data["email"],m_data["name"],district, m_data["address"], m_data["cnum"]))
	conn.commit()
	cursor = conn.execute("SELECT * from manufacturing_company")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], row[3], "\n")
	conn.close()

	return "Success"

@app.route('/update_ph', methods=['GET'])
def update_ph():
	today = str(date.today())
	data = request.json
	gcm_data = json.loads(data)
	print(gcm_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("UPDATE farm_data set SoilPh=? where user_email=@email", (gcm_data["ph"],gcm_data["email"]))
	conn.commit()
	cursor = conn.execute("SELECT * from farm_data")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], "\n")
	conn.close()

	return "Success"

@app.route('/get_water_status',methods=['POST'])
def get_water_status():
	today = str(date.today())
	data_str = request.data.decode("utf-8")
	data = json.loads(data_str)
	print(type(data),data)
	print("in get water method")
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("SELECT * from user_login where email=?", (data["email"],))
	print(result,type(result))
	test = ""
	for row in result:
		test = row[3]
	print(test)
	cursor = conn.execute("SELECT * from user_farm_data where update_date=? and raspberry_id=? order by update_time desc limit 1",(today,test))
	status = ""
	level = ""
	for row in cursor:
		status = row[3]
		level = row[6]
	json_obj = {"water_pump_status":status,"water_tank_level":level}
	print(json_obj)
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], "\n")
	conn.close()

	return jsonify(json_obj)

@app.route('/get_crops', methods=['POST'])
def get_crops():
	data = request.data.decode("utf-8")
	user_data = json.loads(data)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("select * from CropsBasics as cb,user_crop_data ucd where ucd.user_email=? and ucd.crop_sold=0 and cb.Cropid=ucd.CropId",(user_data["email"],))
	crop = []
	for x in cursor:
		crop.append(x[1])
	conn.close()
	json_obj = {"crop":crop}
	print(json_obj)
	return jsonify(json_obj)


@app.route('/get_current_farm_status',methods=['POST'])
def get_current_farm_status():
	today = str(date.today())
	print(today)
	data_str = request.data.decode("utf-8")
	data = json.loads(data_str)
	print(type(data),data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("SELECT raspberry_id from user_login where email=?", (data["email"],));
	test = ""
	for row in result:
		test = row[0]
	print(test)
	cursor = conn.execute("SELECT * from user_farm_data where update_date=? and raspberry_id=? order by update_time desc",(today,test))
	status = []
	temp = []
	mois = []
	level = []
	for row in cursor:
		temp.append(row[1])
		mois.append(row[2])
		status.append(row[3])
		level.append(row[6])
	print(cursor)
	json_obj = {"temp":temp,"mois":mois,"water_pump_status":status,"water_tank_level":level}
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], "\n")
	cursor = conn.execute("SELECT * from user_farm_data")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], "\n")
	conn.close()

	return jsonify(json_obj)

@app.route('/get_current_crops',methods=['GET'])
def get_current_crops():
	today = str(date.today())
	data = request.json
	user_data = json.loads(data)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("SELECT distinct cb.CropId, cb.Cropname from CropBasics as cb,user_crop_data ucd where ucd.user_email=? and ucd.crop_sold=0 and cb.Cropid=ucd.CropId", (user_data["email"],));
	print(result)
	Cropid =[]
	Cropname =[]
	for row in result:
		Cropid.append(result[0])
		Cropname.append(result[1])
	print("message = ", row[0], row[1], row[2], "\n")
	conn.close()
	json_obj = {"cropid":Cropid,"cropname":Cropname}
	return jsonify(json_obj)

@app.route('/add_new_crop', methods=['POST'])
def add_new_crop():
	data = request.data.decode("utf-8")
	crop_data = json.loads(data)
	print(user_data)
	today = str(date.today())
	month = date.today().month
	if (month >= 6 and month <= 10):
		season = "Kharif"
	if (month >= 11 or month <= 3):
		season = "Rabi"
	if (month >= 4 and month <= 6):
		season = "Summer"
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("select * from user_crop_data where user_email=? and season=? and crop_sold=0 and CropId=?",(user_data["email"],season, user_data["cropid"]))
	if cursor:
		msg = "Crop is already added.."
	cursor2 = conn.execute("insert into user_crop_data (user_email,CropId,season,crop_sold,approximate_production) values(?,?,?,?,?)", (user_data["email"], user_data["cropid"], season, 0, user_data["appx_prod"]))
	if cursor2:
		msg = "Crop added."
	return msg



@app.route('/add_new_crop_farmer',methods=['GET'])
def add_new_crop_farmer():
	today = str(date.today())
	month = date.today().month
	year = date.today().month
	data = request.data.decode("utf-8")
	user_data = json.loads(data)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("SELECT distinct cb.CropId, cb.Cropname from CropBasics as cb,user_crop_data ucd where ucd.user_email=? and ucd.crop_sold=0 and cb.Cropid=ucd.CropId", (user_data["email"],));
	print(result)
	Cropid =[]
	Cropname =[]
	for row in result:
		Cropid.append(result[0])
		Cropname.append(result[1])
	print("message = ", row[0], row[1], row[2], "\n")
	conn.close()
	json_obj = {"cropid":Cropid,"cropname":Cropname}
	return jsonify(json_obj)

@app.route('/add_appx_production',methods=['POST'])
def add_appx_production():
	today = str(date.today())
	data_str = request.data.decode("utf-8")
	data = json.loads(data_str)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("UPDATE user_crop_data set approximate_production=? where user_email=? and CropId=? and crop_sold=0", (data["apx_prod"],data["email"],data["cropid"]));
	print(result)
	return "success"

@app.route('/adduser',methods=['GET'])
def adduser():
	data = request.json
	user_data = json.loads(data)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("INSERT into user_login (email,raspberry_id,user_type) values(?, ?, ?)", (user_data["email"], user_data["raspberry_id"], user_data["user_type"]))
	conn.commit()
	cursor = conn.execute("SELECT * from user_login")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], row[1], row[2], "\n")
	conn.close()

	return "User added"

@app.route('/signin',methods=['GET'])
def signin():
	query_parameters = request.args
	email = query_parameters.get('email')
	print("In signin method",email)
	conn = sqlite3.connect('aiscmm.db')
	#cur = conn.cursor()
	user_type = 0
	cursor = conn.execute("SELECT * from user_login")
	print(cursor)
	for row in cursor:
		print("in for loop")
		print("message = ", row[0], "\n")
	cursor = conn.execute("SELECT * from user_login where email=?", (email,))
	print(cursor)
	for row in cursor:
		user_type = row[4]
		print(row[0])
		print("message = ", row[4], "\n")
	if (user_type == 0):
		user_type = -1
	conn.close()
	return jsonify(user_type)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.data.decode("utf-8")
	user_data = json.loads(data)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("insert into user_login(email,user_name,gender,user_type) values(?, ?, ?, ? )", (user_data["email"], user_data["name"], user_data["gender"], user_data["user_type"]))
	conn.commit()
	cursor = conn.execute("select * from user_login where email=?",(user_data["email"],))
	user_type = ""
	for x in cursor:
		user_type=x[4]
	print(user_type)
	json_obj = {"user_type":user_type}
	conn.close()
	return jsonify(json_obj)

@app.route('/add_farmer_details', methods=['POST'])
def add_farmer_details():
	data = request.data.decode("utf-8")
	user_data = json.loads(data)
	print(user_data)
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("SELECT * from District where districtname=?",(user_data["district"],))
	district = ""
	lat = 12.78
	log = 23.89
	for x in cursor:
		district = x[0]
	cursor2 = conn.execute("insert into farm_data(user_email,DistrictId,SoilPh,water_tank_height,farm_address,contact_number,farm_lat,farm_long) values(?, ?, ?, ?, ?, ?, ?, ?)",(user_data["email"], district, user_data["soil_ph"], user_data["water_tank_height"], user_data["address"], user_data["phone_number"], lat, log))
	conn.commit()
	cursor3 = conn.execute("select * from raspberry_map where raspberry_unique_name=?",(user_data["raspberry_id"],))
	ans = ""
	for i in cursor3:
		ans = i[0]
	cursor4 = conn.execute("update user_login set raspberry_id=? where email=?",(user_data["raspberry_id"],user_data["email"]))
	conn.commit()
	conn.close()
	return "success"


@app.route('/get_data', methods=['GET'])
def get_data():
	today = str(date.today())
	time = str(datetime.time(datetime.now()))
	print(type(today), type(time))
	data = request.json
	rpi_data = json.loads(data)
	print(rpi_data)
	conn = sqlite3.connect('aiscmm.db')
	result = conn.execute("INSERT into user_farm_data (raspberry_id,farm_soil_temp,farm_soil_mois,water_pump_status,update_date,update_time,water_tank_level) values(?, ?, ?, ?, ?, ?, ?)", (rpi_data["raspberry_id"], rpi_data["temp"],rpi_data["mois"], rpi_data["water_tank_status"], today, time, rpi_data["water_tank_level"]))
	conn.commit()
	cursor = conn.execute("SELECT * from user_farm_data")
	print(cursor)
	#for row in cursor:
	   #print("message = ", row[0], row[1], row[2], row[3], row[4], row[5], row[6], "\n")
	conn.close()
	#show_data()


	return "Success"


@app.route('/rpi/data', methods=['GET'])
def get_nmcu_data():
	data = request.json
	#print(json_data)
	abc = json.loads(data)
	print("data")
	print(abc["1"])
	#print(data["1"])
	conn = sqlite3.connect('aiscmm.db')
	#print(data)
	abc = conn.execute("INSERT INTO DATA (MSG) VALUES (?);", (abc["1"],));
	conn.commit()
	cursor = conn.execute("SELECT * from DATA")
	print(cursor)
	for row in cursor:
	   print("message = ", row[0], "\n")
	conn.close()
	#show_data()


	return "Success"
# @app.route('/get_bids_farmer', methods=['POST'])
# def get_bids_farmer():


@app.route('/set_new_bid', methods=['POST'])
def set_new_bid():
	data = request.data.decode("utf-8")
	user_data = json.loads(data)
	print(user_data)
	today = str(date.today())
	year = date.today().year
	bidid = user_data["cropid"]+":" + user_data["email"]
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("select * from farm_data where user_email=?",(user_data["email"],))
	district = ""
	for x in cursor:
		district = x[0]
	cursor2 = conn.execute("select * from set_crop_bid where bid_id=?",(bidid,))
	cursor2 = conn.execute("insert into set_crop_bid (user_email,CropId,approximate_production,rate_per_qtl,bid_locked,bid_id,DistrictId) values(?,?,?,?,?,?,?",(user_data["email"],user_data["cropid"],user_data["appx_prod"], user_data["rate_per_qtl"],0,bidid,district))
	conn.commit()
	conn.close()
	return "success"

@app.route('/mobile/data', methods=['GET'])
def send_data():
	conn = sqlite3.connect('aiscmm.db')
	cursor = conn.execute("SELECT * from DATA")
	cursor2 = conn.execute("SELECT * from DATA").fetchall()
	print(cursor)
	data = []
	for row in cursor:
	   print("message = ", row[0], "\n")
	   data.append(row[0])
	conn.commit()
	conn.close()
	print(jsonify(cursor2))
	return jsonify(cursor2)
	

app.run(host="192.168.43.104",port=5010)