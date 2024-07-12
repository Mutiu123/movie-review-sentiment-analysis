### **Project Description**
The **Sentiment Analysis Tool** is designed to predict the sentiment (positive or negative) of movie reviews. By analyzing textual data, it provides insights into audience reactions, which can be valuable for filmmakers, critics, and movie enthusiasts.

### **Problem Statement**
Movie reviews are abundant on various platforms, but manually assessing their sentiment can be time-consuming. The goal of this project is to automate sentiment classification, making it easier to understand overall audience sentiment toward a film.

### **Methodology**
1. **Data Preprocessing:**
   - Load the movie review dataset from a CSV file.
   - Clean the data by removing stopwords and irrelevant characters.

2. **Feature Extraction:**
   - Use the TF-IDF vectorizer to convert text data into numerical features.
   - Limit the number of unique words considered.

3. **Model Training:**
   - Train a logistic regression model on the preprocessed data.
   - Fine-tune hyperparameters for better performance.

4. **Evaluation:**
   - Assess model accuracy using a confusion matrix.
   - Visualize the results.

5. **Model Persistence:**
   - Save the trained model and vectorizer for future use.

### **Contributions**
- **Technical Contribution:**
  - Implement efficient data preprocessing and feature extraction.
  - Develop a robust logistic regression model.
  - Create a user-friendly Streamlit app for prediction.

- **Practical Contribution:**
  - Enable quick sentiment analysis for movie reviews.
  - Facilitate decision-making for filmmakers and marketers.

### **Deployment Process**
1. Install necessary Python libraries (Pandas, NLTK, Matplotlib, scikit-learn, WordCloud, Streamlit).
2. Load your movie review dataset.
3. Train the model and save it using `pickle`.
4. Build a Streamlit app for user interaction.
5. Deploy the app to a web server or cloud platform.

### **Impact and Practical Applications**
- **Film Industry:**
  - Filmmakers can gauge audience reactions during pre-release screenings.
  - Marketing teams can tailor promotional campaigns based on sentiment analysis.

- **Review Aggregators:**
  - Platforms like IMDb or Rotten Tomatoes can enhance their rating systems.
  - Users can filter reviews based on sentiment.

- **Social Media Monitoring:**
  - Brands can analyze sentiment around movie releases on social media.
  - Adjust marketing strategies accordingly.

### **Conclusion**
The Sentiment Analysis Tool simplifies the process of understanding movie reviews. By automating sentiment classification, it contributes to informed decision-making in the entertainment industry. As you continue to refine and expand this project, consider exploring other genres (e.g., TV shows, music) and incorporating more advanced machine learning techniques.

## **System Demo:**

![The System Demo]("https://github.com/Mutiu123/movie-review-sentiment-analysis/blob/main/demo/demo.png")


## **To run the model**
1. **Clone the Repository**:
   - First, clone the repository containing the heart disease prediction system code to your local machine. You can do this using Git or by downloading the ZIP file from the repository.

2. **Install Dependencies**:
   - Open your terminal or command prompt and navigate to the project directory.
   - Install the necessary Python libraries mentioned in the `requirements.txt` file using the following command:
     ```
     pip install -r requirements.txt
     ```

3. **Run the Streamlight App**:
   - In the same terminal or command prompt, execute the following command to run the Streamlight app:
     ```
     streamlet run app.py
     ```
   - This will start the local development server, and you'll see a message indicating that the app is running.
   - Open your web browser and visit `http://localhost:8501` (or the URL provided in the terminal) to access the interactive web app.

4. **Predict Heart Disease**:
   - On the Streamlit app, you'll find a search bar where you can Fill in the relevant information for a patient you want to assess.
   - After entering the patient’s details, click the “Predict” button.

## **Model Deployement**
I Deploy the Streamlight app on Heroku to allow others to access it online Here's an updated step-by-step guide on how to run the app on your device:

1. **Access the Deployed App**:
   - Visit the following link: [Movie Review Sentiment Analysis](https://mrsasys-7c869fa7f5db.herokuapp.com/).
   - You'll see the web interface where users can input patient information and get predictions.

2. **Interact with the App**:
   - On the web page, you'll find input fields for Reviewer to enter their comment/review.
   - Fill in the relevant information.

3. **Click the "Predict" Button**:
   - After entering the patient's details, click the "Click to Predict" button.
   - The app will process the input.

4. **View the Prediction**:
   - The app will display the prediction result: