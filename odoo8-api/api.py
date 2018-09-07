import xmlrpc.client 
import pprint
url = 'http://localhost:8600'
db = 'test'
username = "admin"
password = "mtotomdogo"

# Authenticate to the Server returns the UID needed in every call
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
uid = common.authenticate(db, username, password, {})

#Call this functions returns the objects that allows for model modification
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


# returns the Primary Key of the created
get_customers = models.execute_kw(
    db, uid, password, 'res.partner','search_read',
    [[['customer','=',True],['active','=',True]]],
    {'fields':['name','email','phone','street','city','zip','country_id'],
    }
)
for each in get_customers:
    print(each)





# query_one = models.execute_kw(db, uid, password,
#     'res.partner', 'check_access_rights',
#     ['read'], {'raise_exception': False})
# print('Q1 - >',query_one)

# # ids = models.execute_kw(db, uid, password,
# #     'res.partner', 'search',
# #     [[['is_company', '=', True], ['customer', '=', True]]],
# #     {'limit': 1})

# # [record] = models.execute_kw(db, uid, password,
# #     'res.partner', 'read', [ids])
# # # count the number of fields fetched by default
# # len(record)

# m = models.execute_kw( 
#     db, uid, password, 'res.partner', 'fields_get',
#     [], {'attributes': ['string', 'help', 'type']})
    
# # print('Q2 -> Fields get',m)


# print('Create Partener ->', get_customers)