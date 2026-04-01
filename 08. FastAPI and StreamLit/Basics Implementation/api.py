from fastapi import FastAPI 

app = FastAPI()

# csv
# df = 
# df(

@app.get("/get-survival-rates")
async def get_survival():
    # df[]
    # df []

    return {}
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def get_items():
    return [{
        "name":"item 1"
    },
    {
        "name":"item 2"
    }]