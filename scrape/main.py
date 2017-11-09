
import NYT_API

def run():

	mydata = []
	NYT_API.get_data("condition+of+anonymity", mydata)

	print("=="*20, "IN YOUR TESTER SCRIPTER", "=="*20)

	print(len(mydata))
	print(mydata[0])

	for item in mydata:
	    print(item["web_url"], item["body"])
	    print("__"*10)

	return


if __name__ == '__main__':

	run()