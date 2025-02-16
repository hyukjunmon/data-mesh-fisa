#  FISA Mini Project - data-mesh-fisa

## 📌 프로젝트 개요
**data-mesh-fisa 프로젝트**는 데이터 메시(Data Mesh)에서의 데이터 제공 및 조회를 구현하여 시각화할 수 있도록 설계되었습니다. 
이 프로젝트에서는 **주문 서비스(Order Service)**와 **고객 서비스(Customer Service)**가 **각자 독립적으로 데이터 API를 제공**하며,  
이를 **중앙 데이터 팀 없이** 조회할 수 있습니다.  이를 스트림릿을 통해 구현을 하였습니다.
또한, **데이터 카탈로그 서비스**를 포함하여 메타데이터 관리까지 경험할 수 있습니다.

---

## 🛠️ 기술 스택
- **Backend**
  - Flask (Python)
  - SQLite (Lightweight Database)
- **Frontend**
  - Streamlit (Data Visualization)
- **API Gateway & Communication**
  - RESTful API (Flask 기반)
- **Orchestration**
  - Docker & Docker Compose

---

