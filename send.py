# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = "ACc28176d4cb4243b5a556cf569a094733"
auth_token = "c4d2135dce73a4d57449ccd4334aa721"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+886900222946",
    from_="+13362038608",
    body="Hello there!")
