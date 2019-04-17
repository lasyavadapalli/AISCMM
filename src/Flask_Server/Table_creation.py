#!/usr/bin/python

import sqlite3
from flask import request, jsonify
from datetime import date, time, datetime
import datetime

conn = sqlite3.connect('aiscmm.db')
print("Opened database successfully")

# conn.execute("Delete from user_farm_data where water_pump_status='off'")
# conn.commit()

today = str(date.today())
print(datetime.datetime.now())
cursor = conn.execute("SELECT * from user_farm_data where update_date=? and raspberry_id=? order by update_time desc limit 1",(today,1))
for x in cursor:
	print(x[0],x[1],x[2],x[3],x[4],x[5],x[6]) 
# conn.execute("delete from manufacturing_company where user_email='rashmipawar921@gmail.com'")
# conn.commit()

# conn.execute("delete from farm_data where user_email='rashmipawar921@gmail.com'")
# conn.commit()

# conn.execute("delete from user_login where email='rashmipawar921@gmail.com'")
# conn.commit()

# curson1 = conn.execute("SELECT * from District")
# for x in curson1:
# 	print(x[0], x[1], x[2])
# print("executed")

# curson2 = conn.execute("SELECT * from CropsBasics")
# for x in curson2:
# 	print(x[0], x[1], x[2], x[3])
# print("executed")

# #conn.execute("INSERT into user_crop_data values('rashmipawar921@gmail.com', 1, 1, 10, 0, 'Kharif')")

# curson2 = conn.execute("SELECT * from user_crop_data")
# for x in curson2:
# 	print(x[0], x[1], x[2], x[3], x[4])
# print("executed")

# curson3 = conn.execute("SELECT c.Cropid, c.Cropname from CropsBasics c, cropmap cm, CropReqQualities cr, prev_year_need pcn where cm.DistrictId=1 and cr.SuitableSoilId=1 and cm.CropId=cr.CropId and pcn.CropId=c.CropId")
# for x in curson3:
# 	print(x[0], x[1])
# print("executed")

# cursor = conn.execute("select c.Cropid,c.Cropname from CropsBasics c,cropmap cm,CropReqQualities cr,prev_year_need pcn where cm.DistrictId=1 and cr.SuitableSoilId=1 and c.CropId=cm.CropId and cm.CropId=cr.CropId and pcn.CropId=c.CropId and prev_need>(select SUM(approximate_production) from user_crop_data ucd where ucd.CropId=cr.CropId and ucd.crop_sold=0)")
# conn.commit()
# for x in cursor:
# 	print(x[0])
# 	print(x[1])
# conn.execute("DROP TABLE node_status_faulty")

# conn.execute("INSERT INTO user_farm_data VALUES(1, 30.50, 220.35, 'on', '2019-03-29', '9:00', 7.45)")
# conn.commit()

#conn.execute("CREATE TABLE current_status(raspberry_id INT NULL, pump_id INT NULL, moisture_avg REAL NULL); ")

# conn.execute("INSERT INTO current_status VALUES(1,30.0,313,'on','2019-03-18','16:7',20)")
# conn.commit()

#conn.execute("UPDATE user_farm_data set water_tank_level=10.34 WHERE raspberry_id='1'")

# conn.execute('''CREATE TABLE node_status_faulty
#          (email VARCHAR(20) NULL,
#          raspberry_id INT NULL,
#           nodemcu_id INT NULL,
#          raspberry_ip VARCHAR(20) NULL,
#          nodemcu_ip VARCHAR(20) NULL,
#          today_date TEXT NULL);''')
# print("Table created successfully")

# conn.execute('''CREATE TABLE user_farm_data
#          (raspberry_id REAL NULL,
#           farm_soil_temp REAL NULL,
#          farm_soil_mois REAL NULL,
#          water_pump_status CHAR(10) NULL,
#          update_date TEXT NOT NULL,
#          update_time TEXT,
#          water_tank_level REAL);''')
# print("Table created successfully")

# conn.execute("INSERT INTO user_farm_data VALUES(1,30.0,313,'on','2019-03-18','16:7',20)")
# conn.commit()

# conn.execute('''CREATE TABLE cropmap
#          (cropid INT NULL,
#           districtid INT NULL,
#          crop_priority INT NULL);''')
# print("Table created successfully")

# conn.execute('''CREATE TABLE CropReqQualities
#          (cropid INT NULL,
#           suitablesoilid INT NULL,
#          cropreqph REAL NULL,
#          cropreqtemp REAL NULL);''')
# print("Table created successfully")

# conn.execute('''CREATE TABLE user_login
#          (email VARCHAR(20) NULL,
#           user_name VARCHAR(20) NULL,
#          gender VARCHAR(20) NULL,
#          raspberry_id REAL NULL,
#          user_type INT NULL,
#          profile_complete VARCHAR(20) NULL);''')
# print("Table created successfully")

# conn.execute('''CREATE TABLE user_type
#          (user_type_id INT NULL,
#           user_type INT NULL);''')

# conn.execute('''CREATE TABLE CropsBasics
#          (cropid INT NULL,
#           cropname VARCHAR(20) NULL,
#          cropseason VARCHAR(20) NULL,
#          cropreqtime REAL NULL,
#          croptypeid INT NULL);''')

# conn.execute('''CREATE TABLE CropType
#          (croptype VARCHAR(20) NULL,
#          croptypeid INT NULL);''')

# conn.execute('''CREATE TABLE District
#          (districtid INT NULL,
#           districtname VARCHAR(20) NULL,
#          soilid INT NULL);''')

# conn.execute('''CREATE TABLE SoilBasics
#          (soilid INT NULL,
#           soiltype VARCHAR(20) NULL,
#          soilregion VARCHAR(20) NULL);''')

# conn.execute('''CREATE TABLE SoilQualities
#          (soilid INT NULL,
#           soilphlow REAL NULL,
#          soilphhigh REAL NULL,
#          soilmoisture REAL NULL,
#          soiltemperature REAL NULL,
#          soilwatercapacity REAL NULL,
#          soilminerals VARCHAR(20) NULL);''')

# conn.execute('''CREATE TABLE SoilBasics
#          (soilid INT NULL,
#           soiltype VARCHAR(20) NULL,
#          soilregion VARCHAR(20) NULL);''')

# conn.execute('''CREATE TABLE user_gcm_token
#          (user_email VARCHAR(20) NULL,
#           gcm_token VARCHAR(500) NULL);''')

# conn.execute('''CREATE TABLE farm_data
#          (user_email VARCHAR(20) NULL,
#          districtid INT NULL,
#          soilph REAL NULL,
#          water_tank_height REAL NULL,
#          farm_address VARCHAR(100) NULL,
#          contact_number INT(10) NULL,
#          farm_lat REAL NULL,
#          farm_long REAL NULL);''')

# conn.execute('''CREATE TABLE marketwise_crop_base_rate
#          (marketid INT NULL,
#           cropid INT NULL,
#           base_rate INT NULL);''')

# conn.execute('''CREATE TABLE user_crop_data
#          (user_email VARCHAR(20) NULL,
#          user_raspberry_id INT NULL,
#           cropid INT NULL,
#           approximate_production REAL NULL,
#           crop_sold REAL NULL,
#           season VARCHAR(20) NULL );''')

# conn.execute('''CREATE TABLE set_crop_bid
#          (user_email VARCHAR(20) NULL,
#           cropid INT NULL,
#           approximate_production REAL NULL,
#           rate_per_qtl REAL NULL,
#           bid_locked VARCHAR(20) NULL,
#           bid_id INT NULL,
#           districtid INT NULL,
#           manu_company_id INT NULL);''')

# conn.execute('''CREATE TABLE near_by_markets
#          (districtid INT NULL,
#          marketid INT NULL,
#          market_priority INT NULL);''')

# conn.execute('''CREATE TABLE manufacturing_company
#          (user_email VARCHAR(20) NULL,
#          company_name VARCHAR(20) NULL,
#          districtid INT NULL,
#          company_address VARCHAR(20) NULL,
#          contact_deails VARCHAR(20) NULL,
#          m_lat REAL NULL,
#          m_long REAL NULL);''')

# conn.execute('''CREATE TABLE markets
#          (marketid INT NULL,
#          market_name VARCHAR(20) NULL,
#          market_address VARCHAR(20) NULL,
#          market_lat REAL NULL,
#          market_long REAL NULL);''')

# conn.execute('''CREATE TABLE crop_rate
#          (cropid INT NULL,
#          marketid INT NULL,
#          rate INT NULL);''')

# conn.execute('''CREATE TABLE raspberry_map
#          (raspberry_id INT NULL,
#          raspberry_unique_name VARCHAR(20) NULL);''')

# conn.execute('''CREATE TABLE prev_year_need
#          (cropid INT NULL,
#          prev_need INT NULL);''')
# print("Table created successfully")
# print("Table created successfully")
# abc = conn.execute("DELETE FROM manufacturing_company WHERE user_email='rashmipawar921@gmail.com';");
# conn.commit()

# abc = conn.execute("DELETE FROM District WHERE districtname='Amravati';");
# conn.commit()

# abc = conn.execute("INSERT INTO District VALUES( 1, 'Amravati', 23)");
# conn.commit()
# print("data inserted")
cursor = conn.execute("SELECT * FROM prev_year_need").fetchall()
for row in cursor:
	print("in for loop")
	print("message = ", row[0], row[1], "\n")
conn.close()