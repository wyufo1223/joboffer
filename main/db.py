# -*-coding:utf-8-*-
import pymysql

DB_CONFIG = {
	'user': 'root', 
	'password': '',               
	'host': '127.0.0.1',	
	'charset': 'utf8mb4'
}

DB_NAME = 'joboffer'

CREATE_TABLE_JOB = """	
    CREATE TABLE IF NOT EXISTS `JOB`(
        `ID` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
        `MONTHLYSALARY` VARCHAR(100),
        `WORKINGPLACE` VARCHAR(100),
		`RELEASEDATE` VARCHAR(100),
		`JOBTYPE` VARCHAR(100),
		`WORKEXPERIENCE` VARCHAR(100),
		`LOWESTDEGREE` VARCHAR(100),
		`RECRUITMENTNUMBER` VARCHAR(100),
		`POSITIONCATEGORY` VARCHAR(100),
		`DEMAND` VARCHAR(10000)
    )ENGINE=INNODB DEFAULT CHARSET=UTF8;
"""

INSERT_TABLE_JOB = """
	INSERT INTO `JOB`(`MONTHLYSALARY`, `WORKINGPLACE`, `RELEASEDATE`, `JOBTYPE`, 
		`WORKEXPERIENCE`, `LOWESTDEGREE`, `RECRUITMENTNUMBER`, `POSITIONCATEGORY`, `DEMAND`)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
	    #VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)	 
def create_database():
	conn = pymysql.connect(**DB_CONFIG)
	cursor = conn.cursor()
	cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))

def get_db_conn():
	conn = pymysql.connect(database='joboffer', **DB_CONFIG)	
	return conn

def create_table_job():	
	get_db_conn().cursor().execute(CREATE_TABLE_JOB)
	
def insert_table_job(joboffer):
	conn = get_db_conn()	
	conn.cursor().execute(INSERT_TABLE_JOB, joboffer)
	conn.commit()


#create_database()

#create_table_job()

#joboffer = [1,2,3,4,5,6,7,8,9]
#insert_table_job(joboffer)




