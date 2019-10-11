from demo_app import app


# os.system("kill -9 `lsof -i :5000 -t | xargs`")

if __name__ == '__main__':
	app.run(debug=True)


