# ☁️ Dự án ETL & Trực quan hóa dữ liệu động đất với Azure và Power BI

Dự án này xây dựng **quy trình ETL tự động trên nền tảng Azure Databrick**, giúp thu thập, xử lý và tải dữ liệu vào kho dữ liệu trung tâm, xây dựng mô hình dự đoán,**trực quan hóa kết quả trên Power BI** để hỗ trợ phân tích và ra quyết định.

---

## 📊 Mục tiêu dự án
- Tự động hóa quy trình thu thập và xử lý dữ liệu.
- Lưu trữ dữ liệu tập trung, dễ quản lý và mở rộng.
- Xây dựng mô hình dự đoán
- Trực quan hóa dữ liệu với Power BI

---

## 🧱 Kiến trúc hệ thống
<img width="621" height="539" alt="image" src="https://github.com/user-attachments/assets/5633fdd9-d8df-4c3d-ae10-a54e61daa1bf" />

- **Source:** Data is ingested from an external API in JSON format.
- **Ingest:** Raw data is stored in Azure Data Lake Storage.
- **Storage Layers:**
  - **Bronze:** Lớp dữ liệu thô (data khi craw về được lưu trực tiếp ở đây)
  - **Silver:** Lớp dữ liệu được xử lý lưu ở đây và đã có thể sử dụng để huấn luyện Mô Hình.
  - **Gold:** Lớp dữ liệu được trích xuất và biến đổi phục vụ cho nhu cầu phân tích.
- **Process:** Dữ liệu được biến đổi và phân tích sử dụng Databricks qua thư viện PySpark và Spark ML (Huấn luyện mô hình).
- **Serve:**
  - **Prediction:** Machine learning predictions handled by Databricks.
  - **Analytics:** Advanced analytics managed by Azure Synapse Analytics.
  - **Visualization:** Data visualized using Power BI.

## Setup Instructions

1. Configure Azure Data Lake Storage with appropriate access permissions.
2. Set up a Databricks workspace with Spark and Spark MLlib.
3. Establish an API connection for JSON data ingestion.
4. Install and configure Azure Synapse Analytics and Power BI for analytics and visualization.

## Usage

1. Ingest JSON data into the Bronze layer via the API.
2. Process and clean data through Silver and Gold layers using Databricks notebooks.
3. Serve predictions, analytics, and visualizations from the Gold layer using Synapse Analytics and Power BI.

## Technologies Used

- **Azure Data Lake Storage**
- **Databricks** (Apache Spark, Spark MLlib)
- **Azure Synapse Analytics**
- **Using Grid Event** Tracking Storage Layers to call **Function App** are mapped to Process Data immediately
