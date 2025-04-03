import streamlit as st

# Set the page title
st.set_page_config(page_title="The Last 10 Days of Ramadan")

# Sidebar Navigation
pages = ["Home", "Importance of Ramadan", "Quranic Verses", "Hadiths", "Duas"]
selection = st.sidebar.radio("Go to", pages)

# Home Page
if selection == "Home":
    st.title("The Last 10 Days of Ramadan")
    st.markdown("""
    Ramadan is the month when Muslims fast from dawn until sunset, seeking closeness to Allah through worship, prayer, and reflection.
    The last 10 days are particularly special, containing Laylat al-Qadr, the Night of Decree, which holds blessings more than a thousand months.
    This website explores the significance of the last 10 days, the Quranic verses, Hadiths, and Duas to help you make the most of these blessed days.
    """)

# Importance of Ramadan
elif selection == "Importance of Ramadan":
    st.title("Why Ramadan is So Special")
    st.markdown("""
    Ramadan is the ninth month of the Islamic calendar. Fasting is not just about abstaining from food and drink, but a time for spiritual renewal. 
    Muslims engage in worship, prayers, and good deeds, seeking to draw closer to Allah.
    
    The last 10 days of Ramadan are especially significant because of **Laylat al-Qadr**, the Night of Decree. This night is a time of mercy, forgiveness, and divine blessings.
    
    The Prophet Muhammad (PBUH) said:  
    *"Whoever prays during the last ten nights of Ramadan with faith and hope of reward, all his past sins will be forgiven."*  
    (Sahih Bukhari)
    """)

# Quranic Verses
elif selection == "Quranic Verses":
    st.title("Quranic Verses About Ramadan and Laylat al-Qadr")
    
    st.markdown("### Surah Al-Qadr (97:1)")
    st.markdown("""
    **Arabic:**  
    إِنَّا أَنزَلْنَاهُ فِي لَيْلَةِ الْقَدْرِ  
    
    **English Translation:**  
    *Indeed, We sent it [the Quran] down during the Night of Decree.*  
    
    **Reference:** *Surah Al-Qadr, 97:1*
    """)
    
    st.markdown("### Surah Al-Baqarah (2:185)")
    st.markdown("""
    **Arabic:**  
    شَهْرُ رَمَضَانَ الَّذِي أُنزِلَ فِيهِ الْقُرْآنُ هُدًى لِلنَّاسِ  
    
    **English Translation:**  
    *The month of Ramadan [is that] in which was revealed the Qur'an, a guidance for the people.*  
    
    **Reference:** *Surah Al-Baqarah, 2:185*
    """)

# Hadiths
elif selection == "Hadiths":
    st.title("Hadiths About the Last 10 Days of Ramadan")
    
    st.markdown("### Hadith 1: Laylat al-Qadr")
    st.markdown("""
    **Arabic:**  
    *رسول اللہ صلی اللہ علیہ وسلم نے فرمایا:*  
    *"جو شخص رمضان کی آخری دس راتوں میں ایمان اور احتساب کے ساتھ عبادت کرے، اللہ تعالیٰ اس کے پچھلے گناہ معاف کردے گا۔"*  
    
    **Translation:**  
    *The Prophet Muhammad (PBUH) said: "Whoever spends the last ten nights of Ramadan in prayer with faith and seeking reward, his previous sins will be forgiven."*  
    **Reference:** *Sahih Bukhari, Hadith 2009*
    """)

    st.markdown("### Hadith 2: Reward for Worship in Last 10 Days")
    st.markdown("""
    **Arabic:**  
    *"رمضان کے آخری عشرہ میں نفل عبادت کو فرض کے برابر سمجھا جائے گا..."*  
    
    **Translation:**  
    *"The one who worships during the last ten days of Ramadan, Allah will reward him as if he has worshipped throughout the whole year."*  
    **Reference:** *Sahih Muslim, Hadith 1161*
    """)

# Duas
elif selection == "Duas":
    st.title("Duas for the Last 10 Days of Ramadan")
    
    st.markdown("### Dua for Forgiveness")
    st.markdown("""
    **Arabic:**  
    اللهم إنك عفو تحب العفو فاعف عني  
    
    **English Translation:**  
    *O Allah, You are the Most Forgiving, and You love forgiveness, so forgive me.*  
    """)
    
    st.markdown("### Dua for Protection from Hardship")
    st.markdown("""
    **Arabic:**  
    اللهم إني أعوذ بك من فتنة المحيا والممات  
    
    **English Translation:**  
    *O Allah, I seek refuge in You from the trials of life and death.*  
    """)

    st.markdown("### Dua for Mercy and Blessings")
    st.markdown("""
    **Arabic:**  
    اللهم اجعلنا من أهل الجنة  
    
    **English Translation:**  
    *O Allah, make us among the people of Paradise.*  
    """)

