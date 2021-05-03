import requests

# Add one line to the sheet
def write(data):
	requests.post(
		"https://sheet.best/api/sheets/99848db6-5bf3-402b-82b7-f3436219f299",data)
	return {
            "DONE"
    }
