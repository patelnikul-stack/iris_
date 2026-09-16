import streamlit as st

st.title('Bar Island')
st.subheader('welcomme to Bar Island')

a=st.button("Make a Drink")

if a:
    st.success("your drink is being prepared")

b=st.checkbox('Add Ice')
if b:
    st.success("Ice has been adding to your drink")

c=st.selectbox('select your base',['milk','coconot water','toadi','alcohol','soft drink'])
if c:
    st.success("base has been add  to your drink")

d=st.slider("select your base in strenght",30,250,50)
if d:
    st.write(" you have select your base strenght")

e=st.radio("select your flavour",['chocolate','venila','mint','lime','without flavour'])
if e:
    st.write("your flavour has been added")

f=st.number_input("how manny number of spoon of sugar you want to add?",min_value=0,max_value=8,step=1)

g=st.text_input("enter your name")

if g:
    st.success(f' {g}, your drink is being prepared')

h=st.date_input("enter your dob",key="dob")

st.markdown("### we are planing to introdce two new drinks in the house, please vot for your fav drink")

clm1,clm2=st.columns(2)

with clm1:
    st.header("jamun chatpata")
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhrhzyD-aEv7IQvuODZrAzSt3A2a6qQxWF1OCEzEezlx2tnFt-pNkPRvY&s=10',width=200)
    v1=st.button("vote for jamun chatpata")

with clm2:
    st.header("mango jimjam")
    st.image('https://mydominicankitchen.com/wp-content/uploads/2021/07/Mango-Mojito-My-Dominican-Kitchen-6.jpg',width=200)
    v2=st.button("vote for mango jimjam")

if v1:
    st.success("you have voted for jamun chatpata")
else:
    st.success("you have voted  for mango jimjam")


st.sidebar.title("bar island's sidebar")
n=st.sidebar.number_input('how many drinks you want to order',min_value=1,max_value=10,step=1)
m=st.sidebar.text_input("enter your name")
o=st.sidebar.selectbox('select your base',['milk','coconot water','toadi','alcohol','soft drink'])
st.sidebar.text_input(f" thank you {m}  for your order of {n} drinks. your favourite drink {o}. we will prepare it for you shortly!  ")

with st.expander("insructions for drinks"):
    st.write("1.select my base drink as fresh as new")
    st.write("2. use flovaur as per your choice")
    st.write("3. drink should not be chill and must be not be at room tempreture")
