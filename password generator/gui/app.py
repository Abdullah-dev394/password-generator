from quart import *
import webview,threading,string,secrets,uvicorn,os
 
BASE_DIR=os.path.dirname(os.path.abspath(__file__))


app=Quart(__name__,template_folder=BASE_DIR)



@app.route("/")
async def home():
    return await render_template("index.html")


def generate_random(length=16,upper_letters=False,lower_letters=False,digits=False,symbols=False):
    all_symbols=""
    if upper_letters:
        all_symbols+=string.ascii_uppercase
    if lower_letters:
        all_symbols+=string.ascii_lowercase
    if symbols:
        all_symbols+=string.punctuation
    if digits:
        all_symbols+=string.digits
    if not all_symbols:
        return None
    return "".join(secrets.choice(all_symbols) for _ in range(length))


@app.route("/api/generate",methods=["POST"])
async def generate():
    data=await request.get_json(silent=True)

    if not isinstance(data,dict):
        return jsonify({"error":"Invalid format"}),400


    length=data.get("password_length",16)
    upper=data.get("upper",False)
    lower=data.get("lower",False)
    digits=data.get("digit",False)
    symbols=data.get("symbol",False)

    if not isinstance(length,int):
        return jsonify({"error":"Length must be integer!"}),400

    if not 6<=length<=64:
        return jsonify({"error":"Length must be between 6 and 64!"}),400

    for value in (upper,lower,digits,symbols):
        if not isinstance(value,bool):
            return jsonify({"error":"Incorrect type"}),400
               

    password=generate_random(
        length=length,
        upper_letters=upper,
        lower_letters=lower,
        digits=digits,
        symbols=symbols
    )

    if not password:
        return jsonify({"error":"Please select at least one option!"}),400

    return jsonify({"password":password})

def run_backend():
    uvicorn.run(app,port=36048)


if __name__=="__main__":
    threading.Thread(target=run_backend,daemon=True).start()
    webview.create_window(
    "Password generator",
    "http://127.0.0.1:36048",
    width=400,
    height=700,
    min_size=[400,700])
    webview.start(gui="edgechromium")
