TEST_USERNAME='...@...'  # full user, with domain in "email format"
TEST_PASSWORD='******'
TEST_CLIENT_ID='...-...-...'  # application guid created in the partner portal


import nms_csp


client = nms_csp.CspClient(TEST_USERNAME, TEST_PASSWORD, TEST_CLIENT_ID)
client.login()
print client._get_customers_raw()
