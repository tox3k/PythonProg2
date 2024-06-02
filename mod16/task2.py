



#-------------requirements!!!!!!!!!!!!-----------------------
#----------install tabulate before running!------------------



import sqlite3
import tabulate

DATABASE = 'hw.db'

def select_all_orders():
    print('order_no\tpurchase_amount\tdate\tcustomer_id\tmanager_id')
    with sqlite3.Connection(DATABASE) as con:
        res = []
        cur = con.cursor()
        query = """SELECT customer.full_name, manager.full_name, purchase_amount, date FROM "order"
                    LEFT JOIN customer ON "order".customer_id = customer.customer_id
                    LEFT JOIN manager ON "order".manager_id = manager.manager_id"""
        orders = cur.execute(query)
        for order in orders:
            output = []
            for column in order:
                if column == None:
                    output.append('None')
                    continue
                output.append(str(column))
            res.append(output)
        print(tabulate.tabulate(res))

def select_customers_without_orders():
    with sqlite3.Connection(DATABASE) as con:
        res = []
        cur = con.cursor()
        query = """SELECT customer.full_name FROM customer
                    WHERE NOT EXISTS(SELECT * FROM "order" 
                    WHERE "order".customer_id = customer.customer_id)"""
        
        customers = cur.execute(query)
        for customer in customers:
            output = []
            for column in customer:
                if column == None:
                    output.append('None')
                    continue
                output.append(str(column))
            res.append(output)
        print(tabulate.tabulate(res))

def select_task3():
    
    with sqlite3.Connection(DATABASE) as con:
        res = []
        cur = con.cursor()
        query = """SELECT "order".order_no,manager.full_name, customer.full_name FROM "order"
                    LEFT JOIN manager ON manager.manager_id = "order".manager_id
                    LEFT JOIN customer ON customer.customer_id = "order".customer_id
                    WHERE NOT customer.city = manager.city"""
        
        customers = cur.execute(query)
        for customer in customers:
            output = []
            for column in customer:
                if column == None:
                    output.append('None')
                    continue
                output.append(str(column))
            res.append(output)
        print(tabulate.tabulate(res))

def select_task4():
    
    with sqlite3.Connection(DATABASE) as con:
        res = []
        cur = con.cursor()
        query = """SELECT order_no, customer.full_name FROM "order"
                    LEFT JOIN customer ON customer.customer_id = "order".customer_id
                    WHERE "order".manager_id IS NULL"""
        
        customers = cur.execute(query)
        for customer in customers:
            output = []
            for column in customer:
                if column == None:
                    output.append('None')
                    continue
                output.append(str(column))
            res.append(output)
        print(tabulate.tabulate(res))

def main():
    # select_all_orders()
    # select_customers_without_orders()
    # select_task3()
    select_task4()

if __name__ == '__main__':
    main()
