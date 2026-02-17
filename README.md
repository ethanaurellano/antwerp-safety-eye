# 🛡️ Port of Antwerp: AI Safety Marshall
### Real-Time HSE Compliance & PPE Monitoring

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](YOUR_STREAMLIT_LINK_HERE)

## 🎯 The Business Problem
In high-risk industrial environments like the **Port of Antwerp**, Health, Safety, and Environment (HSE) protocols are a top priority. Monitoring hundreds of CCTV feeds for safety compliance (such as wearing helmets or high-vis vests) is impossible for human supervisors to do 24/7. 

**Manual monitoring leads to:**
* **Safety Blind Spots:** Fatalities or injuries occurring in unmonitored zones.
* **High Liability:** Insurance and legal costs from preventable accidents.
* **Inconsistent Data:** No way to track long-term safety compliance trends.

## 💡 The Solution
This project is an **Automated Safety Supervisor** that uses Computer Vision (YOLOv8) to analyze video streams and identify personnel in hazardous zones. It serves as a proof-of-concept for a fully automated PPE detection system.

**Key features:**
* **Real-Time Detection:** Processes video frames instantly to identify people.
* **Industrial Context:** Tested on actual construction and industrial site footage.
* **Interactive Control:** Adjust AI confidence thresholds on-the-fly via a web dashboard.
* **Cloud Ready:** Fully deployed via Streamlit for remote monitoring.

## 🛠️ Tech Stack
* **AI Engine:** [YOLOv8](https://github.com/ultralytics/ultralytics) (Ultralytics)
* **Framework:** Python 3.x
* **Dashboard:** Streamlit
* **Image Processing:** OpenCV (Headless)
* **Deployment:** GitHub & Streamlit Cloud

## 🚀 Installation & Setup
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/antwerp-safety-eye.git](https://github.com/YOUR_USERNAME/antwerp-safety-eye.git)
   cd antwerp-safety-eye
2. **Install dependencies:**
   ```Bash
   pip install -r requirements.txt
3. **Run the application:**
   ```Bash
   streamlit run vision_app.py
