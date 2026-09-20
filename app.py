from flask import Flask, render_template, request, send_file
import joblib
from reportlab.pdfgen import canvas
import os
import sqlite3
from datetime import datetime


# ==========================
# Flask App
# ==========================

app = Flask(__name__)


# ==========================
# Database Setup
# ==========================

def create_database():

    if not os.path.exists("database"):
        os.makedirs("database")


    conn = sqlite3.connect(
        "database/health.db"
    )

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        patient_name TEXT,

        disease TEXT,

        prediction TEXT,

        probability REAL,

        date TEXT

    )
    """)



    conn.commit()

    conn.close()



create_database()



# ==========================
# Save Prediction Function
# ==========================


def save_prediction(
        patient_name,
        disease,
        prediction,
        probability):


    conn = sqlite3.connect(
        "database/health.db"
    )


    cursor = conn.cursor()


    cursor.execute(
    """
    INSERT INTO predictions
    (
    patient_name,
    disease,
    prediction,
    probability,
    date
    )

    VALUES(?,?,?,?,?)

    """,

    (
        patient_name,
        disease,
        prediction,
        probability,
        datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    )


    conn.commit()

    conn.close()



# ==========================
# Report Data
# ==========================


report_data = {}



# ==========================
# Load Models
# ==========================


# Diabetes

diabetes_model = joblib.load(
    "models/diabetes_model.pkl"
)


diabetes_scaler = joblib.load(
    "models/scaler.pkl"
)




# Heart

heart_model = joblib.load(
    "models/heart_model.pkl"
)


heart_scaler = joblib.load(
    "models/heart_scaler.pkl"
)





# Stroke

stroke_model = joblib.load(
    "models/stroke_model.pkl"
)


stroke_scaler = joblib.load(
    "models/stroke_scaler.pkl"
)





# Kidney

kidney_model = joblib.load(
    "models/kidney_model.pkl"
)


kidney_scaler = joblib.load(
    "models/kidney_scaler.pkl"
)






# Liver

liver_model = joblib.load(
    "models/liver_model.pkl"
)


liver_scaler = joblib.load(
    "models/liver_scaler.pkl"
)
# ==========================
# Home
# ==========================


@app.route("/")
def home():

    return render_template("index.html")





# ==========================
# Diabetes Page
# ==========================


@app.route("/diabetes")
def diabetes():

    return render_template("diabetes.html")





# ==========================
# Heart Page
# ==========================


@app.route("/heart")
def heart():

    return render_template("heart.html")





# ==========================
# Stroke Page
# ==========================


@app.route("/stroke")
def stroke():

    return render_template("stroke.html")





# ==========================
# Kidney Page
# ==========================


@app.route("/kidney")
def kidney():

    return render_template("kidney.html")





# ==========================
# Liver Page
# ==========================


@app.route("/liver")
def liver():

    return render_template("liver.html")








# ==========================
# Diabetes Prediction
# ==========================


@app.route("/predict", methods=["POST"])
def predict():


    try:


        patient_name = request.form["Patient_Name"]



        features = [[

            float(request.form["Age"]),

            int(request.form["Gender"]),

            float(request.form["BMI"]),

            float(request.form["Blood_Pressure"]),

            float(request.form["Heart_Rate"]),

            float(request.form["Cholesterol"]),

            float(request.form["HbA1c"]),

            float(request.form["Blood_Glucose"]),

            1.0,

            14.0,

            int(request.form["Smoking"]),

            int(request.form["Alcohol"]),

            float(request.form["Exercise_Hours"]),

            0,

            int(request.form["Family_History"])

        ]]



        features = diabetes_scaler.transform(features)



        prediction = diabetes_model.predict(features)[0]



        probability = round(

            diabetes_model.predict_proba(features)[0][1]*100,

            2

        )




        if prediction == 1:


            prediction_text = "⚠️ High Risk of Diabetes"


            advice = [

                "🩺 Consult Doctor",

                "🥗 Follow Healthy Diet",

                "🏃 Exercise Regularly",

                "🩸 Monitor Blood Sugar"

            ]


        else:


            prediction_text = "✅ Low Risk of Diabetes"


            advice = [

                "😊 Maintain Healthy Lifestyle",

                "🥗 Eat Balanced Food",

                "🏃 Continue Exercise"

            ]




        save_prediction(

            patient_name,

            "Diabetes",

            prediction_text,

            probability

        )



        report_data["name"] = patient_name

        report_data["prediction"] = prediction_text

        report_data["probability"] = probability

        report_data["advice"] = advice

        report_data["disease"] = "Diabetes Prediction"





        return render_template(

            "diabetes.html",

            prediction_text=prediction_text,

            probability=probability,

            advice=advice

        )



    except Exception as e:


        return render_template(

            "diabetes.html",

            prediction_text="Prediction Failed",

            probability=None,

            advice=[str(e)]

        )









# ==========================
# Heart Prediction
# ==========================


@app.route("/predict_heart", methods=["POST"])
def predict_heart():


    try:


        patient_name = request.form["Patient_Name"]



        features = [[


            float(request.form["Age"]),

            int(request.form["Gender"]),

            float(request.form["BMI"]),

            float(request.form["Blood_Pressure"]),

            float(request.form["Heart_Rate"]),

            float(request.form["Cholesterol"]),

            float(request.form["HbA1c"]),

            float(request.form["Blood_Glucose"]),

            float(request.form["Creatinine"]),

            float(request.form["Hemoglobin"]),

            int(request.form["Smoking"]),

            int(request.form["Alcohol"]),

            float(request.form["Exercise_Hours"]),

            int(request.form["Hypertension"]),

            int(request.form["Family_History"])

        ]]



        features = heart_scaler.transform(features)



        prediction = heart_model.predict(features)[0]



        probability = round(

            heart_model.predict_proba(features)[0][1]*100,

            2

        )




        if prediction == 1:


            prediction_text = "🚨 High Risk of Heart Disease"


            advice = [

                "❤️ Consult Cardiologist",

                "🥗 Follow Healthy Diet",

                "🏃 Exercise Regularly",

                "🚭 Avoid Smoking"

            ]



        else:


            prediction_text = "✅ Low Risk of Heart Disease"


            advice = [

                "😊 Maintain Healthy Lifestyle",

                "🥗 Eat Balanced Food",

                "🏃 Continue Exercise"

            ]





        save_prediction(

            patient_name,

            "Heart Disease",

            prediction_text,

            probability

        )





        report_data["name"] = patient_name

        report_data["prediction"] = prediction_text

        report_data["probability"] = probability

        report_data["advice"] = advice

        report_data["disease"] = "Heart Disease Prediction"




        return render_template(

            "heart.html",

            prediction_text=prediction_text,

            probability=probability,

            advice=advice

        )



    except Exception as e:


        return render_template(

            "heart.html",

            prediction_text="Prediction Failed",

            probability=None,

            advice=[str(e)]

        )
# ==========================
# Stroke Prediction
# ==========================


@app.route("/predict_stroke", methods=["POST"])
def predict_stroke():


    try:


        patient_name = request.form["Patient_Name"]



        features = [[

            float(request.form["Age"]),

            int(request.form["Gender"]),

            float(request.form["BMI"]),

            float(request.form["Blood_Pressure"]),

            float(request.form["Heart_Rate"]),

            float(request.form["Cholesterol"]),

            float(request.form["HbA1c"]),

            float(request.form["Blood_Glucose"]),

            1.0,

            14.0,

            int(request.form["Smoking"]),

            int(request.form["Alcohol"]),

            float(request.form["Exercise_Hours"]),

            0,

            int(request.form["Family_History"]),

            int(request.form["Diabetes"]),

            int(request.form["Heart_Disease"]),

            int(request.form["Kidney_Disease"]),

            int(request.form["Liver_Disease"])

        ]]



        features = stroke_scaler.transform(features)



        prediction = stroke_model.predict(features)[0]



        probability = round(

            stroke_model.predict_proba(features)[0][1]*100,

            2

        )



        if prediction == 1:


            prediction_text = "⚠️ High Risk of Stroke"


            advice = [

                "🧠 Consult Neurologist",

                "🩺 Monitor Blood Pressure",

                "🥗 Maintain Healthy Diet",

                "🏃 Exercise Regularly"

            ]



        else:


            prediction_text = "✅ Low Risk of Stroke"


            advice = [

                "😊 Maintain Healthy Lifestyle",

                "🥗 Eat Balanced Food",

                "🏃 Continue Exercise"

            ]




        save_prediction(

            patient_name,

            "Stroke",

            prediction_text,

            probability

        )



        report_data["name"] = patient_name

        report_data["prediction"] = prediction_text

        report_data["probability"] = probability

        report_data["advice"] = advice

        report_data["disease"] = "Stroke Prediction"



        return render_template(

            "stroke.html",

            prediction_text=prediction_text,

            probability=probability,

            advice=advice

        )



    except Exception as e:


        return render_template(

            "stroke.html",

            prediction_text="Prediction Failed",

            probability=None,

            advice=[str(e)]

        )







# ==========================
# Kidney Prediction
# ==========================


@app.route("/predict_kidney", methods=["POST"])
def predict_kidney():


    try:


        patient_name = request.form["Patient_Name"]



        features = [[


            float(request.form["Age"]),

            int(request.form["Gender"]),

            float(request.form["BMI"]),

            float(request.form["Blood_Pressure"]),

            float(request.form["Heart_Rate"]),

            float(request.form["Cholesterol"]),

            float(request.form["HbA1c"]),

            float(request.form["Blood_Glucose"]),

            1.0,

            14.0,

            int(request.form["Smoking"]),

            int(request.form["Alcohol"]),

            float(request.form["Exercise_Hours"]),

            0,

            int(request.form["Family_History"]),

            int(request.form["Diabetes"]),

            int(request.form["Heart_Disease"]),

            int(request.form["Stroke"]),

            int(request.form["Liver_Disease"])

        ]]



        features = kidney_scaler.transform(features)



        prediction = kidney_model.predict(features)[0]



        probability = round(

            kidney_model.predict_proba(features)[0][1]*100,

            2

        )



        if prediction == 1:


            prediction_text = "⚠️ High Risk of Kidney Disease"


            advice = [

                "🩺 Consult Nephrologist",

                "💧 Drink enough water",

                "🥗 Follow Kidney Healthy Diet",

                "🧂 Reduce Salt Intake"

            ]



        else:


            prediction_text = "✅ Low Risk of Kidney Disease"


            advice = [

                "😊 Maintain Healthy Lifestyle",

                "💧 Stay Hydrated",

                "🏃 Exercise Regularly"

            ]




        save_prediction(

            patient_name,

            "Kidney Disease",

            prediction_text,

            probability

        )



        report_data["name"] = patient_name

        report_data["prediction"] = prediction_text

        report_data["probability"] = probability

        report_data["advice"] = advice

        report_data["disease"] = "Kidney Disease Prediction"



        return render_template(

            "kidney.html",

            prediction_text=prediction_text,

            probability=probability,

            advice=advice

        )



    except Exception as e:


        return render_template(

            "kidney.html",

            prediction_text="Prediction Failed",

            probability=None,

            advice=[str(e)]

        )

# ==========================
# Liver Prediction
# ==========================


@app.route("/predict_liver", methods=["POST"])
def predict_liver():


    try:


        patient_name = request.form["Patient_Name"]



        features = [[


            float(request.form["Age"]),

            int(request.form["Gender"]),

            float(request.form["BMI"]),

            float(request.form["Blood_Pressure"]),

            float(request.form["Heart_Rate"]),

            float(request.form["Cholesterol"]),

            float(request.form["HbA1c"]),

            float(request.form["Blood_Glucose"]),

            1.0,

            14.0,

            int(request.form["Smoking"]),

            int(request.form["Alcohol"]),

            float(request.form["Exercise_Hours"]),

            0,

            int(request.form["Family_History"]),

            int(request.form["Diabetes"]),

            int(request.form["Heart_Disease"]),

            int(request.form["Stroke"]),

            int(request.form["Kidney_Disease"])

        ]]



        features = liver_scaler.transform(features)



        prediction = liver_model.predict(features)[0]



        probability = round(

            liver_model.predict_proba(features)[0][1]*100,

            2

        )



        if prediction == 1:


            prediction_text = "⚠️ High Risk of Liver Disease"


            advice = [

                "🩺 Consult Hepatologist",

                "🚫 Avoid Alcohol",

                "🥗 Follow Healthy Diet",

                "🏃 Exercise Regularly"

            ]


        else:


            prediction_text = "✅ Low Risk of Liver Disease"


            advice = [

                "😊 Maintain Healthy Lifestyle",

                "🥗 Eat Balanced Food",

                "💧 Drink Enough Water"

            ]




        save_prediction(

            patient_name,

            "Liver Disease",

            prediction_text,

            probability

        )



        report_data["name"] = patient_name

        report_data["prediction"] = prediction_text

        report_data["probability"] = probability

        report_data["advice"] = advice

        report_data["disease"] = "Liver Disease Prediction"



        return render_template(

            "liver.html",

            prediction_text=prediction_text,

            probability=probability,

            advice=advice

        )



    except Exception as e:


        return render_template(

            "liver.html",

            prediction_text="Prediction Failed",

            probability=None,

            advice=[str(e)]

        )









# ==========================
# Patient History Page
# ==========================


@app.route("/history")
def history():


    conn = sqlite3.connect(
        "database/health.db"
    )


    cursor = conn.cursor()



    cursor.execute(
        "SELECT * FROM predictions ORDER BY id DESC"
    )


    data = cursor.fetchall()



    conn.close()





    return render_template(

        "history.html",

        data=data

    )





    # Total Predictions

    cursor.execute(
        "SELECT COUNT(*) FROM predictions"
    )

    total = cursor.fetchone()[0]



    # High Risk

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM predictions
        WHERE prediction LIKE '%High Risk%'
        """
    )

    high_risk = cursor.fetchone()[0]



    # Low Risk

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM predictions
        WHERE prediction LIKE '%Low Risk%'
        """
    )

    low_risk = cursor.fetchone()[0]



    # Disease Count

    cursor.execute(
        """
        SELECT disease, COUNT(*)
        FROM predictions
        GROUP BY disease
        """
    )

    disease_data = cursor.fetchall()


    conn.close()

    



    return render_template(
    "dashboard.html",
    total=total,
    high_risk=high_risk,
    low_risk=low_risk,
    disease_data=disease_data,
    data=data
)




# ==========================
# Download PDF Report
# ==========================

@app.route("/download_report")
def download_report():


    if not os.path.exists("reports"):
        os.makedirs("reports")


    filename = "reports/AI_Health_Report.pdf"


    pdf = canvas.Canvas(filename)



    # Date and Time

    current_datetime = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )



    # Hospital Image

    hospital_img = "static/images/hospital.png"


    if os.path.exists(hospital_img):

        pdf.drawImage(
            hospital_img,
            430,
            700,
            width=90,
            height=70
        )



    # Doctor Image

    doctor_img = "static/images/doctor.png"


    if os.path.exists(doctor_img):

        pdf.drawImage(
            doctor_img,
            430,
            560,
            width=90,
            height=100
        )




    # Title

    pdf.setFont(
        "Helvetica-Bold",
        18
    )


    pdf.drawString(
        80,
        750,
        "AI Health Predictor"
    )



    pdf.setFont(
        "Helvetica",
        12
    )



    pdf.drawString(
        80,
        710,
        "Generated On : " + current_datetime
    )



    pdf.drawString(
        80,
        680,
        "Disease : "
        +
        report_data.get(
            "disease",
            "Health Prediction"
        )
    )



    pdf.drawString(
        80,
        650,
        "Patient Name : "
        +
        report_data.get(
            "name",
            "N/A"
        )
    )



    pdf.drawString(
        80,
        620,
        "Prediction : "
        +
        report_data.get(
            "prediction",
            "N/A"
        )
    )



    pdf.drawString(
        80,
        590,
        "Risk Probability : "
        +
        str(
            report_data.get(
                "probability",
                "N/A"
            )
        )
        +
        "%"
    )



    pdf.drawString(
        80,
        540,
        "Doctor Recommendation:"
    )


    pdf.drawString(
        100,
        510,
        "Consult Specialist Doctor"
    )



    pdf.drawString(
        80,
        460,
        "Health Advice:"
    )



    y = 430


    for item in report_data.get(
        "advice",
        []
    ):

        pdf.drawString(
            100,
            y,
            "- " + item
        )

        y -= 25




    pdf.drawString(
        80,
        150,
        "Disclaimer:"
    )


    pdf.drawString(
        80,
        120,
        "AI prediction is for educational purpose only."
    )


    pdf.drawString(
        80,
        100,
        "Consult doctor before medical decisions."
    )



    pdf.save()



    return send_file(
        filename,
        as_attachment=True
    )








# ==========================
# Run
# ==========================


if __name__ == "__main__":


    app.run(debug=True)