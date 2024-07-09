# Face Recognition Attendance System

This project is a Face Recognition Attendance System built using Streamlit and OpenCV. The application captures images from a webcam, recognizes faces, and marks attendance in real-time.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Real-time face detection and recognition.
- Marking attendance with timestamp.
- User-friendly interface built with Streamlit.
- Storage of attendance records in CSV format.
- Easy to add new faces to the recognition system.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the pre-trained face detection model:**

   Download the `haarcascade_frontalface_default.xml` file from [OpenCV GitHub](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in the `models` directory.

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Adding New Faces:**
   - Use the "Add New Faces" section to capture and store new faces.
   - Provide the name of the person and capture their face using the webcam.

3. **Marking Attendance:**
   - Go to the "Mark Attendance" section.
   - The app will use the webcam to recognize faces and mark attendance.

4. **Viewing Attendance Records:**
   - Check the "Attendance Records" section to view the stored attendance data.

## Dependencies

- Python 3.x
- Streamlit
- OpenCV
- NumPy
- Pandas

## Project Structure

```
face-recognition-attendance-system/
├── app.py                  # Main Streamlit application
├── face_recognition.py     # Face recognition logic
├── attendance.py           # Attendance marking logic
├── data/                   # Directory to store face images and attendance records
│   ├── faces/              # Subdirectory for storing face images
│   └── attendance.csv      # CSV file for storing attendance records
├── models/                 # Directory for storing machine learning models
│   └── haarcascade_frontalface_default.xml  # Pre-trained face detection model
├── requirements.txt        # List of dependencies
└── README.md               # Project README file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file to better suit your project's needs.
