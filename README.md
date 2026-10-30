# Recipe Discovery Application

**Recipe Discovery Application** is a lightweight and intuitive web app designed to help users explore and discover recipes based on ingredients they have at hand or their dietary preferences. Built using Python (Flask), HTML/CSS, and JavaScript, this application offers a seamless user experience for finding delicious meal ideas.

---

##  Table of Contents

- [Features](#features)  
- [Demo](#demo)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running Locally](#running-locally)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Features

- Input-based recipe search (by ingredients or keywords)  
- Responsive and user-friendly interface  
- Easily extensible backend for adding new recipe sources  
- Lightweight and educational—ideal for learning or prototyping

---

## Demo

*(Include a screenshot or GIF here for a quick visual preview—for example:)*  

![App Screenshot](static/img/screenshot.png)

---

## Tech Stack

- **Backend**: Python + Flask (`app.py`)  
- **Frontend**: HTML, CSS, JavaScript  
- **Templates**: Jinja2 (`templates/` directory)  
- **Static Assets**: JavaScript & CSS (`static/` directory)

---

## Getting Started

### Prerequisites

- Python 3.7+ installed  
- `pip` package manager  

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jayapraksh1234/Recipe_discovery_application.git
   cd Recipe_discovery_application
   ```

2. **Optional**: Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

```bash
python app.py
```

- Visit `http://127.0.0.1:5000/` in your browser to access the app.

---

## Usage

1. Navigate to the home page.  
2. Enter ingredients or recipe keywords (e.g., “chicken, tomato”).  
3. Submit to view a list of matching recipes.  
4. Click on a recipe to view detailed steps or ingredients list.  

---

## Project Structure

```
Recipe_discovery_application/
├── app.py
├── templates/
│   ├── index.html
│   └── results.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── main.js
├── README.md
└── requirements.txt
```

---

## Contributing

Contributions are always welcome! Whether it's improving UI, adding features, or fixing bugs—feel free to open an issue or pull request.

**Steps to contribute**:
1. Fork the repo.  
2. Create a feature branch: `git checkout -b my-feature`  
3. Commit your changes: `git commit -m "Add some feature"`  
4. Push to your branch: `git push origin my-feature`  
5. Open a pull request and describe your improvements.  

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## Contact

**Created by**: Jayapraksh  

Have questions or feedback? Feel free to reach out via GitHub issues or at [jayaprakashn109@email.com].

---

*Thank you for checking out the Recipe Discovery Application—happy cooking!*  
