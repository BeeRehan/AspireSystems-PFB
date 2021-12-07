import configparser

config = configparser.ConfigParser()


config['CARD'] = {"Number":"1234 1234 1234 1234",
                    "Pin":"1111",
                    "cvv":"123",
                    "OTP":"12121212"}


config['NET BANKING'] = {"username":"testuser",
                        "password":"test"}
config['GPAY']  = {"UPI ID":"mohamed@oksi",
                    "PIN":"1234"}

config['PHONEPAY']  = {"UPI ID":"1234567898@YPI",
                    "PIN":"1234"}

config['PAYTM']  = {"UPI ID":"mohamedpt@oksi",
                    "PIN":"1234"}


with open('config.ini', 'w') as configfile:
    config.write(configfile)
