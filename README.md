# 🩺 Medical Symptom Analyzer

## 📌 Project Overview

Medical Symptom Analyzer is an AI-powered multilingual healthcare assistant developed using Python.

The system allows users to enter symptoms using text or voice input and intelligently analyzes possible diseases, risk levels, emergency conditions, and medical suggestions.

This project also supports dynamic follow-up questions, multilingual interaction, voice responses, and emergency guidance.

---

# ✨ Key Features

## 🌍 Multilingual Support

Supports the following languages:

* English
* Hindi
* Marathi
* Bengali
* Tamil
* Telugu
* Kannada
* Malayalam
* Gujarati
* Punjabi
* Urdu
* Hinglish

---

## 🎤 Voice + Text Input

Users can:

* Type symptoms manually
* Speak symptoms using voice recognition

---

## 🤖 AI-Based Symptom Analysis

The system:

* Detects symptoms
* Matches diseases
* Calculates confidence percentage
* Suggests possible conditions

---

## ❓ Dynamic Follow-up Questions

The analyzer intelligently asks extra questions based on symptoms.

### Example

```text
Fever → Do you also feel weakness?
Cough → Do you also have difficulty breathing?
```

This improves analysis accuracy.

---

## 🚨 Risk Detection System

The system automatically detects:

* LOW Risk
* MEDIUM Risk
* HIGH Risk

based on symptoms and follow-up answers.

---

## ⚠ Dynamic Emergency Guidance

Emergency warnings change dynamically according to symptoms.

### Example

```text
Do not ignore breathing problems.
Do not ignore chest pain.
Do not ignore severe weakness.
```

---

## 🔊 Voice Output

The system speaks:

* Questions
* Results
* Emergency alerts
* Recommendations

using AI voice output.

---

## 📄 Patient Health Report

The project generates a complete patient report including:

* Symptoms
* Risk level
* Possible diseases
* Recommendations

---

# 🛠 Technologies Used

* Python
* SpeechRecognition
* gTTS
* playsound
* JSON
* AI Logic-Based Analysis

---

# ⚙ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/mudgalshriya2004-eng/medical_symptom_analyzer.git
```

---

## 2️⃣ Open Project Folder

```bash
cd medical_symptom_analyzer
```

---

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run the Project

Run the following command:

```bash
python run.py
```

---

# 🧪 Example Output

```text
=====================================
     MEDICAL SYMPTOM ANALYZER
=====================================

Select Language:
1. English
2. Hindi
3. Marathi

Enter choice: 1

Use voice? (y/n): y

Please tell your symptoms

You: fever and cough

Do you also have difficulty breathing? (yes/no)

You: yes

Risk Level: HIGH

Possible Condition:
- Pneumonia
- Flu
```

---

# 🎯 Project Capabilities

✅ Symptom Detection
✅ Disease Prediction
✅ Confidence Percentage
✅ Emergency Alerts
✅ Voice Interaction
✅ Multilingual Support
✅ Dynamic Follow-up Questions
✅ Risk Assessment
✅ Healthcare Report Generation

---

# ⚠ Disclaimer

This project is developed for educational and research purposes only.

It does not replace professional medical advice, diagnosis, or treatment.

Always consult a qualified doctor for medical emergencies.

---

# ⭐ Conclusion

Medical Symptom Analyzer is a smart healthcare assistant that combines:

* AI logic
* Voice interaction
* Multilingual communication
* Dynamic risk analysis

to provide an intelligent medical support system.
