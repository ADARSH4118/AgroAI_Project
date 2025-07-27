🌾 Smart Fertilizer Recommendation System
An intelligent web app that helps farmers get personalized, real-time fertilizer advice using machine learning and live weather data.

🚀 Project Overview
📌 What Is It?
This project is a smart web-based platform that delivers personalized fertilizer recommendations. It blends:

🤖 Machine learning

🌦️ Live weather data

🧑‍💻 Modern interactive UI

...to ensure crop and climate-specific suggestions that are:

✅ Accurate
🔄 Dynamic
👌 User-friendly

✨ Key Features
🧠 Personalized Fertilizer Advice
Input: Soil Type, Crop Type, Soil pH, City/Location

Output:

📌 Best Fertilizer Type

⚖️ Recommended Quantity

⏰ Ideal Timing (before/after rain)

☁️ Live Weather Integration
Fetches real-time temperature, humidity, and rainfall from OpenWeatherMap

Ensures weather-aware fertilizer suggestions

🧬 Machine Learning Driven
Powered by a pre-trained ML model

Trained on historical soil, crop, and climate data

Predictions are fast and data-informed

🖥️ Modern, Interactive UI
Built with HTML/CSS/JS and AJAX for dynamic UX

Clean and responsive layout

No page reloads! 🚫🔁

🧩 Easy to Extend
Modular design

Future-ready: Add-on features like crop disease prediction, irrigation advice, etc.

🔍 How It Works
<details> <summary>📋 <strong>User Journey</strong> (Click to expand)</summary>
User opens the app

Clicks "Optimal Fertilizer Suggestion"

Fills in:

Soil Type

Crop Type

pH Level

City Name

Clicks "Analyze"

App:

🔍 Fetches live weather data via OpenWeatherMap API

📊 Encodes & feeds all data to the ML model

🎯 Predicts:

Fertilizer type

Quantity (kg/hectare)

Ideal application timing

📋 Instantly shows recommendations without reloading the page

</details>
🛠️ Tech Stack
Technology	Role
Flask	Python web server & backend logic
Scikit-learn	ML model training & prediction
OpenWeatherMap	Real-time weather data API
HTML/CSS/JS	Frontend (form, layout, AJAX)
Pickle	Model & encoder serialization
.env	Secure API key management

👥 Who Is It For?
👨‍🌾 Farmers & Agro-Advisors: Get crop-specific, environment-aware fertilizer advice.

🎓 Students: Hands-on tool for learning agri-tech & machine learning.

💡 Researchers & Developers: Base framework for agri-intelligence systems.

✅ Key Benefits
♻️ Reduces Waste: Avoids over/under-fertilization

🌱 Boosts Yield: Advice aligned to crop and climate

⏱️ Saves Time: Instant insights via simple interface

🌍 Eco-Smart: Encourages sustainable farming

📌 Example Use Case
🧑‍🌾 A wheat farmer in Mumbai enters:

Soil Type: Loamy  
Crop Type: Wheat  
Soil pH: 6.5  
City: Mumbai
🧪 The app fetches live weather and recommends:
✅ Fertilizer: Urea
✅ Quantity: 120 kg/hectare
✅ Timing: At the sowing stage

🎯 Demo / Screenshots
live weather fetch, form input, prediction result display

<img width="1895" height="954" alt="Screenshot 2025-07-24 014356" src="https://github.com/user-attachments/assets/7f3bc7ad-8c7c-40bc-b3f5-10040d59194b" />
<img width="1916" height="952" alt="Screenshot 2025-07-27 191133" src="https://github.com/user-attachments/assets/6a9e5ffc-b304-4fb5-ab39-3a3e430f7bdc" />
<img width="1919" height="950" alt="Screenshot 2025-07-27 191145" src="https://github.com/user-attachments/assets/699aefda-9939-4eff-9400-982c0ad5eaed" />
<img width="1919" height="953" alt="Screenshot 2025-07-27 191219" src="https://github.com/user-attachments/assets/5002167a-d547-4e8a-85e0-628490ceb1ee" />

