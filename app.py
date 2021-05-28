# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc
#from eda_app import run_eda
import pandas as pd
import plotly_express as px
#from upload import upload_data
from Eda_app_ import run_eda
from ml_app import run_ml

#st.set_page_config(page_title='Visualization', page_icon='📊')
html_temp = """
		<div style="background-color:#4682b4;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Educational Data Mining</h1>
		<h4 style="color:white;text-align:center;">Analysis & Prediction</h4>
		</div>
		"""


def main():
	stc.html(html_temp)
	menu = ["Home","Upload & EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)


	if choice == "Upload & EDA":
		run_eda()

	elif choice == "ML":
		run_ml()

	elif choice == "About":
		st.subheader("About")
		# st.info("Built with Streamlit")
		st.info("Project title: Educational Data Mining")
		st.text("SVIT")
		st.text("Build by: \nSwapnil prajapati \nUtkarsh patel \nParth patel ")



	else:
		st.subheader("Home")
		st.text("\nHow to use this data science web app")
		st.text("1)Upload your respective CSV or Excel File from the Upload page. "
				"\n2)After uploading EDA & data report will help to explore the data further. "
				"\n3)If the machine learning algorithm is required then prefere the ML section."
				"\n Note: Upload a preproceessed file in the ML section.")


if __name__ == '__main__':
	main()