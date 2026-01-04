personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
a=list(map(lambda x:{"name":x["name"],
                     "clearance":x["clearance"],
                     "category":(
"confidental" if 2<=x["clearance"]<=3 else "top secret" if x["clearance"]>=4 else "restricted")},personnel
                     ))
print(a)