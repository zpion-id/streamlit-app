# import module
import streamlit as st

# Title
st.title("Hello saya streamlit !!!")

# Header
st.header("ini adalah sebuah header")

# Subheader
st.subheader("Ini adalah subheader")

# Text
st.text("ini adalah teks !!!")

# Markdown
st.markdown("### ini dalam format markdown")

# success
st.success("Success")

# success
st.info("Information")

# success
st.warning("Warning")

# success
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Mencoba membagi dengan nol")
st.exception(exp)

# Write text
st.write("menulis teks dengan perintah write")

# Writing python inbuilt function range()
st.write(range(10))

# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)


# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

	# display the text if the checkbox returns True value
	st.text("Menampilkan widget widget")

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")

# Selection box

# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
					['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi select box

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
						['Dancing', 'Reading', 'Sports'])

# write the selected options
st.write("You selected", len(hobbies), 'hobbies')

# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
	st.text("Welcome To GeeksForGeeks!!!")

# Text Input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(result)

# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
	# take height input in centimeters
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height")

elif(status == 'meters'):
	# take height input in meters
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	# take height input in feet
	height = st.number_input('Feet')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

	# print the BMI INDEX
	st.text("Your BMI Index is {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("You are Extremely Underweight")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight")
	elif(bmi >= 30):
		st.error("Extremely Overweight")

