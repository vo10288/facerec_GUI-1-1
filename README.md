# Facial Recognition 1:1 GUI

Facial recognition application with GUI interface using `Tkinter` and `face_recognition` for comparing two images: known and unknown. It shows both images inside the main GUI and provides a biometric match percentage and result.

## 🔍 Features

- Load two images: known (right) and unknown (left)
- Show both images inside the same interface (no external window)
- Perform 1:1 face recognition with `face_recognition`
- Display match percentage and result
- Support for face landmarks visualization
- Easy reset and background theme switch (black/white)
- Designed for forensic analysis workflows

## 🧰 Requirements

Install the dependencies via:

```bash
pip install -r requirements.txt


sudo apt update
sudo apt install cmake libboost-all-dev libopenblas-dev liblapack-dev

python facial_gui.py
.
├── facial_gui.py                 # Main GUI script
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── 03.reports/
│   ├── reconunknown/            # Folder for unknown images
│   └── reconknown/              # Folder for known images
└── /usr/share/icons/tsurugi/tsurugi.gif  # Optional: logo

CREATED  by Antonio "Visi@n" Broi
Original base: https://tsurugi-linux.org

Licensed under the MIT License.
