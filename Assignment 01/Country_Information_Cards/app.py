import streamlit as st
import requests
import pandas as pd

st.set_page_config("Country_info_cards.🏳")
st.title("Country Information Cards..🏳")
st.write("You can get contries information using this app.")

country = st.text_input("Enter country name: ")
search = st.button("Search")

if search and country:
    try:
        request_url = f'https://restcountries.com/v3.1/name/{country}'
        response = requests.get(request_url)

        if response.status_code == 200:
            info = response.json()[0]

            name = info.get('name', {})
            currencies = info.get('currencies', {})
            languages = info.get('languages', {})

            country_data = {
                'country': name.get('common', 'N/A'),
                'official_name': name.get('official', 'N/A'),
                'capital': ', '.join(info.get('capital', ['N/A'])),
                'region': info.get('region', 'N/A'),
                'subregion': info.get('subregion', 'N/A'),
                'population': f"{info.get('population', 0):,}",
                'area': f"{info.get('area', 0):,} km²",
                'currency': f"{list(currencies.keys())[0]} ({currencies.get(list(currencies.keys())[0], {}).get('name', 'N/A')})" if currencies else 'N/A',
                'languages': ', '.join(languages.values()) if languages else 'N/A',
                'Timezones': ', '.join(info.get('timezones', ['N/A'])),
                'maps': info.get('maps', {}).get('googleMaps', 'N/A')
            }

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(info.get('flags', {}).get('png', ''), width=250)
                st.markdown(f"**Country Code:** {info.get('cca2', 'N/A')}")

            with col2:
                st.header(country_data['official_name'])
                st.table(pd.DataFrame.from_dict(country_data, orient='index', columns=['Details']))

                with st.expander("More Details"):
                    if 'borders' in info:
                        st.subheader("Bordering Countries")
                        st.write(', '.join(info['borders']))

                st.markdown(f"[View on Google Maps]({country_data['maps']})", unsafe_allow_html=True)
        else:
            st.error("Country not found. Please check spelling or try another country.")
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif search:
    st.warning("Please enter a country name first")
