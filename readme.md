# Secure Image Steganography - README

## 📌 Introduction
This is a **Python-based Steganography project** that allows users to **hide secret messages inside images** and later retrieve them using a **passcode**. It uses the **Least Significant Bit (LSB) technique** to encode messages in images without visually altering them.

## 🚀 Features
✅ **Hide a secret message inside an image**  
✅ **Retrieve hidden messages using a passcode**  
✅ **Graphical User Interface (GUI) with Tkinter**  
✅ **Progress bar during decryption**  
✅ **Passcode protection for extra security**  
✅ **Supports PNG and JPG images**  

## 🏗️ Project Structure
```
SteganographyApp/
│── src/
│   ├── main.py        # The main UI file
│   ├── encrypt.py     # Logic for hiding messages in an image
│   ├── decrypt.py     # Logic for extracting hidden messages
│   ├── utils.py       # Helper functions for UI and file handling
│── README.md          # Project documentation
```

## 🛠️ Installation & Setup
### Prerequisites:
- **Python 3.x**
- **Pip**

### Step 1: Clone the Repository
```sh
git clone https://github.com/yourusername/SteganographyApp.git
cd SteganographyApp/src
```

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Run the Application
```sh
python main.py
```

## 🖥️ How to Use
### 🔐 Hiding a Message (Encryption)
1️⃣ Open the application.  
2️⃣ Go to the **Encrypt Tab**.  
3️⃣ Select an image 📷.  
4️⃣ Enter your **secret message** and **passcode** 🔑.  
5️⃣ Click **Encrypt & Save** - Your message is now hidden in the image! 🕵️‍♂️

### 🔓 Revealing a Message (Decryption)
1️⃣ Open the application.  
2️⃣ Go to the **Decrypt Tab**.  
3️⃣ Select the **steganographic image** 📷.  
4️⃣ Enter the correct **passcode** 🔑.  
5️⃣ Click **Decrypt & Read** - If correct, your secret message appears! 🎉

## 🔍 How It Works
- **LSB Encoding**: Hides message bits in the least significant bits of image pixels.
- **Passcode Protection**: Encrypts the message before hiding it.
- **Threading for Decryption**: Keeps UI responsive by running decryption in a separate thread.

## 🛠️ Built With
- **Python** 🐍
- **Tkinter** - For GUI 🖥️
- **OpenCV** - For image processing 📷
- **NumPy** - For handling pixel data 🔢

## 🤝 Contributing
Contributions are welcome! Follow these steps:
1️⃣ Fork the repository 🍴  
2️⃣ Create a new branch 🏗️  
3️⃣ Commit your changes 📝  
4️⃣ Push the changes and open a pull request 🔄

## 📜 License
This project is licensed under the **MIT License**.

## 📞 Contact
For questions or suggestions, reach out:
📧 Email: [your-email@example.com](mailto:your-email@example.com)  
🔗 GitHub: [yourusername](https://github.com/yourusername)  

