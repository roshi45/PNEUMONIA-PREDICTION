# 🫁 Pneumonia Prediction using Deep Learning  

![Pneumonia Detection](https://img.shields.io/badge/Pneumonia-Prediction-blue.svg)  
A deep learning-based model for pneumonia detection using chest X-ray images. The model is trained to classify images as **Normal** or **Pneumonia** using **Convolutional Neural Networks (CNNs)**.  

---

## 🚀 Features  
- 📊 **Deep Learning Model**: Uses a pre-trained CNN model for accurate pneumonia detection.  
- 📸 **Chest X-ray Classification**: Identifies pneumonia in X-ray images.  
- ⚡ **Flask Web App**: Provides an interactive UI for users to upload and classify images.  
- 📦 **TensorFlow & Keras**: Built using **TensorFlow 2.x** and **Keras**.  

---

## 📂 Dataset  
The dataset used for training is from [Kaggle's Chest X-ray Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia). It consists of:  
- **Normal** chest X-rays  
- **Pneumonia** affected chest X-rays  

---

## 🛠 Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/roshi45/PNEUMONIA-PREDICTION.git
cd PNEUMONIA-PREDICTION
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Download the Model  
Since GitHub LFS is restricted, **manually download** the trained model (`model.h5`) and place it in the project folder.  

### 4️⃣ Run the Flask App  
```bash
python app.py
```

---

## 📌 Usage  
1. Run the app (`python app.py`).  
2. Open `http://127.0.0.1:5000/` in your browser.  
3. Upload a chest X-ray image.  
4. The model will classify it as **Normal** or **Pneumonia**.  

---

## ⚙ Technologies Used  
- **Python 3.11**  
- **TensorFlow / Keras**  
- **Flask**  
- **OpenCV**  
- **Pandas & NumPy**  

---

## 📷 Sample Prediction  
![Pneumonia Prediction UI](<img width="295" alt="image" src="https://github.com/user-attachments/assets/6a85915b-c493-4cf9-b7ff-9b5b8dfd7239" />
)
---



