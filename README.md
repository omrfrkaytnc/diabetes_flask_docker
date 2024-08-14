# Diabetes Prediction API Project

This project provides a Flask API application using a diabetes prediction model and data. It includes various Python files for data analysis and model predictions.

## Project Content

### Files and Descriptions

- **`app.py`**: The main file for the Flask application. Defines API endpoints and starts the application.
- **`diabetes.csv`**: CSV file containing diabetes data. Used for model training and analysis.
- **`requirements.txt`**: Lists the Python libraries required for the project. Includes dependencies needed for the application to run.
- **`diabetes_model.py`**: Python file for creating and training the diabetes prediction model.
- **`diabetes_data_visualization.py`**: Python file for visualizing diabetes data.
- **`diabetes_form.py`**: Contains form components used in the Flask application for user data input.
- **`Dockerfile`**: Defines the configuration required for running the application in a Docker container. Ensures the application runs in an isolated environment using Docker.
- **`helpers.py`**: Contains helper functions and utilities used in the application.
- **`voting_clf.pkl`**: Pickle format file of the trained model. Used for making predictions.
- **`diabetes_res`**: File containing model results (you may need to specify a clear format).
- **`scaler.pkl`**: Pickle format file of the scaler object used for data scaling.
- **`templates/`**: Directory containing HTML templates for the Flask application.

## Installation and Setup

### Step 1: Clone the Repository

To clone the project to your local machine, use the following command:

```bash
git clone https://github.com/username/repository.git
cd repository
```

### Step 2: Create and Activate a Virtual Environment

To create and activate a virtual environment:

```bash
python -m venv venv
```

- Windows:

```bash
venv\Scripts\activate
```

- macOS/Linux:
```bash
source venv/bin/activate
```

### Step 3: Install Dependencies
To install the required Python libraries:

```bash
pip install -r requirements.txt
```


### Step 4: Run the Application
To start the application:
```bash
python app.py
```

The application will be available at http://127.0.0.1:5000 by default.

## Docker Usage

If you want to use Docker:

- 1.Build the Docker image:

```bash
docker build -t diabetes-api .
```

- 2.Start the Docker container:
```bash
docker run -p 5000:5000 diabetes-api
```

The application will be available at http://localhost:5000 in the Docker container.




---



# Diyabet Tahmin API Projesi

Bu proje, diyabet tahmin modelini ve verilerini kullanarak bir Flask API uygulaması sağlar. Proje, verileri analiz etmek ve model tahminlerini sunmak için çeşitli Python dosyalarını içerir.

## Proje İçeriği

### Dosyalar ve Açıklamaları

- **`app.py`**: Flask uygulamasının ana dosyasıdır. API endpoint'lerini tanımlar ve uygulamanın çalışmasını başlatır.
- **`diabetes.csv`**: Diyabet verilerini içeren CSV dosyası. Model eğitimi ve analizi için kullanılır.
- **`requirements.txt`**: Proje için gerekli Python kütüphanelerini listeler. Uygulamanın çalışması için gereken bağımlılıkları içerir.
- **`diabetes_model.py`**: Diyabet tahmin modeli oluşturma ve eğitme işlemlerini gerçekleştiren Python dosyasıdır.
- **`diabetes_data_visualization.py`**: Diyabet verilerini görselleştirmek için kullanılan Python dosyasıdır.
- **`diabetes_form.py`**: Flask uygulamasında kullanıcıdan veri girişi için kullanılan form bileşenlerini içerir.
- **`Dockerfile`**: Uygulamanın bir Docker konteynerinde çalıştırılması için gereken yapılandırmayı tanımlar. Docker ile uygulamanın izole bir ortamda çalışmasını sağlar.
- **`helpers.py`**: Uygulamada tekrar eden yardımcı işlevleri ve araçları içerir.
- **`voting_clf.pkl`**: Eğitimli modelin pickle formatındaki dosyasıdır. Tahminler yapmak için kullanılır.
- **`diabetes_res`**: Model sonuçlarını içeren dosya (belirgin bir format belirtmeniz gerekebilir).
- **`scaler.pkl`**: Verilerin ölçeklendirilmesi için kullanılan scaler nesnesinin pickle formatındaki dosyasıdır.
- **`templates/`**: Flask uygulamasının HTML şablonlarını içeren klasördür.



### Adım 1: Depoyu Klonlayın

Projenizi yerel bilgisayarınıza klonlamak için aşağıdaki komutu kullanın:

```bash
git clone https://github.com/username/repository.git
cd repository
```


### Adım 2 : Sanal Ortam Oluşturun ve Aktifleştirin

Sanal ortam oluşturmak ve aktifleştirmek için:

```bash
python -m venv venv
```

- Windows:

```bash
venv\Scripts\activate
```

- macOS/Linux:
```bash
source venv/bin/activate
```

### Adım 3: Gereksinimleri Yükleyin
Gerekli Python kütüphanelerini yüklemek için:

```bash
pip install -r requirements.txt
```


### Adım 4: Uygulamayı Başlatın
```bash
python app.py
```

Uygulama varsayılan olarak http://127.0.0.1:5000 adresinde çalışacaktır.

## Docker Kullanımı

Eğer Docker kullanmak istiyorsanız:

- 1.Docker imajını oluşturun:

```bash
docker build -t diabetes-api .
```

- 2.Docker konteynerini başlatın:
```bash
docker run -p 5000:5000 diabetes-api
```

Uygulama Docker konteynerinde http://localhost:5000 adresinde çalışacaktır.











