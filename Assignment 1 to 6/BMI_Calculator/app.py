import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="🔢", layout="centered")

st.header("🧮 BMI Calculator...🏋️‍♂️", )


height = {    
    'meter': 1,  # base unit
    'centimeter': 100,
}

age = st.text_input("📅 Age: (between 2-120)", max_chars=3)

gender = st.radio("Gender: ", options=['Male', 'Female'], horizontal=True)

weight = st.text_input(label="⚖️ Weight:", placeholder="kg", max_chars=5)

height = st.text_input(label="📏 Height: ",placeholder="cm", max_chars=4)

if st.button(label="🔢 Calculate"):
    try:
        if not weight or not height or not age:
            st.error("⚠️ Please fill all required fields.")
        elif not weight.replace('.', '', 1).isdigit() or not height.replace('.', '', 1).isdigit() or not age.isdigit():
            st.error("⚠️ Pleae enter only numeric values.")
        else:
            weight = float(weight)
            height = float(height)
            age = float(age)

        if weight <= 0 or height <= 0 or age <= 0:
            st.error("🚫 Height, Weight and Age must be greater than 0.")
        else:
            bmi = weight / (height / 100)**2
            st.success(f"📊 Your BMI is: {bmi:.2f} kg/m²")

            if bmi < 16:
                st.write("🏥 **Category: Severe Thinness")
                st.warning("⚠️ Consult a doctor, improve your diet, and take proper nutrition for healthy weight gain.")
            elif bmi <= 17:
                st.write("🍽️ **Category: Moderate Thinness")
                st.warning("🥩 Consume high-calorie and protein-rich food, and follow a workout routine to build muscle.")
            elif bmi <= 18.5:
                st.write("🥗 **Category: Mild Thinness")
                st.warning("📅 Gain a little weight, follow a balanced diet, and maintain a proper meal schedule.")
            elif bmi <= 25:
                st.write("💪 **Category: Normal")
                st.warning("🎉 Your weight is perfect! Maintain a healthy lifestyle, continue exercising, and follow a balanced diet.")
            elif bmi <= 30:
                st.write("⚠️ **Category: Overweight")
                st.warning("🥦 Control your weight: Avoid excess calories, exercise daily, and choose healthy food options.")
            elif bmi <= 35:
                st.write("⚠️ **Category: Obese Class I")
                st.warning("📉 Weight loss is necessary: Create a proper diet and workout plan and seek guidance from a doctor/nutritionist.")
            elif bmi <= 40:
                st.write("🚨 **Category: Obese Class II")
                st.warning("⚠️ Serious risk: Follow a strict weight loss program and consult a medical professional.")
            else:
                st.write("🛑 **Category: Obese Class III")
                st.warning("❗ Very high risk! It is essential to consult a doctor, and lifestyle or medical interventions may be required.")

    except Exception as e:
        ""