# from quart import *
# import secrets,os,uvicorn,string

# BASE_DIR=os.path.dirname(os.path.abspath(__file__))

# FULL_PATH=os.path.join(BASE_DIR,"favicon.svg")

# app=Quart(__name__,template_folder="")

# @app.route("/")
# async def home():
#     return await render_template("index.html")


# @app.route("/favicon.svg")
# async def send_icon():
#     return await send_file(FULL_PATH,mimetype="image/svg+xml")

# def generate_random(length=16,upper_letters=False,lower_letters=False,digits=False,symbols=False):
#     all_symbols=""
#     if upper_letters:
#         all_symbols+=string.ascii_uppercase
#     if lower_letters:
#         all_symbols+=string.ascii_lowercase
#     if digits:
#         all_symbols+=string.digits
#     if symbols:
#         all_symbols+=string.punctuation
    
#     if not all_symbols:
#         return None
#     return "".join(secrets.choice(all_symbols) for _ in range(length))


# @app.route("/api/generate",methods=["POST"])
# async def generate():
#     data=await request.get_json()
#     length=data.get("password_length",16)
#     upper=data.get("upper",False)
#     lower=data.get("lower",False)
#     digits=data.get("digit",False)
#     symbols=data.get("symbol",False)

#     password=generate_random(
#         length=length,
#         upper_letters=upper,
#         lower_letters=lower,
#         digits=digits,
#         symbols=symbols
#     )

#     if not password:
#         return jsonify({"error":"Please select at least one option!"})
    
#     return jsonify({"password":password})

# if __name__=="__main__":
#     uvicorn.run(app,port=36048)
    


from color_tree import get_path_tree
import os

get_path_tree(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),colorful=False)
