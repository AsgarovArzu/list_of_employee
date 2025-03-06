import pandas as pd;
import sqlite3 
conn = sqlite3.connect("STAFF.db");

table_name = "INSTRUCTOR";
attribute_list = ["ID", "f_name", "l_name", "city", "c_code"];

file_path = "/home/asgarov/Desktop/IBM_DATA_ENGINEERING/Python_Project/Modul1/list_of_employee/INSTRUCTOR.csv";
df = pd.read_csv(file_path, names = attribute_list);
df.to_sql(table_name, conn, if_exists="replace", index=False);
print("Table is ready");

data_dict = {
    "ID":[89],
    "f_name":["Arzu"],
    "l_name":["Asgar"],
    "city":["Krakow"],
    "c_code":["PL"],
};

data_append = pd.DataFrame(data_dict);
data_append.to_sql(table_name,conn, if_exists = "append", index=False);
query_statement = f"SELECT f_name FROM {table_name}";
query_output = pd.read_sql(query_statement, conn);
print(query_statement);
print(query_output);
conn.close();