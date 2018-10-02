from app import app
from app.mainSNP import filterURLs

@app.route('/')
def index():
    input = 'https://www.dell.com/en-us/work/shop/dell-ultrasharp-34-curved-ultrawide-monitor-u3415w/apd/210-adtr/monitors-monitor-accessories'
    filterURLs(input)
    return 'SNP'
