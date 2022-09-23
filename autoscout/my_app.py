import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# sbar = st.sidebar.button("About Us")
# sbar = st.sidebar.button("Car Valuation")
# sbar = st.sidebar.button("EDA")
sbar = st.sidebar.radio("Navigation",["Car Valuation","About Us","EDA"])
sbar_img = f"""
    <style>
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("https://www.bugatti.com/fileadmin/_processed_/sei/p322/se-image-9001f5f7ae5cbec89f2ece1f7b98ba4d.webp");
    background-position: top left; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }} </style> """
st.markdown(sbar_img, unsafe_allow_html=True)


if sbar == "Car Valuation":

    html_temp = """
        <div style="background-color:#ea9999;
            padding:0px;border-radius:20px;margin:40px 0px;">
        <h2 style="color:white;text-align:center;"> Car Price Valuation </h2>
        </div>
        """
    # st.title("FREE CAR VALUATION")
    st.markdown(html_temp,unsafe_allow_html=True)

    df = pd.read_csv("./final_scout_not_dummy.csv")
    df = df[["make_model", "hp_kW", "km","age", "price", "Gearing_Type", "Gears"]]


    data_container = st.container()
    with data_container:
        a,b = st.columns(2)
        with a:
            car_model=st.selectbox("Car Model", df["make_model"].unique())
            gears=st.selectbox("Gears", sorted(df["Gears"].astype(int).unique()))
        with b:
            gearing_type=st.selectbox("Gearing Type", df["Gearing_Type"].unique())
            age=st.selectbox("Age", sorted(df["age"].astype(int).unique()))

    #slider
    hp = st.slider("Horse Power", min_value=int(df["hp_kW"].min()), max_value=int(df["hp_kW"].max()), value=80, step=1)

    km = st.slider("Mileage", min_value=int(df["km"].min()), max_value=int(df["km"].max()), value=20000, step=1)

    if car_model == "Audi A1":
        link = "https://cdn.euroncap.com/media/54606/audi-a1.png"
    elif car_model == "Audi A2":
        link="https://resources.compressor-express.com/images/brands2/audi-a2.png"
    elif car_model == "Audi A3":
        link="https://img0.icarros.com/dbimg/galeriaimgmodelo/7/27066_1.jpg"   
    elif car_model == "Opel Astra":
        link="http://cartem.net/wp-content/uploads/2021/09/000000000000000000000000.png"
    elif car_model == "Opel Corsa":
        link="https://www.rentscootercarzante.com/wp-content/uploads/2020/11/rent-car-zante-opel-corsa.jpg"
    elif car_model == "Opel Insignia":
        link="https://www.uzunrentacar.com/timthumb.php?src=/uploads/marka_images/orjopel-insignea-92.jpg&w=760&h=400&zc=2"
    elif car_model == "Renault Clio":
        link="https://uzunrentacar.com.tr/tema/rentacar/uploads/araclar/4-50-9-renault-clio.png"   
    elif car_model == "Renault Duster":
        link="https://wallpapercave.com/wp/wp2210669.jpg"
    elif car_model == "Renault Espace":
        link="https://img.autoabc.lv/Renault-Espace/Renault-Espace_2010_Minivens_15112734125_2.jpg"
    else:
        link = "https://cdn.euroncap.com/media/54606/audi-a1.png"
        
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url({link});
    background-size: 70%;
    background-position: center right;
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("https://www.bugatti.com/fileadmin/_processed_/sei/p322/se-image-9001f5f7ae5cbec89f2ece1f7b98ba4d.webp");
    background-position: top left; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    import pickle
    filename = 'my_model'
    model = pickle.load(open(filename, 'rb'))

    my_dict = {
        "make_model": car_model ,
        "hp_kW": hp,
        "km": km,
        "age" :age,
        "Gearing_Type":gearing_type,
        "Gears":gears
    }

    df=pd.DataFrame.from_dict([my_dict])
    pred = model.predict(df)

    df.columns=["Car Model", "Horse Power","Mileage","Age","Gearing Type","Gears"]
    st.table(df.loc[0,:])


    predict_style = f"""
        <div style="background-color:#073763;padding:10px;border-radius:10px;width: 10em;margin: auto">
        <h2 style="color:white;text-align:center;"> {str(int(pred[0]))+" $"} </h2>
        </div>
        """
    if st.button("Calculate Your Car Price"): 
        st.markdown(predict_style,unsafe_allow_html=True)
        

    m = st.markdown("""<style>
    div.stButton > button:first-child {
        background-color: #ea9999;
        color: white;
        height: 3em;
        width: 16em;
        border-radius:10px;
        font-size:20px;
        font-weight: bold;
        margin: auto;
        display: block;
    }

    div.stButton > button:hover {
        background:linear-gradient(to bottom, #ef7676 5%, #ef7676 100%);
        background-color:#ef7676;
    }
    div.stButton > button:active {
        position:relative;}
    <style>""", unsafe_allow_html=True)





elif sbar == "About Us":
    st.write("This web page is not yet complete ")
elif sbar == "EDA" : 
    st.write("This web page is not yet complete ")