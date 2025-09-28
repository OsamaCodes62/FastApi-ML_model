# FastApi-ML_model

## 🚀 Overview

FastApi-ML_model is a powerful Python application that leverages FastAPI for creating a RESTful API and machine learning models to predict insurance premiums based on user input. This project is designed to be easy to use, scalable, and highly customizable, making it ideal for developers and data scientists looking to integrate machine learning models into their applications.

### Key Features

- **Predict Insurance Premiums**: Use a pre-trained machine learning model to predict insurance premiums based on user input.
- **User-Friendly Interface**: A simple and intuitive frontend built with Streamlit for easy data input and prediction.
- **Scalable API**: Built with FastAPI, ensuring high performance and scalability.
- **Modular Design**: Easily extendable and customizable for different machine learning models and datasets.

### Who This Project Is For

- Data scientists and machine learning engineers looking to deploy their models as APIs.
- Developers interested in building scalable web applications with FastAPI.
- Anyone looking to integrate machine learning into their applications.

## ✨ Features

- 🌟 **Machine Learning Integration**: Easily integrate and deploy machine learning models.
- 🌟 **FastAPI**: High-performance, modern web framework for building APIs.
- 🌟 **Streamlit**: User-friendly frontend for data input and prediction.
- 🌟 **Comprehensive Documentation**: Clear and detailed documentation for easy setup and usage.

## 🛠️ Tech Stack

- **Programming Language**: Python
- **Frameworks and Libraries**:
  - FastAPI
  - Streamlit
  - Pandas
  - Scikit-learn
  - Pydantic
  - Uvicorn
- **System Requirements**:
  - Python 3.8 or later
  - pip

## 📦 Installation

### Prerequisites

- Python 3.8 or later
- pip

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/FastApi-ML_model.git

# Navigate to the project directory
cd FastApi-ML_model

# Install the required packages
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app:app --reload

# Run the Streamlit frontend
streamlit run frontend.py
```

### Alternative Installation Methods

- **Docker**: You can use Docker to containerize the application for easier deployment.
  ```bash
  docker build -t fastapi-ml-model .
  docker run -p 8000:8000 fastapi-ml-model
  ```

## 🎯 Usage

### Basic Usage

```python
# Example of making a prediction using the API
import requests

data = {
    "age": 30,
    "weight": 65.0,
    "height": 1.5,
    "income_lpa": 12.0,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

response = requests.post("http://127.0.0.1:8000/predict", json=data)
print(response.json())
```

### Advanced Usage

- **Custom Models**: You can replace the `insurance_model.pkl` with your own trained model.
- **Configuration**: Modify the `app.py` file to change the input fields and model prediction logic.

## 📁 Project Structure

```
FastApi-ML_model/
│
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── frontend.py
└── insurance.csv
```

## 🔧 Configuration

- **Environment Variables**: No specific environment variables are required.
- **Configuration Files**: The `app.py` file contains the main configuration for the FastAPI application.

## 🤝 Contributing

We welcome contributions! Here's how you can get started:

### Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FastApi-ML_model.git
   cd FastApi-ML_model
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app:app --reload
   streamlit run frontend.py
   ```

### Code Style Guidelines

- Follow PEP 8 for Python code.
- Use meaningful variable and function names.
- Add comments to explain complex logic.

### Pull Request Process

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Open a pull request to the main repository.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors & Contributors

- **Maintainer**: [Your Name]
- **Contributors**: [List of contributors]

## 🐛 Issues & Support

- **Report Issues**: Open an issue on the GitHub repository.
- **Get Help**: Join the discussion on the GitHub repository or contact the maintainer.

## 🗺️ Roadmap

- **Planned Features**:

  - Add support for more machine learning models.
  - Improve the frontend with more interactive features.
  - Add authentication and authorization.

- **Future Improvements**:
  - Integrate with more data sources.
  - Improve performance and scalability.

---

**Additional Information**

- For more information, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/) and [Streamlit documentation](https://docs.streamlit.io/).
