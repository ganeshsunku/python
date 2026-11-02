# API status handling

# You receive these HTTP status codes:
status_codes = [200, 401, 429, 503, 200]

def status_code_handling(status_code:int):
    if status_code==200:
        print("Success")
    elif status_code==401:
        print("Unauthorized")
    elif status_code==429:
        print("Rate Limited")
    elif status_code==503:
        print("Service Unavailable")

for status_code in status_codes:
    status_code_handling(status_code)



# Customer processing
customers = ["CustomerA", "CustomerB", "CustomerC"]
statuses = ["Active", "Inactive", "Active"]

def process_active_customers(customers, statuses):
    active_customers=[]
    for customer, status in zip(customers, statuses):
        if status == "Active":
            active_customers.append((customer, status))
    print(active_customers)

process_active_customers(customers, statuses)