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
        `KEYWORD` VARCHAR(100),
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
	INSERT INTO `JOB`(`KEYWORD`, `MONTHLYSALARY`, `WORKINGPLACE`, `RELEASEDATE`, `JOBTYPE`, 
		`WORKEXPERIENCE`, `LOWESTDEGREE`, `RECRUITMENTNUMBER`, `POSITIONCATEGORY`, `DEMAND`)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

SELECT_TABLE_JOB = """
	SELECT 
		KEYWORD, MONTHLYSALARY, WORKINGPLACE, RELEASEDATE, JOBTYPE, 
		WORKEXPERIENCE, LOWESTDEGREE, RECRUITMENTNUMBER, POSITIONCATEGORY, DEMAND
	FROM `JOB`
	WHERE KEYWORD like %s
"""

	    	 
def create_database():
	conn = pymysql.connect(**DB_CONFIG)
	cursor = conn.cursor()
	cursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	cursor.close()
	conn.close()

def get_db_conn():
	conn = pymysql.connect(database='joboffer', **DB_CONFIG)	
	return conn

def create_table_job():	
	conn = get_db_conn()
	cursor = conn.cursor()
	cursor.execute(CREATE_TABLE_JOB)
	cursor.close()
	conn.close()

	
def insert_table_job(joboffer):
	conn = get_db_conn()
	cursor = conn.cursor()
	cursor.execute(INSERT_TABLE_JOB, joboffer)
	conn.commit()
	cursor.close()
	conn.close()

def select_table_job(searchkey):
	conn = get_db_conn()
	cursor = conn.cursor()
	cursor.execute(SELECT_TABLE_JOB, searchkey)
	values = cursor.fetchall()
	cursor.close()
	conn.close()
	return values
	
#create_database()

#create_table_job()

#cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
#insert_table_job(joboffer)

#select_table_job('java')




