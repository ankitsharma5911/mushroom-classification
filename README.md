# Mushroom Classification Project

This project focuses on building a machine learning model to classify mushrooms as either edible or poisonous based on their physical and chemical attributes. The system leverages data preprocessing, machine learning pipelines, and hyperparameter tuning, and is deployed as a web API for easy accessibility.

---

## Table of Contents

- [Mushroom Classification Project](#mushroom-classification-project)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup and Installation](#setup-and-installation)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Testing](#testing)
  - [Docker Support](#docker-support)
  - [Contributing](#contributing)
  - [License](#license)

---

## Introduction
The objective of this project is to classify mushrooms as edible or poisonous using a dataset of categorical features such as cap shape, cap surface, odor, and habitat. The application processes user input and returns predictions through a deployed Flask API hosted on Render.

---

## Features

- **Data Preprocessing**: Handles missing values, encodes categorical variables, and prepares data for model training.
- **Machine Learning Models**: Uses algorithms such as Logistic Regression, Random Forest, and Gradient Boosting with hyperparameter tuning.
- **API Deployment**: Provides a RESTful API with endpoints for predictions and health checks.
- **Experiment Tracking**: Utilizes MLflow for tracking experiments and logging metrics.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Scikit-learn
  - Flask
  - NumPy, Pandas
  - Matplotlib, Seaborn
- **Tools**:
  - MLflow for experiment tracking
  - Render for deployment

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ankitsharma5911/mushroom-classification.git
   cd mushroom-classification
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Flask server locally:
   ```bash
   python app.py
   ```
4. Access the application at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## Usage

1. **Local Testing**:
   - Send a POST request to the `/` endpoint with mushroom attributes as input.
   - Example input:
     ```json
     {
         "cap_shape": "x",
         "cap_surface": "s",
         "cap_color": "n",
         "bruises": "t",
         "odor": "n",
         "gill_attachment": "f",
         "gill_spacing": "c",
         "gill_size": "n",
         "gill_color": "n",
         "stalk_shape": "e",
         "stalk_root": "c",
         "stalk_surface_above_ring": "s",
     }
     ```
   - Example output:
     ```json
     {
         "prediction": "edible"
     }
     ```

2. **Deployed API**:
   - Access the live API at [this link](https://mushroom-classification-jaxa.onrender.com) .

---

## API Endpoints

- **POST `/`**:
  - Input: JSON object with mushroom attributes.
  - Output: Prediction (`"edible mushroom"` or `"mushroom is poisonous"`).

- **GET `/predict`**:
  - Returns the prediction from the input sent via `/`.

- **GET `/train`**:
  - Train the model.

---

## Testing

- **Unit Tests**:
  - Run tests for preprocessing, model predictions, and API endpoints:
    ```bash
    python -m unittest discover tests
    ```
- **API Testing**:
  - Use tools like Postman or cURL to test the endpoints.

---

## Docker Support

To simplify deployment, this project uses a prebuilt Docker image available at `ankitsharma80/mushroom_classification`.

1. Pull the Docker image:
   ```bash
   docker pull ankitsharma80/mushroom_classification
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 ankitsharma80/mushroom_classification
   ```

3. Access the application at `http://127.0.0.1:5000/`.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.


